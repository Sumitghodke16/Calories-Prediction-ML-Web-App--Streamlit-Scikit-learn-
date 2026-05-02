import streamlit as st
import joblib
import numpy as np

# ---------------- CUSTOM CSS ----------------
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #00B4D8;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        font-weight: bold;
    }

    div.stButton > button:hover {
        background-color: #0096C7;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
bundle = joblib.load("calories_model.pkl")
model = bundle["model"]
features_order = bundle["features"]

# ---------------- TITLE ----------------
st.title("🔥 Calories Prediction App")
st.caption("Input your activity data to predict calories burned!")

# ---------------- IMAGE ----------------
st.image("image/guide.png")

# ---------------- COLUMNS WITH SPACE ----------------
col1, spacer, col2 = st.columns([2, 0.3, 1])

# ---------------- LEFT SIDE (INPUTS) ----------------
with col1:
    st.subheader("📥 Enter Activity Details")

    steps = st.slider("Total Steps", 0, 20000, 5000)
    distance = st.slider("Total Distance (km)", 0.0, 20.0, 4.0)

    very_active = st.slider("Very Active Minutes", 0, 120, 20)
    fairly_active = st.slider("Fairly Active Minutes", 0, 120, 10)
    light_active = st.slider("Lightly Active Minutes", 0, 300, 60)
    sedentary = st.slider("Sedentary Minutes", 0, 1000, 500)

    st.write("")  # spacing
    predict_btn = st.button("🚀 Predict Calories")

# ---------------- PREDICTION LOGIC ----------------
if predict_btn:
    values = {
        'TotalSteps': steps,
        'TotalDistance': distance,
        'VeryActiveMinutes': very_active,
        'FairlyActiveMinutes': fairly_active,
        'LightlyActiveMinutes': light_active,
        'SedentaryMinutes': sedentary
    }

    X_input = np.array([[values[f] for f in features_order]])
    prediction = model.predict(X_input)
    result = prediction[0]
else:
    result = None

# ---------------- RIGHT SIDE (OUTPUT) ----------------
with col2:
    st.subheader("🔥 Prediction Result")

    if result is not None:
        st.markdown(f"## 🔥 {result:.2f} kcal")
        st.success("Great job! Keep going 💪")
    else:
        st.info("Enter values and click predict")