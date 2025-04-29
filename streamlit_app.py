import streamlit as st
import random

# Tambahkan CSS untuk tema latar belakang
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1581090700227-1e8e7b47f1ed');
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }
    .css-18e3th9, .css-1d391kg, .css-1kyxreq, .css-ffhzg2 {
        background-color: rgba(0, 0, 0, 0.6) !important;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul aplikasi
st.title("Pembelajaran Biologi SMA Kelas 11: Sel")

# Sidebar menu
menu = st.sidebar.selectbox("Pilih Menu", ["Materi Sel", "Kuis", "Game"])

# Menu 1: Materi Sel
if menu == "Materi Sel":
    st.header("Materi: Struktur dan Fungsi Sel")

    st.subheader("1. Pengantar Sel")
    st.write("""
        Sel merupakan unit struktural, fungsional, dan biologis terkecil dari semua makhluk hidup. Semua makhluk hidup tersusun atas satu atau lebih sel. Sel mampu melakukan semua fungsi kehidupan seperti metabolisme, pertumbuhan, dan reproduksi.

        Terdapat dua jenis utama sel:
        - **Sel Prokariotik**: Merupakan sel yang tidak memiliki membran inti sel. Materi genetiknya tersebar di sitoplasma. Contoh organisme prokariotik adalah bakteri dan archaea.
        - **Sel Eukariotik**: Merupakan sel yang memiliki membran inti. Materi genetiknya tersimpan dalam inti sel (nukleus). Contoh sel eukariotik adalah sel tumbuhan, sel hewan, jamur, dan protista.
    """)

    st.subheader("2. Organel-Organel dalam Sel")
    st.markdown("**Nukleus**: Nukleus atau inti sel adalah pusat pengendali sel yang menyimpan materi genetik (DNA). Nukleus dilapisi oleh membran inti dan berperan dalam mengatur pertumbuhan, metabolisme, dan reproduksi sel.")
    st.markdown("**Mitokondria**: Merupakan organel yang menghasilkan energi melalui proses respirasi seluler. Mitokondria sering disebut sebagai 'pembangkit tenaga sel'.")
    st.markdown("**Ribosom**: Organel kecil yang tersebar di sitoplasma atau menempel pada retikulum endoplasma. Fungsinya adalah untuk menyintesis protein yang dibutuhkan oleh sel.")
    st.markdown("**Retikulum Endoplasma (RE)**: Terdiri dari dua jenis, yaitu RE kasar (mengandung ribosom) dan RE halus (tidak mengandung ribosom). RE berfungsi dalam transportasi zat dan sintesis lipid serta protein.")
    st.markdown("**Aparatus Golgi**: Berfungsi untuk memodifikasi, mengemas, dan mengirim protein serta lipid ke bagian lain dari sel atau ke luar sel.")
    st.markdown("**Lisosom**: Organel yang berisi enzim pencerna. Fungsinya adalah untuk mencerna partikel asing dan menghancurkan organel yang sudah rusak (autofagi). Biasanya ditemukan pada sel hewan.")
    st.markdown("**Kloroplas**: Organel yang hanya terdapat pada sel tumbuhan dan alga. Mengandung klorofil dan berperan penting dalam proses fotosintesis.")
    st.markdown("**Vakuola**: Rongga yang berisi cairan. Pada sel tumbuhan, vakuola berukuran besar dan berfungsi untuk menyimpan cadangan makanan, air, dan produk sisa metabolisme.")
    st.markdown("**Membran Sel**: Struktur semi-permeabel yang mengatur keluar-masuknya zat dari dan ke dalam sel.")
    st.markdown("**Dinding Sel**: Struktur keras yang melindungi dan memberi bentuk sel. Hanya dimiliki oleh sel tumbuhan dan beberapa mikroorganisme seperti jamur dan bakteri.")

# Menu 2: Kuis
elif menu == "Kuis":
    st.header("Kuis: Pemahaman tentang Sel")
    score = 0

    q1 = st.radio("1. Apa fungsi utama mitokondria?", [
        "Sintesis protein", "Respirasi sel dan produksi energi", "Pengemasan protein"])
    if q1 == "Respirasi sel dan produksi energi":
        score += 1

    q2 = st.radio("2. Organel apa yang menyimpan materi genetik?", [
        "Ribosom", "Nukleus", "Lisosom"])
    if q2 == "Nukleus":
        score += 1

    q3 = st.radio("3. Sel prokariotik tidak memiliki...?", [
        "Sitoplasma", "Membran sel", "Nukleus"])
    if q3 == "Nukleus":
        score += 1

    if st.button("Lihat Skor"):
        st.success(f"Skor kamu: {score} dari 3")

# Menu 3: Game
elif menu == "Game":
    st.header("Game: Tebak Organel")

    soal_game = [
        {
            "deskripsi": "Tempat berlangsungnya sintesis protein.",
            "jawaban": "Ribosom",
            "opsi": ["Mitokondria", "Ribosom", "Nukleus"]
        },
        {
            "deskripsi": "Organel penghasil energi melalui proses respirasi sel.",
            "jawaban": "Mitokondria",
            "opsi": ["Mitokondria", "Lisosom", "Aparatus Golgi"]
        },
        {
            "deskripsi": "Tempat penyimpanan materi genetik dan pusat kontrol sel.",
            "jawaban": "Nukleus",
            "opsi": ["Retikulum Endoplasma", "Nukleus", "Ribosom"]
        }
    ]

    score_game = 0
    for i, soal in enumerate(soal_game):
        st.subheader(f"Soal {i+1}")
        jawaban = st.radio(soal["deskripsi"], soal["opsi"], key=i)
        if st.button(f"Cek Jawaban Soal {i+1}"):
            if jawaban == soal["jawaban"]:
                st.success("Benar!")
                score_game += 1
            else:
                st.error(f"Salah. Jawaban yang benar adalah: {soal['jawaban']}")

    if st.button("Lihat Skor Akhir Game"):
        st.info(f"Skor akhir kamu di game ini: {score_game} dari {len(soal_game)}")
