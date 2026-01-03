import streamlit as st
import requests

st.set_page_config(page_title="Language Translator", page_icon="🌍")
st.title("🌍 Multi-Language Translator")
st.write("Translate between English and world languages (Press Enter)")

# Language options
LANGUAGES = {
    "English": "en",
    "Russian": "ru",
    "Japanese": "ja",
    "Chinese": "zh",
    "German": "de",
    "Spanish": "es",
    "French": "fr",
    "Italian": "it",
    "Persian": "fa",
    "Urdu": "ur"
}

source_lang = st.selectbox("From", LANGUAGES.keys(), index=0)
target_lang = st.selectbox("To", LANGUAGES.keys(), index=1)

text = st.text_input("Enter text and press Enter")

def translate(text, source, target):
    url = "https://libretranslate.de/translate"
    payload = {
        "q": text,
        "source": source,
        "target": target,
        "format": "text"
    }
    try:
        response = requests.post(url, data=payload, timeout=10)
        return response.json()["translatedText"]
    except:
        return "⚠️ Translation failed. Try again."

if text:
    result = translate(text, LANGUAGES[source_lang], LANGUAGES[target_lang])
    st.subheader("✅ Translation")
    st.success(result)
