import streamlit as st

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
    st.write("Pilih organel yang sesuai dengan deskripsi berikut:")

    deskripsi = "Tempat berlangsungnya sintesis protein."
    jawaban = st.selectbox("Organel apakah ini?", ["Mitokondria", "Ribosom", "Nukleus"])
    if st.button("Cek Jawaban"):
        if jawaban == "Ribosom":
            st.success("Benar! Ribosom berperan dalam sintesis protein.")
        else:
            st.error("Salah. Coba lagi!")
