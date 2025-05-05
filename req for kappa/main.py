import streamlit as st
from ReqForKappa import check_kappa_requirement

st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
    }

    .stButton>button {
        display: block;
        margin: 0 auto;
    }

    .stTextInput>div>div>input {
        text-align: center;
    }

    .stMarkdown, .stTextInput, .stSubheader, .stWarning, .stError {
        text-align: center;
    }

    .element-container {
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
    }
    </style>
""", unsafe_allow_html=True)

#Streamlit App
st.title("Is It Required For Kappa?")

quest_name = st.text_input("Enter the quest name to find out!")

if quest_name:
    result = check_kappa_requirement(quest_name)

    if result["match"]:
        quest = result["match"]
        st.subheader(f"✅ {quest['name']} is {'required' if quest['required'] else 'not required'} for Kappa.")
        st.markdown(f"[View on Wiki]({quest['link']})")
    elif result["suggestions"]:
        st.warning("Did you mean one of these?")
        for s in result["suggestions"]:
            st.markdown(f"- [{s['name']}]({s['link']}) {'✅ Required' if s['required'] else '❌ Not Required'}")
    else:
        st.error("Quest not found. Please check your spelling.")

        st.markdown("---")  # horizontal line

st.markdown("""
    <style>
    html, body, [data-testid="stApp"] {
        height: 100%;
        margin: 0;
        padding: 0;
    }

    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        text-align: center;
        padding: 12px;
        font-size: 16px;
        z-index: 9999;
    }

    .footer a {
        color: #1f77b4; /* Blue */
        text-decoration: none;
        padding: 0 8px;
    }

    .footer a:hover {
        text-decoration: underline;
        color: #0056b3; /* Darker blue on hover */
    }
    </style>


    <div class="footer">
        Connect with me:
        <a href="https://twitch.tv/loafedbreadd" target="_blank">Twitch</a> |
        <a href="https://twitter.com/loafedbr" target="_blank">Twitter</a> |
        <a href="https://www.youtube.com/@loafedbr" target="_blank">YouTube</a>
    </div>
""", unsafe_allow_html=True)