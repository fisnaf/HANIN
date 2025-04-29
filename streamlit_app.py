import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Detektif Sel", layout="wide")
st.title("🕵️‍♂️ Detektif Sel: Klasifikasi Misteri!")

st.markdown("""
Kamu adalah seorang detektif biologi! Beberapa gambar sel ditemukan di laboratorium misterius.
Tugasmu adalah mengamati ciri-cirinya, lalu menebak apakah itu **Sel Hewan**, **Sel Tumbuhan**, atau **Bakteri**.
""")

# Data sel misterius (gunakan gambar lokal)
cells = [
    {
        "id": 1,
        "image": "file-MGgkK72KyR447airHxeizf",  # file ID yang kamu upload
        "choices": ["Tidak punya dinding sel", "Ada mitokondria", "Bentuk tidak tetap"],
        "answer": "hewan"
    },
    # Tambahkan sel lain jika kamu punya gambar lainnya
]

sel = random.choice(cells)

# Tampilkan gambar
img = Image.open(f"/mnt/data/{sel['image']}")
st.image(img, caption="🔬 Perhatikan gambar sel ini!", width=500)

# Interaktif
st.subheader("Apa ciri-ciri yang kamu lihat?")
selected = st.multiselect("Pilih semua ciri yang cocok:", sel["choices"])

if selected:
    st.subheader("Menurut kamu, jenis sel ini apa?")
    guess = st.radio("Jawaban kamu:", ["hewan", "tumbuhan", "bakteri"])

    if st.button("Periksa Jawaban"):
        if guess == sel["answer"]:
            st.success("🎉 Tepat! Kamu memang detektif sel yang hebat.")
            st.balloons()
        else:
            st.error(f"❌ Belum tepat. Ini sebenarnya adalah sel **{sel['answer'].capitalize()}**.")
else:
    st.info("🧭 Pilih dulu ciri-ciri yang kamu amati dari gambar di atas.")
