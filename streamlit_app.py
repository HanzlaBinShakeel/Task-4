"""
Health Information Assistant — modern Streamlit UI
Run: streamlit run streamlit_app.py
"""

import streamlit as st
from health_bot import HealthChatbot
from ui_styles import HEALTH_CSS

st.set_page_config(
    page_title="HealthGuide AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(HEALTH_CSS, unsafe_allow_html=True)

EXAMPLE_QUESTIONS = [
    "What causes a sore throat?",
    "Is paracetamol safe for children?",
    "How much water should I drink daily?",
    "What helps with mild headaches?",
]


def init_session():
    if "bot" not in st.session_state:
        with st.spinner("Loading health assistant..."):
            st.session_state.bot = HealthChatbot()
    if "messages" not in st.session_state:
        st.session_state.messages = []


def render_hero():
    st.markdown(
        """
        <motion-hero class="hero-banner">
            <h1>🩺 HealthGuide AI</h1>
            <p>Friendly general health information powered by prompt engineering &amp; safety filters.
            Not a doctor — always consult professionals for personal medical advice.</p>
        </motion-hero>
        """,
        unsafe_allow_html=True,
    )


def main():
    init_session()

    with st.sidebar:
        st.markdown("### ⚙️ Settings")
        backend = st.selectbox(
            "AI Backend",
            ["huggingface", "openai", "auto"],
            index=0,
            help="Use OpenAI only if OPENAI_API_KEY is set in .env",
        )
        if st.button("Apply backend", use_container_width=True):
            st.session_state.bot = HealthChatbot(backend=backend)

        st.markdown("---")
        st.markdown("### 💡 Try asking")
        for q in EXAMPLE_QUESTIONS:
            if st.button(q, key=f"ex_{q[:20]}", use_container_width=True):
                st.session_state.pending = q

        st.markdown("---")
        st.markdown("### 📋 About")
        st.caption(
            "**DevelopersHub Corporation** — AI/ML Internship Task 4\n\n"
            "• Prompt-engineered responses\n"
            "• Safety filters for harmful requests\n"
            "• Hugging Face or OpenAI GPT-3.5"
        )
        if st.button("🗑️ Clear chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

    col_main, col_info = st.columns([2.2, 1])

    with col_main:
        render_hero()
        st.markdown(
            '<motion-disclaimer class="disclaimer-box">'
            "⚠️ <strong>Educational use only.</strong> This bot does not diagnose, prescribe, "
            "or replace emergency care. Call emergency services for urgent symptoms."
            "</motion-disclaimer>",
            unsafe_allow_html=True,
        )

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"], avatar="🧑‍⚕️" if msg["role"] == "assistant" else "👤"):
                st.markdown(msg["content"])

        prompt = st.session_state.pop("pending", None) or st.chat_input(
            "Ask a general health question..."
        )

        if prompt:
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user", avatar="👤"):
                st.markdown(prompt)

            with st.chat_message("assistant", avatar="🧑‍⚕️"):
                with st.spinner("Thinking..."):
                    reply = st.session_state.bot.generate(prompt)
                st.markdown(reply)

            st.session_state.messages.append({"role": "assistant", "content": reply})

    with col_info:
        st.markdown("### 🛡️ Safety features")
        st.info(
            "Blocks harmful requests (self-harm, overdose, stop medication, diagnosis demands)."
        )
        st.markdown("### 📊 Skills demonstrated")
        st.markdown(
            """
            - Prompt engineering
            - LLM API integration
            - Safety handling
            - Conversational UI
            """
        )
        st.markdown("### 🚀 CLI mode")
        st.code("python health_bot.py", language="bash")


if __name__ == "__main__":
    main()
