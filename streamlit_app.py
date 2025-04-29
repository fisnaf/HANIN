import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Detektif Sel", layout="wide")
st.title("🕵️‍♂️ Detektif Sel: Klasifikasi Misteri!")

st.markdown("""
Kamu adalah seorang detektif biologi! Beberapa gambar sel ditemukan di laboratorium misterius.
Tugasmu adalah mengamati ciri-cirinya, lalu menebak apakah itu **Sel Hewan**, **Sel Tumbuhan**, atau **Bakteri**.
""")

# Data sel
