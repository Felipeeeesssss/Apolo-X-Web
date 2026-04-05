import streamlit as st

# 1. Configuración de página minimalista
st.set_page_config(page_title="APOLO X", page_icon="⚪️", layout="centered")

# 2. CSS Avanzado para estética Premium y "Cero Iconos"
st.markdown("""
    <style>
    /* Fondo blanco y texto negro */
    .stApp { background-color: #ffffff; color: #000000; }
    
    /* ESCONDER ICONOS Y ROLES COMPLETAMENTE */
    [data-testid="stChatMessageAvatarUser"], 
    [data-testid="stChatMessageAvatarAssistant"],
    [data-testid="stChatMessage"] h2 { display: none !important; }
    
    /* Burbujas minimalistas (Estilo mensajería moderna) */
    [data-testid="stChatMessage"] {
        background-color: #f0f2f5; 
        border-radius: 18px; 
        padding: 12px 16px;
        margin-bottom: 8px;
        border: none;
        max-width: 85%;
        margin-left: 0 !important; /* Quita el margen de los iconos */
    }
    
    /* ALINEAR MENSAJES DEL USUARIO A LA DERECHA */
    [data-testid="stChatMessage"][data-testid="stChatMessageUser"] {
        background-color: #007bff; /* Color azul tipo Instagram/iMessage */
        color: #ffffff;
        margin-left: auto !important; /* Empuja a la derecha */
        margin-right: 0 !important;
    }
    
    /* Color de texto negro para el asistente */
    [data-testid="stChatMessage"][data-testid="stChatMessageAssistant"] {
        color: #000000;
    }

    /* Cuadro de entrada minimalista */
    .stChatInputContainer { padding-bottom: 20px; border-top: 1px solid #e6e6e6; }
    
    /* Contenedor del Logo */
    .logo-container {
        text-align: center;
        margin-top: -60px; /* Sube el logo */
        margin-bottom: 30px;
    }
    </style>
    <div class="logo-container">
        <h1 style="font-family: 'Helvetica Neue', Arial, sans-serif; font-weight: bold; color: #000000; font-size: 32px; letter-spacing: -1px; margin-bottom: 0;">APOLO</h1>
        <h1 style="font-family: 'Times New Roman', serif; font-weight: normal; font-style: italic; color: #000000; font-size: 28px; margin-top: -5px;">X</h1>
    </div>
    """, unsafe_allow_html=True)

# 3. Lógica del Chat (Iniciarla si está vacía)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Mostrar los mensajes sin avatars
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. LÓGICA DE RESPUESTA (Cerebro Básico) ---
if prompt := st.chat_input("Escribe un mensaje..."):
    # Guardar y mostrar tu mensaje
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Respuesta de APOLO X
    with st.chat_message("assistant"):
        p = prompt.lower()
        if "hola" in p:
            respuesta = "Hola. ¿En qué puedo ayudarte hoy?"
        elif "quien eres" in p:
            respuesta = "Soy APOLO X, tu asistente digital personal."
        elif "creador" in p:
            respuesta = "He sido diseñado bajo los parámetros de simplicidad y elegancia de Felipe."
        else:
            respuesta = f"He recibido tu instrucción: '{prompt}'. Estoy procesando la información."
        
        st.markdown(respuesta)
    
    # Guardar la respuesta del asistente
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
