import streamlit as st
from auth.auth_page import auth_page
from contacts.dashboard import dashboard
from auth.session import is_logged_in

st.set_page_config(page_title="Contact Manager", layout="centered")

# Initialize page state
if 'page' not in st.session_state:
    st.session_state.page = 'auth'

# Auto-redirect if already logged in
if is_logged_in():
    st.session_state.page = 'dashboard'

# Routing
if st.session_state.page == 'dashboard':
    dashboard()
else:
    auth_page()
