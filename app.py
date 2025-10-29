import streamlit as st
import tensorflow as tf
import numpy as np
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="FAQ Text Generator",
    page_icon="🧠",
    layout="centered"
)

# =========================
# LOAD MODEL & TOKENIZER
# =========================
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("faq_nextword_model.h5")
    return model

@st.cache_resource
def load_tokenizer():
    with open("tokenizer.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()
tokenizer = load_tokenizer()
max_sequence_len = model.input_shape[1] + 1

# =========================
# HEADER
# =========================
st.title("🧠 FAQ Text Generator Dashboard")
st.markdown(
    """
    <div style='text-align: center; font-size: 17px; color: #444;'>
    Enter a starting phrase and watch your AI model complete the sentence!
    </div>
    <br>
    """,
    unsafe_allow_html=True,
)

# =========================
# TEXT GENERATION FUNCTION
# =========================
def generate_text(seed_text, next_words=10):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')
        predicted = np.argmax(model.predict(token_list, verbose=0), axis=-1)[0]

        for word, index in tokenizer.word_index.items():
            if index == predicted:
                seed_text += " " + word
                break
    return seed_text

# =========================
# INPUT SECTION
# =========================
col1, col2 = st.columns([2, 1])
with col1:
    user_input = st.text_input("Enter your starting phrase:", "What is the")

with col2:
    num_words = st.number_input("Words to generate", min_value=1, max_value=50, value=10, step=1)

# =========================
# GENERATE BUTTON
# =========================
if st.button("🚀 Generate Text"):
    with st.spinner("Generating text... please wait ⏳"):
        output = generate_text(user_input, next_words=num_words)
    st.success("✅ Generated Text:")
    st.markdown(f"<div style='padding:10px; background-color:#f6f6f6; border-radius:10px;'>{output}</div>", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown(
    """
    <hr>
    <div style='text-align:center; font-size:14px; color:#777;'>
    Built by Bhavana Koli | Powered by TensorFlow & Streamlit 🚀
    </div>
    """,
    unsafe_allow_html=True,
)
