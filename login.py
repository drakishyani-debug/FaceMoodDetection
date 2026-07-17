import streamlit as st

st.markdown("""
<style>

/* Same background as app.py */
body {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1a4e 50%, #0f0f2e 100%);
}

.stApp {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1a4e 50%, #0f0f2e 100%);
}

[data-testid="stAppViewContainer"]{
    background: linear-gradient(135deg, #0a0e27 0%, #1a1a4e 50%, #0f0f2e 100%);
}

[data-testid="stMainBlockContainer"]{
    background: transparent;
    padding-top:2rem;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background: rgba(15,15,46,0.95);
}

/* Login Card */
.login-card{
    background: rgba(255,255,255,0.08);
    border:1px solid rgba(255,255,255,0.15);
    border-radius:20px;
    padding:30px;
    backdrop-filter: blur(10px);
    box-shadow:0 8px 32px rgba(31,38,135,0.37);
}

/* Heading */
.login-title{
    text-align:center;
    font-size:3rem;
    font-weight:900;
    background: linear-gradient(135deg,#00d4ff,#7f5af0);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:20px;
}

/* Labels */
label{
    color:white !important;
    font-weight:bold;
}

/* Text Inputs */
.stTextInput input{
    background:rgba(255,255,255,0.08) !important;
    color:white !important;
    border:1px solid rgba(0,212,255,0.4) !important;
    border-radius:10px !important;
}

/* Buttons */
.stButton>button{
    width:100%;
    background:linear-gradient(135deg,#00d4ff,#7f5af0)!important;
    color:white!important;
    border:none!important;
    border-radius:10px!important;
    padding:10px!important;
    font-weight:bold!important;
}

.stButton>button:hover{
    box-shadow:0 0 20px rgba(0,212,255,.5)!important;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"]{
    background:rgba(255,255,255,0.08);
    border-radius:10px;
}

/* Success/Error */
.stSuccess,.stError{
    border-radius:10px!important;
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
