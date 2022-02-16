import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
col1, col2, col3 = st.columns(3)

col1.image(Image.open('streamlit-logo-secondary-colormark-darktext.png'))
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

a1, a2, a3, a4 = st.columns(4)
with a1:
    with st.container():
        st.metric("Temperature", "70 °F", "1.2 °F")
    with st.container():
        st.metric("Temperature", "70 °F", "1.2 °F")
a2.metric("Wind", "9 mph", "-8%")
a3.metric("Humidity", "86%", "4%")
a4.metric("Humidity", "86%", "4%")
