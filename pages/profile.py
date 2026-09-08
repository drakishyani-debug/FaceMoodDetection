import streamlit as st
import pyrebase

st.set_page_config(
    page_title="Profile",
    page_icon="👤"
)

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
db = firebase.database()

# Check login
uid = st.session_state.get("uid")
id_token = st.session_state.get("id_token")

if not uid or not id_token:
    st.error("❌ Please login first.")
    st.stop()

# Get existing profile from Firebase
try:
    user = db.child("Users").child(uid).get(token=id_token).val()
except Exception as e:
    st.error(f"❌ Could not load profile: {e}")
    st.stop()

# Check whether profile has actually been created
profile_exists = (
    user
    and user.get("name")
    and user.get("phone")
    and user.get("age")
    and user.get("gender")
)

if profile_exists:

    # ================= EXISTING PROFILE =================

    st.title("👤 My Profile")

    st.success("✅ Profile already created")

    st.write("### Profile Details")

    st.write(f"**Name:** {user.get('name')}")
    st.write(f"**Email:** {user.get('email', st.session_state.get('email', ''))}")
    st.write(f"**Phone:** {user.get('phone')}")
    st.write(f"**Age:** {user.get('age')}")
    st.write(f"**Gender:** {user.get('gender')}")

    st.divider()

    if st.button("🚀 Go to Face Mood Detection"):
        st.switch_page("pages/app.py")

else:

    # ================= CREATE PROFILE =================

    st.title("👤 Create Your Profile")

    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    age = st.number_input("Age", 1, 100)
    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    profile_pic = st.file_uploader(
        "Upload Profile Picture",
        type=["jpg", "jpeg", "png"]
    )

    if st.button("Save Profile"):

        data = {
            "name": name,
            "phone": phone,
            "age": age,
            "gender": gender,
            "email": st.session_state.get("email", "")
        }

        try:
            db.child("Users").child(uid).set(
                data,
                token=id_token
            )

            # Update session state
            st.session_state["name"] = name
            st.session_state["phone"] = phone
            st.session_state["age"] = age
            st.session_state["gender"] = gender

            st.success("✅ Profile Created Successfully!")

            st.switch_page("pages/app.py")

        except Exception as e:
            st.error(f"❌ Profile Save Error: {e}")
