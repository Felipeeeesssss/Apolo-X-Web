import streamlit as st

# Configuración de página con estética oscura y limpia
st.set_page_config(page_title="APOLO X", page_icon="🔘")

# CSS para inyectar el estilo "Dark Elegant"
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .stChatInput { border-radius: 20px; }
    .stChatMessage { border-radius: 10px; border: 1px solid #30363d; }
    h1 { font-family: 'Segoe UI', sans-serif; letter-spacing: -1px; }
    </style>
    """, unsafe_allow_html=True)

st.title("APOLO X")
st.write("---") # Una línea sutil para separar

# El historial de mensajes (Memoria de la sesión)
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Cuadro de entrada tipo GPT
if prompt := st.chat_input("Escribe tu comando para APOLO X..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Respuesta simulada mientras conectamos el cerebro
    with st.chat_message("assistant"):
        st.markdown("Sistemas operativos de APOLO X v1.0 en línea. Esperando integración de lenguaje.")
