import streamlit as st


def contact_page():
    a, b = st.columns([0.9, 1.4])
    a.image('https://www.ipmc.cnrs.fr/fichiers/images/photo_1.jpg')
    st.markdown("<h3 style='text-align: center; color: black;'>Introduction</h1>", unsafe_allow_html=True)
