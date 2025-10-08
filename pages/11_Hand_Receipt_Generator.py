import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Access Restricted",
    page_icon="🚫",
    layout="centered"
)

# Display access restricted message
st.error("### 🚫 Access Restricted")
st.markdown("""
This tool has been removed from the PWD Tools Hub.
Please return to the main page to access available tools.
""")

# Add a button to return to home
if st.button("Return to Home", use_container_width=True):
    st.switch_page("app.py")
