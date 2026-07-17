import streamlit as st
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
db = firebase.database()

# ---------------- Page ----------------
st.set_page_config(page_title="Create Profile", page_icon="👤")

st.title("👤 Create Your Profile")

name = st.text_input("Full Name")
phone = st.text_input("Phone Number")
age = st.number_input("Age", 1, 100)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])

profile_pic = st.file_uploader(
    "Upload Profile Picture",
    type=["jpg", "jpeg", "png"]
)

if st.button("Save Profile"):

    # Save in session state
    st.session_state["name"] = name
    st.session_state["phone"] = phone
    st.session_state["age"] = age
    st.session_state["gender"] = gender
    st.session_state["profile_pic"] = profile_pic

    # Save in Firebase Database
    data = {
        "name": name,
        "phone": phone,
        "age": age,
        "gender": gender,
        "email": st.session_state.get("email", "")
    }

    db.child("Users").child(
        st.session_state.get("email", "").replace(".", "_")
    ).set(data)

    st.success("✅ Profile Created Successfully!")

    st.switch_page("pages/app.py")
