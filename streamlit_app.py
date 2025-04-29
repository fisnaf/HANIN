import streamlit as st

st.set_page_config(page_title="Perbandingan Sel", layout="centered")
st.title("🔬 Perbandingan Sel Prokariotik dan Eukariotik")

st.markdown("Bandingkan dua jenis sel utama dengan mencentang ciri-cirinya.")

col1, col2 = st.columns(2)

with col1:
    st.header("🦠 Prokariotik")
    prokaryotic = st.checkbox("Tidak punya inti sel")
    st.checkbox("DNA melingkar")
    st.checkbox("Tidak punya organel membran")
    st.checkbox("Bentuk sederhana")
    st.checkbox("Contoh: Bakteri")

with col2:
    st.header("🧫 Eukariotik")
    eukaryotic = st.checkbox("Punya inti sel")
    st.checkbox("DNA linear")
    st.checkbox("Punya organel bermembran")
    st.checkbox("Bentuk kompleks")
    st.checkbox("Contoh: Hewan & Tumbuhan")

st.markdown("---")
if st.button("Selesai Bandingkan"):
    st.success("Bagus! Kamu sudah memahami struktur dasar perbedaan dua jenis sel.")
