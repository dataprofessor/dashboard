import streamlit as st

st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

a1, a2, a3, a4 = st.columns(4)
a1.metric("Temperature", "70 °F", "1.2 °F")
a2.metric("Wind", "9 mph", "-8%")
a3.metric("Humidity", "86%", "4%")
a4.metric("Humidity", "86%", "4%")
