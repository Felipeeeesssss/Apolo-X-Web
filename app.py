import streamlit as st
from PIL import Image

# 1. Configuración de página minimalista y centrada
st.set_page_config(page_title="APOLO X", page_icon="⚪️", layout="centered")

# 2. Cargar y mostrar el Logo REAL (Asegúrate de tener logo.png en GitHub)
try:
    image = Image.open('logo.png')
    # Usamos columnas para centrar la imagen perfectamente
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(image, use_column_width=True)
except FileNotFoundError:
    st.error("No se encontró el archivo 'logo.png'. Por favor, súbelo a tu repositorio de GitHub.")
except Exception as e:
    st.error(f"Ocurrió un error al cargar el logo: {e}")

# 3. CSS Avanzado para estética Premium, Cero Iconos y Alineación Correcta
st.markdown("""
    <style>
    /* Fondo blanco total y texto negro */
    .stApp { background-color: #ffffff; color: #000000; }
    
    /* ESCONDER ICONOS Y ROLES COMPLETAMENTE */
    [data-testid="stChatMessageAvatarUser"], 
    [data-testid="stChatMessageAvatarAssistant"],
    [data-testid="stChatMessage"] h2 { display: none !important; }
    
    /* Contenedor general de mensajes */
    [data-testid="stChatMessage"] {
        background-color: transparent !important;
        padding: 0 !important;
        margin-bottom: 10px !important;
    }

    /* Burbujas minimalistas base */
    [data-testid="stChatMessage"] > div {
        border-radius: 18px !important; 
        padding: 12px 16px !important;
        border: none !important;
        max-width: 80% !important;
        width: fit-content !important;
    }
    
    /* TÚ (Izquierda, Gris, Texto Negro Fuerte) */
    [data-testid="stChatMessage"][data-testid="stChatMessageUser"] > div {
        background-color: #f0f2f5 !important; /* Gris claro */
        color: #000000 !important;
        margin-left: 0 !important;
        margin-right: auto !important;
        font-weight: 500 !important;
    }
    
    /* IA (Derecha, Blanco, Texto Negro) */
    [data-testid="stChatMessage"][data-testid="stChatMessageAssistant"] > div {
        background-color: #ffffff !important; /* Blanco */
        color: #000000 !important;
        margin-right: 0 !important;
        margin-left: auto !important;
        border: 1px solid #eaeaea !important; /* Borde sutil */
    }

    /* Cuadro de entrada minimalista y OVALADO ÚNICO */
    .stChatInputContainer {
        padding-bottom: 20px;
        border-top: 1px solid #e6e6e6;
        background-color: #ffffff;
    }
    
    /* Eliminar el rectángulo sobrepuesto del input */
    [data-testid="stChatInput"] {
        border-radius: 25px !important;
        border: 1px solid #e6e6e6 !important;
        background-color: #ffffff !important;
        box-shadow: none !important; /* Quita sombras extra */
    }
    
    /* Ajustar el padding interno del input */
    [data-testid="stChatInput"] textarea {
        padding: 10px 15px !important;
    }
    
    /* Asegurar que el texto de los mensajes sea visible */
    [data-testid="stChatMessage"] p {
        color: inherit !important;
        margin: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. Lógica del Chat (Inicializar historial si está vacío)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Mostrar los mensajes con la alineación correcta
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 6. SISTEMA DE RESPUESTA (Cerebro Básico Provisional) ---
if prompt := st.chat_input("Escribe tu mensaje..."):
    # Guardar y mostrar tu mensaje (Gris, Izquierda)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Respuesta de APOLO X (Blanco, Derecha)
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
