import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="RickBot - Rick and Morty Chat",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --- Custom CSS Styling ---
def inject_custom_css(theme="light"):
    if theme == "dark":
        st.markdown(
            """
            <style>
            body {
                background-color: #0e1117;
                color: #f0f0f0;
            }
            .css-18e3th9 {
                background-color: #0e1117;
            }
            iframe {
                border-radius: 10px;
                border: 2px solid #3e3e3e;
            }
            </style>
        """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
            iframe {
                border-radius: 10px;
                border: 2px solid #ddd;
            }
            </style>
        """,
            unsafe_allow_html=True,
        )


# --- Sidebar Chat History (Simulated) ---
with st.sidebar:
    st.title("💬 RickBot History")
    theme_toggle = st.radio("🌓 Theme", ["Light", "Dark"])
    st.markdown("---")
    chat_history = st.session_state.get("chat_history", [])
    if chat_history:
        for i, chat in enumerate(chat_history):
            st.markdown(f"**Chat {i + 1}:** {chat}")
    else:
        st.markdown("_No previous chats yet._")

# --- Chat Input Simulation (optional for logging history) ---
st.sidebar.markdown("---")
user_message = st.sidebar.text_input("🗨️ Say something to Rick...")
if user_message:
    st.session_state.chat_history = st.session_state.get("chat_history", []) + [
        user_message
    ]

# --- Apply Theme ---
inject_custom_css(theme_toggle.lower())

# --- Main UI ---
st.title("🤖 RickBot - Chat with Rick Sanchez")
st.caption(
    "Welcome to the multi-purpose RickBot powered by Dify.ai. Get ready for genius sarcasm and interdimensional banter!"
)

st.markdown(
    f"""
<iframe
    src="https://udify.app/chatbot/ps7JaGJuAW3iw1h5"
    style="width: 100%; height: 700px;"
    frameborder="0"
    allow="microphone">
</iframe>
""",
    unsafe_allow_html=True,
)
