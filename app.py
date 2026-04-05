import streamlit as st

# Configuración de página minimalista
st.set_page_config(page_title="APOLO X", page_icon="⚪️")

# CSS para el diseño exacto: Tú (Gris/Izquierda), IA (Blanco/Derecha)
st.markdown("""
    <style>
    .stApp { background-color: #f7f7f8; }
    
    /* Esconder elementos de IA por defecto */
    [data-testid="stChatMessageAvatarUser"], 
    [data-testid="stChatMessageAvatarAssistant"],
    [data-testid="stChatMessage"] h2 { display: none !important; }

    /* Estilo general de las burbujas */
    [data-testid="stChatMessage"] {
        padding: 0px !important;
        background-color: transparent !important;
    }

    /* TUS MENSAJES (Izquierda, Gris, Texto Negro Fuerte) */
    [data-testid="stChatMessage"][data-testid="stChatMessageUser"] > div {
        background-color: #e9e9eb !important;
        color: #1a1a1a !important;
        border-radius: 20px !important;
        padding: 12px 18px !important;
        margin-left: 0px !important;
        margin-right: auto !important;
        width: fit-content !important;
        max-width: 80% !important;
        font-weight: 500 !important;
    }

    /* MENSAJES DE LA IA (Derecha, Blanco, Texto Negro) */
    [data-testid="stChatMessage"][data-testid="stChatMessageAssistant"] > div {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 20px !important;
        padding: 12px 18px !important;
        margin-right: 0px !important;
        margin-left: auto !important;
        width: fit-content !important;
        max-width: 80% !important;
        border: 1px solid #e5e5e5 !important;
    }

    /* Input de mensaje ovalado estilo GPT */
    [data-testid="stChatInput"] {
        border-radius: 25px !important;
        border: 1px solid #e5e5e5 !important;
        background-color: #ffffff !important;
    }

    /* Logo Apolo X centrado */
    .logo-container {
        text-align: center;
        margin-top: -50px;
        margin-bottom: 40px;
    }
    .apolo-text { font-family: sans-serif; font-weight: bold; font-size: 35px; margin: 0; }
    .x-text { font-family: serif; font-style: italic; font-size: 30px; margin-top: -10px; }
    </style>

    <div class="logo-container">
        <p class="apolo-text">APOLO</p>
        <p class="x-text">X</p>
    </div>
    """, unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Escribe tu mensaje..."):
    # Mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Respuesta de APOLO X
    with st.chat_message("assistant"):
        respuesta = "Entendido. Procesando comando en los sistemas de APOLO X."
        st.markdown(respuesta)
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
 
