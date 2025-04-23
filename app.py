
import streamlit as st
import google.generativeai as genai
import dotenv
import os

dotenv.load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Page config
st.set_page_config(page_title="Heart Health Assistant", page_icon="❤️", layout="centered")

# Custom CSS for better UI
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #D6336C;
            text-align: center;
        }
        .subtext {
            text-align: center;
            font-size: 18px;
            color: #555;
            margin-bottom: 30px;
        }
        .stChatInput input {
            font-size: 16px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="title">❤️ Heart Health Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Your friendly AI assistant for heart health insights and lifestyle tips</div>', unsafe_allow_html=True)

# Sidebar for health inputs
with st.sidebar:
    st.header("Your Health Info")

    age = st.slider("Age", 10, 100, 30)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    cp_type = st.selectbox("Chest Pain Type", [
        "Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"
    ])
    blood_pressure = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    cholesterol = st.number_input("Cholesterol (mg/dl)", 100, 400, 200)
    fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", ["Yes", "No"])
    rest_ecg = st.selectbox("Resting ECG Results", [
        "Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"
    ])
    st.markdown("---")
    st.info("You can modify these anytime for a personalized chat.")

# Session memory
def fetch_conversation_history():
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {
                "role": "user",
                "parts": (
                    f"System prompt: You are a Heart Health Assistant. "
                    f"Your job is to provide friendly, clear, and supportive heart health guidance. "
                    f"Consider the user's age ({age}), gender ({gender}), chest pain type ({cp_type}), "
                    f"blood pressure ({blood_pressure}), cholesterol ({cholesterol}), fasting sugar ({fasting_blood_sugar}), "
                    f"and ECG results ({rest_ecg}). "
                    f"Suggest lifestyle changes, recommend when to consult a doctor, and encourage healthy habits. "
                    f"Be warm, informative, and conversational."
                )
            }
        ]
    return st.session_state["messages"]

# Chat section
st.subheader("💬 Talk to your Heart Health Assistant")
user_input = st.chat_input("Ask me about symptoms, lifestyle changes, or heart tips...")

def get_response(messages):
    try:
        response = model.generate_content(messages)
        return response
    except Exception as e:
        return f"Error: {str(e)}"

if user_input:
    messages = fetch_conversation_history()
    messages.append({"role": "user", "parts": user_input})
    response = get_response(messages)

    try:
        reply = response.candidates[0].content.parts[0].text
    except Exception as e:
        reply = f"Oops, error: {str(e)}"

    messages.append({"role": "model", "parts": reply})

    for message in messages:
        if message["role"] == "model":
            st.markdown(f"**Heart Health Assistant:** {message['parts']}")
        elif message["role"] == "user" and "System prompt" not in message['parts']:
            st.markdown(f"**You:** {message['parts']}")
