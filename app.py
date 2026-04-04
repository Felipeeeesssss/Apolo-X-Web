import streamlit as st

# Configuración de página limpia
st.set_page_config(page_title="APOLO X", page_icon="⚪️")

# CSS para estética Blanca/Instagram
st.markdown("""
    <style>
    /* Fondo blanco total */
    .stApp { background-color: #ffffff; color: #000000; }
    
    /* Ajuste de burbujas (sin iconos de robots/personas) */
    [data-testid="stChatMessage"] {
        background-color: #f0f2f5; 
        border-radius: 20px; 
        padding: 15px;
        margin-bottom: 10px;
        border: none;
    }
    
    /* El nombre del rol oculto para que parezca chat puro */
    [data-testid="stChatMessage"] h2 { display: none; }
    
    /* Cuadro de texto abajo */
    .stChatInputContainer { padding-bottom: 20px; }
    
    /* Título minimalista */
    .main-title {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 200;
        text-align: center;
        letter-spacing: 2px;
        color: #000000;
        margin-bottom: 30px;
    }
    </style>
    <h1 class="main-title">APOLO X</h1>
    """, unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- LÓGICA DE CHAT (Para que responda) ---
if prompt := st.chat_input("Escribe un mensaje..."):
    # Tu mensaje
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Respuesta de APOLO X
    # Por ahora es una respuesta automática lógica, pronto le pondremos la API
    with st.chat_message("assistant"):
        if "hola" in prompt.lower():
            respuesta = "Hola. ¿En qué puedo ayudarte hoy?"
        elif "quien eres" in prompt.lower():
            respuesta = "Soy APOLO X, tu asistente personal."
        else:
            respuesta = f"He recibido tu mensaje: '{prompt}'. Estoy procesando la integración con mi base de datos."
        
        st.markdown(respuesta)
    
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
