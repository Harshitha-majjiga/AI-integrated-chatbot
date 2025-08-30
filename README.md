# 🤖 Simple AI ChatBot with Google Gemini

This is a simple Python-based chatbot using **Google's Gemini API**.

## 🚀 Features
- Uses `gemini-1.5-flash` model.
- Stores chat history for context.
- Runs in the terminal (CLI).
- Easy to extend into a web app (Flask/Streamlit).

---

## 🛠️ Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Simple-AI-ChatBot.git
   cd Simple-AI-ChatBot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

4. Paste your API key in `botgeminiai.py`:
   ```python
   genai.configure(api_key="YOUR_API_KEY_HERE")
   ```

---

## ▶️ Run the ChatBot
```bash
python botgeminiai.py
```

Type your queries in the console, and type `quit` or `exit` to stop.

---

## 📌 Example
```
You: Hi
Bot: Hello! How can I help you today?

You: Give me AI career guidance
Bot: Sure! To start a career in AI...
```

---

## 📂 Future Improvements
- Web interface using **Flask/Streamlit**
- Save chat history to file
- Add GUI support
