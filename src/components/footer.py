import streamlit as st


def footer_home():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center;">
            <p style="font-weight:bold; color:white;">Created with ❤️ by</p>
            <p style="font-weight:bold; color:#FF5733;">ABHISHEK MAJILA</p>
        </div>
    """, unsafe_allow_html=True)