import streamlit as st
import os


STATIC_PASSWORD = st.secrets["password"]

st.title("Main Web App")

#Login feature

password = st.text_input("Enter Password:", type="password") if password == STATIC_PASSWORD: st.success("Access granted!")

st.subheader("Access Your Apps")

# Links to open the two apps in a new tab
st.markdown("[Open App 1](https://akhand.streamlit.app)", unsafe_allow_html=True)
st.markdown("[Open App 2](https://akhand-selected-people.streamlit.app)", unsafe_allow_html=True)

# Buttons to redirect users
if st.button("Open App 1"):
    st.markdown('<meta http-equiv="refresh" content="0; url=https://your-app1-url.streamlit.app">', unsafe_allow_html=True)

if st.button("Open App 2"):
    st.markdown('<meta http-equiv="refresh" content="0; url=https://your-app2-url.streamlit.app">', unsafe_allow_html=True)

else: st.error("Access denied. Incorrect password.")

