import streamlit as st
from PIL import Image
import pytesseract
import requests

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Universal Translator", page_icon="🌐")
st.title("🌐 Universal Translator")
st.markdown("""
Translate **any English text or image** into multiple languages:
- Russian, Japanese, Chinese, German, Spanish, French, Italian, Persian, Urdu, Hindi
""")

# ---------------- FUNCTION ----------------
def translate_text(text, source, target):
    url = "https://libretranslate.de/translate"
    payload = {
        "q": text,
        "source": source,
        "target": target,
        "format": "text"
    }
    try:
        res = requests.post(url, data=payload, timeout=10).json()
        return res.get("translatedText", "Translation failed")
    except:
        return "Translation failed"

# ---------------- MODE SELECTION ----------------
mode = st.radio("Select Input Type:", ["Text Input", "Image Input"])

languages = {
    "English": "en",
    "Russian": "ru",
    "Japanese": "ja",
    "Chinese": "zh",
    "German": "de",
    "Spanish": "es",
    "French": "fr",
    "Italian": "it",
    "Persian": "fa",
    "Urdu": "ur",
    "Hindi": "hi"
}

if mode == "Text Input":
    source_lang = st.selectbox("From", list(languages.keys()), index=0)
    target_lang = st.selectbox("To", list(languages.keys()), index=1)
    text = st.text_input("Enter text and press Enter")

    if text:
        translated = translate_text(text, languages[source_lang], languages[target_lang])
        st.success(f"✅ Translation:\n{translated}")

else:
    source_lang = st.selectbox("From (for OCR detection)", list(languages.keys()), index=0)
    target_lang = st.selectbox("To", list(languages.keys()), index=1)
    uploaded_file = st.file_uploader("Upload an image", type=["png","jpg","jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # OCR
        try:
            extracted_text = pytesseract.image_to_string(image)
            st.info(f"📄 Extracted Text:\n{extracted_text}")
            
            if extracted_text.strip():
                translated = translate_text(extracted_text, languages[source_lang], languages[target_lang])
                st.success(f"✅ Translation:\n{translated}")
        except Exception as e:
            st.error(f"OCR Failed: {e}")
