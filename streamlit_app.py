import streamlit as st
import random

# Judul aplikasi
st.title("Pembelajaran Biologi SMA Kelas 11: Sel")

# Sidebar menu
menu = st.sidebar.selectbox("Pilih Menu", ["Materi Sel", "Kuis", "Game"])

# Menu 1: Materi Sel
if menu == "Materi Sel":
    st.header("Materi: Struktur dan Fungsi Sel")
    st.subheader("1. Pengantar Sel")
    st.write("""
        Sel adalah unit struktural dan fungsional terkecil dari makhluk hidup. Terdapat dua jenis utama sel:
        - Sel Prokariotik (contoh: bakteri)
        - Sel Eukariotik (contoh: sel hewan dan tumbuhan)
    """)

    st.subheader("2. Organel-Organel dalam Sel")
    st.markdown("**Nukleus**: Mengatur aktivitas sel dan menyimpan DNA.")
    st.markdown("**Mitokondria**: Tempat respirasi sel untuk menghasilkan energi.")
    st.markdown("**Ribosom**: Sintesis protein.")
    st.markdown("**Retikulum Endoplasma**: Transportasi dalam sel.")
    st.markdown("**Aparatus Golgi**: Pengemasan dan pengiriman protein.")

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
