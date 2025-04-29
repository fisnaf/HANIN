import streamlit as st
import random

st.set_page_config(page_title="Detektif Sel", layout="wide")
st.title("🕵️‍♂️ Detektif Sel: Klasifikasi Misteri!")

st.markdown("""
Kamu adalah seorang detektif biologi! Beberapa gambar sel ditemukan di laboratorium misterius.
Tugasmu adalah mengamati ciri-cirinya, lalu menebak apakah itu **Sel Hewan**, **Sel Tumbuhan**, atau **Bakteri**.
""")

# Data sel misterius
cells = [
    {
        "id": 1,
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Animal_cell_structure-en.svg",
        "choices": ["Tidak punya dinding sel", "Ada mitokondria", "Bentuk tidak tetap"],
        "answer": "hewan"
    },
    {
        "id": 2,
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/30/Plant_cell_structure-en.svg",
        "choices": ["Ada kloroplas", "Punya dinding sel", "Ada vakuola besar"],
        "answer": "tumbuhan"
    },
    {
        "id": 3,
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Prokaryote_cell_diagram.svg",
        "choices": ["Tidak punya inti sel", "Bentuk batang", "Punya pili dan flagela"],
        "answer": "bakteri"
    }
]

sel = random.choice(cells)
st.image(sel["image"], caption="Perhatikan gambar sel ini!", use_column_width=True)
st.subheader("Apa ciri-ciri yang kamu lihat?")

selected = st.multiselect("Pilih semua ciri yang cocok:", sel["choices"])

if selected:
    st.subheader("Menurut kamu, jenis sel ini apa?")
    guess = st.radio("Jawaban kamu:", ["hewan", "tumbuhan", "bakteri"])

    if st.button("Periksa Jawaban"):
        if guess == sel["answer"]:
            st.success("Tepat! Kamu memang detektif sel yang hebat.")
            st.balloons()
        else:
            st.error(f"Belum tepat. Ini sebenarnya adalah sel {sel['answer'].capitalize()}.")
else:
    st.info("Pilih dulu ciri-ciri yang kamu amati dari gambar di atas.")
