## Heart Health Assistant

A Streamlit-based AI chatbot that helps users understand heart health by providing personalized insights and lifestyle advice. Users can enter basic health parameters, ask questions about symptoms or prevention, and receive friendly, informative guidance. This tool is intended for educational purposes and should not replace professional medical advice.

---

### 🔧 Features

- **Interactive UI**: Clean, responsive design with sidebar inputs.
- **Health Parameters**: Users can select or enter:
  - Age
  - Gender
  - Chest pain description
  - Resting blood pressure
  - Cholesterol level
  - Fasting blood sugar
  - Resting ECG results
- **Conversational Chatbot**: Powered by Google Gemini (gemini-1.5-flash) via the `google-generativeai` API.
- **Session Memory**: Chat history persists throughout the session.

---

### ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/heart-health-assistant.git
   cd heart-health-assistant
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### 🔐 Environment Variables

Create a `.env` file in the project root containing:
```env
API_KEY=your_google_generativeai_api_key
```

---

### 🚀 Running the App

```bash
streamlit run app.py
```

The app will open in your default browser at [http://localhost:8501](http://localhost:8501).

---

### 💬 Usage

1. **Enter Health Info**: Use the sidebar to input your age, gender, and other heart health parameters.
2. **Chat with the Assistant**: Type your questions or describe symptoms in the chat box.
3. **Receive Advice**: The AI assistant will respond with personalized tips and suggestions.

---

### 🛠️ Project Structure

```
├── app.py            # Main Streamlit application
├── requirements.txt  # Python dependencies
├── .env              # Environment variables (not committed)
└── README.md         # Project documentation
```

---

### 🤝 Contributing

1. Fork this repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a Pull Request.

Please ensure your code follows proper style guidelines and includes necessary tests.

---

> **Disclaimer:** This application is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.

