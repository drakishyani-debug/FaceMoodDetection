import streamlit as st

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #081A4B 0%, #0B2C8C 50%, #102D72 100%);
    color: white;
}

/* Login form */
div[data-testid="stForm"],
div[data-testid="stVerticalBlock"] {
    background: rgba(255,255,255,0.05);
    border-radius: 15px;
    padding: 20px;
}

/* Labels */
label {
    color: white !important;
}

/* Button */
.stButton > button {
    background-color: #2196F3;
    color: white;
    border-radius: 8px;
    border: none;
}

.stButton > button:hover {
    background-color: #1976D2;
}
</style>
""", unsafe_allow_html=True)
import pyrebase

firebaseConfig = {
    "apiKey":"AIzaSyBArammCIVUuo1xhF5H1RzeiN7IAWHZsdQ",
    "authDomain": "facemooddetection.firebaseapp.com",
    "databaseURL": "https://facemooddetection-default-rtdb.firebaseio.com/",
    "projectId": "facemooddetection",
    "storageBucket": "facemooddetection.firebasestorage.app",
    "messagingSenderId": "153465858963",
    "appId": "1:153465858963:web:116408eedfcc72fd66d666"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# ---------------- LOGIN PAGE ----------------

st.title("🔐 Face Mood Detection Login")

choice = st.sidebar.selectbox(
    "Login / Signup",
    ["Login", "Sign Up"]
)

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if choice == "Sign Up":
    if st.button("Create Account"):
        try:
            auth.create_user_with_email_and_password(email, password)
            st.success("✅ Account created successfully!")
        except Exception as e:
            st.error(f"Error: {e}")

if choice == "Login":
    if st.button("Login"):
        try:
            auth.sign_in_with_email_and_password(email, password)
            st.session_state["logged_in"] = True
            st.switch_page("pages/app.py")
        except Exception as e:
            import json
            st.error(e)
            
# Stop here if not logged in
if not st.session_state.get("logged_in"):
    st.stop()
