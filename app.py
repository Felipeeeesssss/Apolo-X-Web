import streamlit as st

st.set_page_config(page_title="APOLO X", layout="wide", initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
    html, body, .stApp {
        background: #ffffff !important;
    }

    #MainMenu, footer, header {
        visibility: hidden !important;
        height: 0 !important;
        min-height: 0 !important;
    }

    .block-container {
        max-width: 1100px !important;
        padding-top: 1rem !important;
        padding-bottom: 5rem !important;
    }

    .apolo-logo {
        text-align: center;
        margin: 0.25rem 0 1rem 0;
        line-height: 1;
        user-select: none;
    }

    .apolo-logo .main {
        font-family: sans-serif;
        font-weight: 900;
        font-size: 2.2rem;
        letter-spacing: 0.22em;
        color: #000000;
        margin: 0;
        padding: 0;
    }

    .apolo-logo .sub {
        font-family: serif;
        font-style: italic;
        font-size: 1.35rem;
        font-weight: 400;
        color: #000000;
        margin: -0.15rem 0 0 0;
        padding: 0;
    }

    [data-testid="stChatMessage"] {
        width: 100%;
        display: flex;
        margin: 0.35rem 0;
        align-items: flex-start;
    }

    [data-testid="stChatMessage"] > div:first-child,
    [data-testid="stChatMessageAvatarUser"],
    [data-testid="stChatMessageAvatarAssistant"] {
        display: none !important;
        width: 0 !important;
        min-width: 0 !important;
        max-width: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        overflow: hidden !important;
    }

    [data-testid="stChatMessageContent"] {
        padding: 0.8rem 1rem !important;
        border-radius: 999px !important;
        max-width: min(78%, 72ch) !important;
        width: fit-content !important;
        overflow-wrap: anywhere !important;
        word-break: break-word !important;
        box-shadow: none !important;
    }

    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
        justify-content: flex-start;
    }

    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"] {
        background: #f2f2f2 !important;
        border: 1px solid #f2f2f2 !important;
        color: #000000 !important;
        font-weight: 800 !important;
        text-align: center !important;

        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"] p {
        margin: 0 !important;
        width: 100% !important;
        color: inherit !important;
        font-weight: inherit !important;
    }

    [data-testid="stChatMessage"]:not(:has([data-testid="stChatMessageAvatarUser"])) {
        justify-content: flex-end;
    }

    [data-testid="stChatMessage"]:not(:has([data-testid="stChatMessageAvatarUser"])) [data-testid="stChatMessageContent"] {
        background: #ffffff !important;
        border: 1px solid #dddddd !important;
        color: #000000 !important;
        font-weight: 400 !important;
        text-align: center !important;

        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    [data-testid="stChatMessage"]:not(:has([data-testid="stChatMessageAvatarUser"])) [data-testid="stChatMessageContent"] p {
        margin: 0 !important;
        width: 100% !important;
        color: inherit !important;
        font-weight: inherit !important;
    }

    [data-testid="stChatInput"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    [data-testid="stChatInput"] > div,
    [data-testid="stChatInput"] > div > div,
    [data-testid="stChatInput"] [data-baseweb="textarea"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    textarea[data-testid="stChatInputTextArea"] {
        background: #ffffff !important;
        border: 1px solid #dddddd !important;
        border-radius: 999px !important;
        box-shadow: none !important;
        outline: none !important;
        resize: none !important;
        min-height: 54px !important;
        padding: 0.9rem 1.1rem !important;
        color: #000000 !important;
    }

    textarea[data-testid="stChatInputTextArea"]::placeholder {
        color: #888888 !important;
    }

    textarea[data-testid="stChatInputTextArea"]:focus {
        border: 1px solid #cccccc !important;
        box-shadow: none !important;
        outline: none !important;
    }

    button[data-testid="stChatInputSubmitButton"] {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="apolo-logo">
        <div class="main">APOLO</div>
        <div class="sub">X</div>
    </div>
    """,
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hola."}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Escribe algo...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": "Estoy aquí."})
    st.rerun()
