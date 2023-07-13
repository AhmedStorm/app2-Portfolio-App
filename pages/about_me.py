import streamlit as st


st.header("Contact Me")

with st.form(key="forms"):
    st.text_input("Your E-Mail Address: ")
    st.text_area("Your Message: ")
    st.form_submit_button("Submit")