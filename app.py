import streamlit as st
from streamlit.components.v1 import html

# Authentication
def check_password():
    """Returns `True` if the user entered the correct password."""
    
    def password_entered():
        if st.session_state["password"] == st.secrets["PASSWORD"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input(
            "Password", type="password", key="password", on_change=password_entered
        )
        return False
    elif not st.session_state["password_correct"]:
        st.text_input(
            "Password", type="password", key="password", on_change=password_entered
        )
        st.error("😕 Password incorrect")
        return False
    else:
        return True

if check_password():
    st.title("Akhand Unified Dashboard")
    
    tab1, tab2 = st.tabs(["Public App", "Private App"])
    
    with tab1:
        st.header("Public Application")
        html(
            f'<iframe src="https://akhand.streamlit.app/" width="100%" height="800"></iframe>',
            height=800,
        )
    
    with tab2:
        st.header("Private Application")
        html(
            f'<iframe src="https://akhand-selected-people.streamlit.app/" width="100%" height="800"></iframe>',
            height=800,
        )
