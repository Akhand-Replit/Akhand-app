# main_app.py
import streamlit as st

# Authentication
def check_password():
    """Returns `True` if the user entered the correct password."""
    
    def password_entered():
        if "PASSWORD" in st.secrets and "password" in st.session_state:
            if st.session_state["password"] == st.secrets.PASSWORD:
                st.session_state["password_correct"] = True
                del st.session_state["password"]
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
    st.title("Akhand Unified Portal")
    
    st.subheader("Access Applications")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """<a href="https://akhand.streamlit.app/" target="_blank">
            <button style="width:100%;padding:10px;cursor:pointer;">Open Public App</button>
            </a>""",
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            """<a href="https://akhand-selected-people.streamlit.app/" target="_blank">
            <button style="width:100%;padding:10px;cursor:pointer;">Open Private App</button>
            </a>""",
            unsafe_allow_html=True
        )
    
    st.markdown("---")
    st.info("ℹ️ Apps will open in new browser tabs")
