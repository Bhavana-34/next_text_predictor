# 🧠 Next Text Predictor ⚡

A smart FAQ-style text generator built with **Streamlit** and **LSTM**! Type a phrase and watch the AI predict the rest of the question or answer.

---

## 🎥 Live Demo

See it in action!

![Next Text Predictor Demo](./demo.gif)
---

## ✨ Features

* **🤖 Smart Predictions:** Uses a powerful LSTM (Long Short-Term Memory) model to predict the next word in a sequence.
* **📚 FAQ-Trained:** Specifically trained on a dataset of Frequently Asked Questions, making it great for generating support-style text.
* **💻 Interactive UI:** A simple and clean web interface built with Streamlit.
* **✏️ Real-Time Generation:** Get predictions instantly as you type.

---

## ⚙️ How It Works

This project isn't just magic; it's a deep learning model!

1.  **Data Preprocessing:** A corpus of FAQ text is tokenized (broken into words) and converted into numerical sequences.
2.  **Model Training:** An LSTM neural network is trained on these sequences to learn the patterns and context of the language.
3.  **Prediction:** When you input a "seed phrase" (your starting text), the model predicts the most probable next word.
4.  **Iteration:** This new word is appended to the phrase, which is then fed back into the model to generate the *next* word, and so on!
5.  **Streamlit UI:** The entire process is wrapped in a user-friendly Streamlit web app, allowing you to interact with the trained model directly in your browser.

---

## 🚀 Running Locally

Want to run this on your own machine?

1.  **Clone the repository:**
    ```bash
    git clone [your-repo-link]
    cd next-text-predictor
    ```

2.  **Install the dependencies:**
    (It's highly recommended to use a virtual environment!)
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app:**
    ```bash
    streamlit run app.py
    ```

---

## 🛠️ Built With

* **Model:** TensorFlow & Keras
* **Web App:** Streamlit
* **Core:** Python
