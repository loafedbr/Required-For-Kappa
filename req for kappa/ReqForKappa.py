import requests
import difflib
from bs4 import BeautifulSoup

def format_wiki_link(quest_name):
    base = "https://escapefromtarkov.fandom.com/wiki/"
    return base + quest_name.replace(" ", "_")

def load_kappa_quests():
    url = "https://escapefromtarkov.fandom.com/wiki/Quests"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quests = {}

    for table in soup.select("table.wikitable"):
        for row in table.select("tr"):
            cells = row.find_all(['td', 'th'])
            if cells:
                quest_link = cells[0].find("a")
                if quest_link:
                    href = quest_link.get("href", "")
                    if href.startswith("/wiki/") and not any(x in href for x in ["Category:", "File:", "Template:"]):
                        quest_name = quest_link.get_text(strip=True)
                        kappa_cell = cells[-1].get_text(strip=True).lower()
                        kappa_required = kappa_cell == 'yes'
                        quests[quest_name.lower()] = {
                            "required": kappa_required,
                            "name": quest_name,
                            "link": format_wiki_link(quest_name)
                        }
    return quests

def check_kappa_requirement(user_input):
    quests = load_kappa_quests()
    user_input = user_input.strip().lower()

    if user_input in quests:
        return {"match": quests[user_input], "suggestions": None}

    # Try substring match
    matches = [name for name in quests if user_input in name]
    if not matches:
        # Fallback to fuzzy match
        matches = difflib.get_close_matches(user_input, quests.keys(), n=5, cutoff=0.6)

    if matches:
        suggestions = [quests[m] for m in matches]
        return {"match": None, "suggestions": suggestions}

    return {"match": None, "suggestions": None}