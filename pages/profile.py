import streamlit as st

st.set_page_config(page_title="Profile", page_icon="👤")

st.title("👤 User Profile")

st.write("### Name")
st.write(st.session_state.get("name", "User"))

st.write("### Email")
st.write(st.session_state.get("email", "Not Available"))

st.write("### Role")
st.write("Face Mood Detection User")

if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("login.py")
