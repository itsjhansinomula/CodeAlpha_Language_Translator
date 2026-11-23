# CodeAlpha - Task 1: Language Translation Tool
# Author: Jhansi Nomula

import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="AI Language Translator", page_icon="🌍")
st.title("🌍 AI Language Translator")
st.write("Type any text and translate it to 10+ languages using AI!")

languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Arabic": "ar"
}

text = st.text_area("Enter Text Here:", "Hello, how are you? I am learning Artificial Intelligence.")
source = st.selectbox("From Language:", list(languages.keys()), index=0)
target = st.selectbox("To Language:", list(languages.keys()), index=1)

if st.button("Translate 🔄"):
    if text.strip() == "":
        st.warning("Please enter some text!")
    else:
        try:
            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)
            st.success("Translated Text:")
            st.write(f"### {translated}")
            st.code(translated)
        except Exception as e:
            st.error(f"Translation failed. Please try again. Error: {e}")

st.markdown("---")
st.markdown("**Built by Jhansi Nomula | CodeAlpha AI Internship**")
