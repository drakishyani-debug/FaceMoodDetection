import streamlit as st

st.markdown("""
<style>

/* ===== App Background ===== */
.stApp,
[data-testid="stAppViewContainer"]{
    background: linear-gradient(135deg, #0a0e27 0%, #1a1a4e 50%, #0f0f2e 100%);
}

[data-testid="stMainBlockContainer"]{
    background: transparent;
    padding-top: 2rem;
}

/* ===== Sidebar ===== */
[data-testid="stSidebar"]{
    background: rgba(15,15,46,0.95);
}

/* Sidebar page names (login/app) */
[data-testid="stSidebarNav"] a{
    color: white !important;
    font-weight: bold !important;
}

[data-testid="stSidebarNav"] a:hover{
    color: #00d4ff !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"]{
    color: white !important;
    background: rgba(255,255,255,0.15) !important;
    border-radius: 8px;
}

/* ===== Login Card ===== */
.login-card{
    background: rgba(255,255,255,0.08);
    border:1px solid rgba(255,255,255,0.15);
    border-radius:20px;
    padding:30px;
    backdrop-filter:blur(10px);
    box-shadow:0 8px 32px rgba(31,38,135,0.37);
}

/* ===== Title ===== */
.login-title{
    text-align:center;
    font-size:3rem;
    font-weight:900;
    color:#ffffff !important;
    text-shadow:0 0 15px #00d4ff;
    margin-bottom:20px;
}

/* ===== Labels ===== */
label{
    color:white !important;
    font-weight:bold;
}

/* ===== Text Input ===== */
.stTextInput input{
    background:rgba(255,255,255,0.08) !important;
    color:black !important;
    border:1px solid rgba(0,212,255,0.4) !important;
    border-radius:10px !important;
}

/* Password Input */
.stTextInput input::placeholder{
    color:black !important;
}

/* ===== Selectbox ===== */
.stSelectbox div[data-baseweb="select"]{
    background:rgba(255,255,255,0.08) !important;
    color:white !important;
    border-radius:10px;
}

/* ===== Buttons ===== */
.stButton > button{
    width:100%;
    background:linear-gradient(135deg,#00d4ff,#7f5af0) !important;
    color:white !important;
    border:none !important;
    border-radius:10px !important;
    padding:10px !important;
    font-weight:bold !important;
}

.stButton > button:hover{
    box-shadow:0 0 20px rgba(0,212,255,0.5) !important;
}

/* ===== Messages ===== */
.stSuccess,
.stError,
.stWarning{
    border-radius:10px !important;
}

/* ===== White Headings ===== */
h1,h2,h3,h4,p{
    color:white !important;
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
db = firebase.database()

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
            user_auth = auth.create_user_with_email_and_password(
                email,
                password
            )

            uid = user_auth["localId"]
            id_token = user_auth["idToken"]

            db.child("Users").child(uid).set(
                {
                    "email": email,
                    "name": "",
                    "phone": "",
                    "age": "",
                    "gender": ""
                },
                token=id_token
            )

            st.success("✅ Account created successfully!")

        except Exception as e:
            st.error(f"❌ Signup Error: {e}")
            
if choice == "Login":
    if st.button("Login"):
        try:
            # Authenticate user
            user_auth = auth.sign_in_with_email_and_password(
                email,
                password
            )

            # Get Firebase UID and ID token
            uid = user_auth["localId"]
            id_token = user_auth["idToken"]

            # Save login session
            st.session_state["logged_in"] = True
            st.session_state["email"] = email
            st.session_state["uid"] = uid
            st.session_state["id_token"] = id_token

            # Check if profile exists using UID
            user = db.child("Users").child(uid).get(token=id_token).val()

            if user:
                st.session_state["name"] = user.get("name", "")
                st.session_state["phone"] = user.get("phone", "")
                st.session_state["age"] = user.get("age", "")
                st.session_state["gender"] = user.get("gender", "")

                st.switch_page("pages/app.py")
            else:
                st.switch_page("pages/profile.py")

        except Exception as e:
            st.error(f"❌ Login Error: {e}")

            
# Stop here if not logged in
if not st.session_state.get("logged_in"):
    st.stop()
