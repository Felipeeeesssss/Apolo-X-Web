import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="APOLO X", page_icon="⚪️", layout="centered")

# 2. CSS Definitivo (Sin imágenes externas, alineación forzada y limpieza visual)
st.markdown("""
    <style>
    /* Fondo de la aplicación completamente blanco */
    .stApp { background-color: #ffffff; }
    
    /* Ocultar barra superior extraña de Streamlit */
    header { visibility: hidden; }
    .block-container { padding-top: 2rem !important; padding-bottom: 100px !important; }

    /* OCULTAR TODOS LOS ICONOS Y NOMBRES (Avatares) */
    [data-testid="stChatMessageAvatarUser"], 
    [data-testid="stChatMessageAvatarAssistant"],
    [data-testid="stChatMessage"] h2 { display: none !important; }

    /* Configuración principal de las filas de chat */
    [data-testid="stChatMessage"] {
        background-color: transparent !important;
        padding: 0 !important;
        margin-bottom: 15px !important;
        display: flex !important;
        width: 100% !important;
    }

    /* --- TÚ (USUARIO): IZQUIERDA --- */
    [data-testid="stChatMessage"][data-testid="stChatMessageUser"] {
        justify-content: flex-start !important; /* Fuerza la izquierda */
        flex-direction: row !important;
    }
    /* Burbuja: Gris claro, ovalada, letras negras fuertes */
    [data-testid="stChatMessage"][data-testid="stChatMessageUser"] > div:last-child {
        background-color: #f0f2f5 !important;
        color: #000000 !important;
        font-weight: 700 !important; /* Letras más gruesas */
        border-radius: 20px 20px 20px 5px !important;
        padding: 12px 18px !important;
        max-width: 80% !important;
    }

    /* --- IA (ASISTENTE): DERECHA --- */
    [data-testid="stChatMessage"][data-testid="stChatMessageAssistant"] {
        justify-content: flex-end !important; /* Fuerza la derecha */
        flex-direction: row !important;
    }
    /* Burbuja: Blanca, ovalada, borde sutil, letras normales negras */
    [data-testid="stChatMessage"][data-testid="stChatMessageAssistant"] > div:last-child {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #dcdcdc !important;
        border-radius: 20px 20px 5px 20px !important;
        padding: 12px 18px !important;
        max-width: 80% !important;
        text-align: left !important;
    }

    /* --- CAJA DE TEXTO INFERIOR (ÓVALO LIMPIO) --- */
    [data-testid="stChatInputContainer"] {
        padding-bottom: 20px !important;
        background-color: #ffffff !important;
    }
    [data-testid="stChatInput"] {
        border-radius: 30px !important;
        border: 1px solid #dcdcdc !important;
        background-color: #ffffff !important;
        padding: 2px 10px !important;
        box-shadow: none !important; /* Elimina rectángulos superpuestos */
    }
    [data-testid="stChatInput"]:focus-within {
        border: 1px solid #a0a0a0 !important;
    }
    [data-testid="stChatInput"] textarea {
        color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Logo Generado por Código (100% a prueba de fallos, idéntico a tu imagen)
st.markdown("""
    <div style="text-align: center; margin-top: -30px; margin-bottom: 50px; user-select: none;">
        <div style="font-family: -apple-system, BlinkMacSystemFont, Arial, sans-serif; font-size: 55px; font-weight: 900; letter-spacing: 5px; color: black; line-height: 1;">APOLO</div>
        <div style="font-family: 'Times New Roman', Times, serif; font-size: 45px; font-style: italic; color: black; line-height: 0.7;">X</div>
    </div>
""", unsafe_allow_html=True)

# 4. Inicializar memoria del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Mostrar mensajes anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Lógica de entrada y respuesta
if prompt := st.chat_input("Escribe tu mensaje..."):
    # Guardar y mostrar tu mensaje (Aparecerá a la Izquierda)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Respuesta de APOLO X (Aparecerá a la Derecha)
    with st.chat_message("assistant"):
        respuesta = "Sistemas de APOLO X en línea. Interfaz gráfica configurada con éxito."
        st.markdown(respuesta)
    
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
