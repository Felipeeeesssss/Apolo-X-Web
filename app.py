import streamlit as st

st.set_page_config(page_title="APOLO X", layout="wide", initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
    /* =========================
       BASE
    ========================= */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background: #ffffff !important;
    }

    #MainMenu, footer, [data-testid="stHeader"], [data-testid="stToolbar"] {
        visibility: hidden !important;
        height: 0 !important;
        min-height: 0 !important;
    }

    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 6rem !important;
        max-width: 1100px !important;
    }

    /* =========================
       LOGO
    ========================= */
    .apolo-logo-wrap {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: 0.2rem 0 1rem 0;
        line-height: 1;
        user-select: none;
    }

    .apolo-logo-main {
        font-family: sans-serif;
        font-weight: 800;
        font-size: 2.2rem;
        letter-spacing: 0.22em;
        color: #000000;
        margin: 0;
        padding: 0;
    }

    .apolo-logo-sub {
        font-family: serif;
        font-style: italic;
        font-size: 1.35rem;
        font-weight: 400;
        color: #000000;
        margin: -0.1rem 0 0 0;
        padding: 0;
    }

    /* =========================
       CHAT MESSAGES
       - user: izquierda, gris claro, negrita
       - assistant: derecha, blanco con borde fino, normal
    ========================= */
    div[data-testid="stChatMessage"] {
        width: 100%;
        display: flex;
        align-items: flex-start;
        gap: 0.5rem;
        margin: 0.35rem 0;
    }

    /* User on the LEFT */
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
        flex-direction: row;
        justify-content: flex-start;
    }

    /* Assistant on the RIGHT */
    div[data-testid="stChatMessage"]:not(:has([data-testid="stChatMessageAvatarUser"])) {
        flex-direction: row-reverse;
        justify-content: flex-end;
    }

    /* Kill avatars / circles completely */
    div[data-testid="stChatMessage"] > div:first-child,
    div[data-testid="stChatMessageAvatarUser"],
    div[data-testid="stChatMessageAvatarAssistant"] {
        display: none !important;
        width: 0 !important;
        min-width: 0 !important;
        max-width: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        overflow: hidden !important;
    }

    /* Bubble base */
    div[data-testid="stChatMessageContent"] {
        width: fit-content !important;
        max-width: min(78%, 72ch) !important;
        border-radius: 999px !important;
        padding: 0.85rem 1.05rem !important;
        box-shadow: none !important;
        overflow-wrap: anywhere !important;
        word-break: break-word !important;
    }

    /* User bubble */
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) div[data-testid="stChatMessageContent"] {
        background: #f2f2f2 !important;
        border: 1px solid #f2f2f2 !important;
        color: #000000 !important;
        margin-right: auto !important;
        margin-left: 0 !important;
        text-align: left !important;
        font-weight: 800 !important;
    }

    /* Assistant bubble */
    div[data-testid="stChatMessage"]:not(:has([data-testid="stChatMessageAvatarUser"])) div[data-testid="stChatMessageContent"] {
        background: #ffffff !important;
        border: 1px solid #dddddd !important;
        color: #000000 !important;
        margin-left: auto !important;
        margin-right: 0 !important;
        text-align: left !important;
        font-weight: 400 !important;
    }

    /* Normalize text spacing */
    div[data-testid="stChatMessageContent"] p,
    div[data-testid="stChatMessageContent"] ul,
    div[data-testid="stChatMessageContent"] ol {
        margin: 0 !important;
        color: inherit !important;
    }

    div[data-testid="stChatMessageContent"] * {
        color: inherit !important;
    }

    /* Make user text strong inside bubble */
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) div[data-testid="stChatMessageContent"] * {
        font-weight: 800 !important;
    }

    /* Assistant normal weight */
    div[data-testid="stChatMessage"]:not(:has([data-testid="stChatMessageAvatarUser"])) div[data-testid="stChatMessageContent"] * {
        font-weight: 400 !important;
    }

    /* =========================
       CHAT INPUT
       One clean oval, no stacked rectangles
    ========================= */
    [data-testid="stChatInput"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Outer wrappers that often create the ugly layered look */
    div[data-testid="stChatInput"] > div,
    div[data-testid="stChatInput"] > div > div,
    div[data-testid="stChatInput"] div[data-baseweb="textarea"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    textarea[data-testid="stChatInputTextArea"] {
        background: #ffffff !important;
        border: 1px solid #e1e1e1 !important;
        border-radius: 999px !important;
        box-shadow: none !important;
        outline: none !important;
        resize: none !important;
        min-height: 54px !important;
        padding: 0.95rem 1.15rem !important;
        color: #000000 !important;
    }

    textarea[data-testid="stChatInputTextArea"]::placeholder {
        color: #888888 !important;
    }

    textarea[data-testid="stChatInputTextArea"]:focus {
        border: 1px solid #cfcfcf !important;
        box-shadow: none !important;
        outline: none !important;
    }

    button[data-testid="stChatInputSubmitButton"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="apolo-logo-wrap">
        <div class="apolo-logo-main">APOLO</div>
        <div class="apolo-logo-sub">X</div>
    </div>
    """,
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hola. Escribe algo y mira si esta interfaz deja de pelearse contigo."}
    ]

# Render history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
prompt = st.chat_input("Escribe aquí...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Demo response; reemplázalo por tu lógica real
    response = f"Recibido: {prompt}"
    st.session_state.messages.append({"role": "assistant", "content": response})

    st.rerun() 
