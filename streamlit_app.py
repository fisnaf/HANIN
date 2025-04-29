import streamlit as st

# Halaman utama
st.set_page_config(page_title="Belajar Sel - Biologi SMA", layout="wide")
st.title("Platform Belajar Interaktif - Materi Sel Biologi Kelas 11")

menu = st.sidebar.radio("Pilih Menu", ["Materi", "Kuis"])

if menu == "Materi":
    st.header("Materi Tentang Sel")
    subbab = st.selectbox("Pilih Sub-Bab", [
        "Pengertian Sel",
        "Sejarah Penemuan Sel",
        "Teori Sel",
        "Perbedaan Prokariotik dan Eukariotik",
        "Struktur Sel Tumbuhan dan Hewan",
        "Organel-organel Sel",
        "Transportasi Membran",
        "Pembelahan Sel (Mitosis & Meiosis)",
        "Sintesis Protein"
    ])

    if subbab == "Pengertian Sel":
        st.subheader("Pengertian Sel")
        st.write("""
        Sel adalah unit struktural dan fungsional terkecil dari makhluk hidup.
        Semua makhluk hidup terdiri atas satu atau lebih sel.
        """)

    elif subbab == "Sejarah Penemuan Sel":
        st.subheader("Sejarah Penemuan Sel")
        st.write("""
        Konsep sel pertama kali ditemukan oleh Robert Hooke pada tahun 1665.
        Ia mengamati irisan tipis gabus dengan mikroskop dan melihat struktur kotak-kotak.
        """)

    elif subbab == "Teori Sel":
        st.subheader("Teori Sel")
        st.write("""
        1. Sel adalah unit struktural semua makhluk hidup.
        2. Sel adalah unit fungsional terkecil kehidupan.
        3. Semua sel berasal dari sel yang sudah ada sebelumnya.
        """)

    elif subbab == "Perbedaan Prokariotik dan Eukariotik":
        st.subheader("Perbedaan Prokariotik dan Eukariotik")
        st.write("""
        | Ciri-ciri | Sel Prokariotik | Sel Eukariotik |
        |-----------|------------------|------------------|
        | Inti Sel  | Tidak ada        | Ada              |
        | Organel   | Tidak kompleks   | Kompleks         |
        | Contoh    | Bakteri          | Hewan, Tumbuhan  |
        """)

    elif subbab == "Struktur Sel Tumbuhan dan Hewan":
        st.subheader("Struktur Sel Tumbuhan dan Hewan")
        st.write("""
        Sel tumbuhan memiliki dinding sel dan kloroplas, sedangkan sel hewan tidak.
        Sel hewan memiliki sentriol yang tidak dimiliki sel tumbuhan.
        """)

    elif subbab == "Organel-organel Sel":
        st.subheader("Organel-organel Sel dan Fungsinya")
        st.write("""
        - Nukleus: Mengontrol aktivitas sel
        - Mitokondria: Respirasi sel
        - Ribosom: Sintesis protein
        - Retikulum endoplasma: Transportasi zat
        - Badan Golgi: Modifikasi dan pengemasan protein
        - Lisosom: Pencernaan intraseluler
        """)

    elif subbab == "Transportasi Membran":
        st.subheader("Transportasi Membran")
        st.write("""
        Transportasi membran meliputi difusi, osmosis, transport aktif, dan endositosis.
        """)

    elif subbab == "Pembelahan Sel (Mitosis & Meiosis)":
        st.subheader("Pembelahan Sel")
        st.write("""
        - Mitosis: untuk pertumbuhan dan regenerasi
        - Meiosis: untuk pembentukan gamet
        """)

    elif subbab == "Sintesis Protein":
        st.subheader("Sintesis Protein")
        st.write("""
        Proses dimulai dari transkripsi (DNA ke mRNA) lalu translasi (mRNA ke protein).
        """)

elif menu == "Kuis":
    st.header("Kuis Interaktif Biologi - Materi Sel")
    st.write("Silakan pilih level untuk memulai kuis.")
    # Placeholder untuk level kuis
    level = st.selectbox("Pilih Level", ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5"])

    st.info("Fitur kuis akan segera ditambahkan dengan total 50 soal dan penilaian per level.")
