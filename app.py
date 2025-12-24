import streamlit as st
import joblib

# Load model
model = joblib.load("models/extremism_model.pkl")

# Page config
st.set_page_config(
    page_title="Extremism Detector",
    page_icon="🚨",
    layout="centered"
)

# Custom CSS for banner and input card
st.markdown("""
    <style>
    .top-banner {
        background-color: #FF4B2B;
        padding: 15px;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    .glass-card{
        background-color: #f9f9f9;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        border: 1px solid #e0e0e0;
        margin-top: 20px;
    }
    .stTextArea textarea{
        background-color: #ffffff;
        color: black;
        font-size: 16px;
    }
    .stButton button{
        background-color: #FF4B2B;
        color: white;
        font-weight: bold;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Top banner
st.markdown('<div class="top-banner">🚨 Social Media Extremism Detector 🚨</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Subtitle
st.markdown("<p style='text-align:center; color:#555555; font-size:18px;'>Check if a message contains extremist content</p>", unsafe_allow_html=True)

# Input card
with st.container():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    user_input = st.text_area(
        "✍️ Enter a social media message here:",
        placeholder="Type your message..."
    )

    if st.button("🔍 Analyze Message"):
        if user_input.strip() == "":
            st.warning("Please write something first!")
        else:
            pred = model.predict([user_input])[0]
            proba = model.predict_proba([user_input])[0]
            ext_prob = round(proba[list(model.classes_).index("EXTREMIST")] * 100, 2)
            non_prob = round(proba[list(model.classes_).index("NON_EXTREMIST")] * 100, 2)

            st.write("---")

            # Prediction
            if pred == "EXTREMIST":
                st.error(f"⚠️ Prediction: EXTREMIST CONTENT DETECTED ({ext_prob}%)")
            else:
                st.success(f"✅ Prediction: NON-EXTREMIST CONTENT ({non_prob}%)")

            # Probability bars
            st.write("### 📊 Probabilities")
            st.progress(int(ext_prob))

            st.write(f"🔥 Extremist: **{ext_prob}%**")
            st.write(f"🕊 Non-Extremist: **{non_prob}%**")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<p style='text-align:center; color:#777777; margin-top:20px;'>
💡 Educational Purpose Only · Built with ❤️ using Streamlit
</p>
""", unsafe_allow_html=True)
