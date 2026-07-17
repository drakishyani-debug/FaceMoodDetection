import streamlit as st

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
    st.session_state["name"] = name
    st.session_state["phone"] = phone
    st.session_state["age"] = age
    st.session_state["gender"] = gender
    st.session_state["profile_pic"] = profile_pic

    st.success("✅ Profile Created Successfully!")

    st.switch_page("pages/app.py")
