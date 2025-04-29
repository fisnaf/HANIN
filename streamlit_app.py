import streamlit as st

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
        st.write("Sel adalah unit struktural dan fungsional terkecil dari makhluk hidup.")

    elif subbab == "Sejarah Penemuan Sel":
        st.subheader("Sejarah Penemuan Sel")
        st.write("Robert Hooke pada tahun 1665 pertama kali mengamati sel melalui mikroskop.")

    elif subbab == "Teori Sel":
        st.subheader("Teori Sel")
        st.write("""1. Sel adalah unit struktural semua makhluk hidup.
2. Sel adalah unit fungsional terkecil kehidupan.
3. Semua sel berasal dari sel yang sudah ada sebelumnya.""")

    elif subbab == "Perbedaan Prokariotik dan Eukariotik":
        st.subheader("Perbedaan Prokariotik dan Eukariotik")
        st.table({
            "Ciri-ciri": ["Inti Sel", "Organel", "Contoh"],
            "Sel Prokariotik": ["Tidak ada", "Tidak kompleks", "Bakteri"],
            "Sel Eukariotik": ["Ada", "Kompleks", "Hewan, Tumbuhan"]
        })

    elif subbab == "Struktur Sel Tumbuhan dan Hewan":
        st.subheader("Struktur Sel Tumbuhan dan Hewan")
        st.write("Sel tumbuhan memiliki dinding sel dan kloroplas, sedangkan sel hewan tidak.")

    elif subbab == "Organel-organel Sel":
        st.subheader("Organel-organel Sel dan Fungsinya")
        st.write("""- Nukleus: Mengontrol aktivitas sel
- Mitokondria: Respirasi sel
- Ribosom: Sintesis protein
- RE: Transportasi zat
- Badan Golgi: Modifikasi dan pengemasan protein
- Lisosom: Pencernaan intraseluler""")

    elif subbab == "Transportasi Membran":
        st.subheader("Transportasi Membran")
        st.write("Meliputi difusi, osmosis, transport aktif, endositosis, dan eksositosis.")

    elif subbab == "Pembelahan Sel (Mitosis & Meiosis)":
        st.subheader("Pembelahan Sel")
        st.write("""- Mitosis: pertumbuhan & perbaikan
- Meiosis: pembentukan gamet dengan pengurangan jumlah kromosom.""")

    elif subbab == "Sintesis Protein":
        st.subheader("Sintesis Protein")
        st.write("Transkripsi (DNA → mRNA) lalu Translasi (mRNA → Protein di ribosom).")

elif menu == "Kuis":
    st.header("Kuis Interaktif Biologi - Materi Sel")
    level = st.selectbox("Pilih Level", ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5"])

    def tampilkan_kuis(soal_list):
        score = 0
        for i, (soal, benar, pilihan) in enumerate(soal_list):
            st.markdown(f"**{i+1}. {soal}**")
            jawaban = st.radio("Jawaban kamu:", pilihan, key=i)
            if jawaban == benar:
                score += 1

        if st.button("Submit Jawaban"):
            st.success(f"Skor kamu: {score}/{len(soal_list)}")
            if score >= 7:
                st.balloons()
                st.info("Selamat! Kamu bisa lanjut ke level berikutnya.")
            else:
                st.warning("Kamu belum lulus. Coba ulangi lagi ya!")

    soal_per_level = {
        "Level 1": [
            ("Apa unit terkecil kehidupan?", "Sel", ["Jaringan", "Sel", "Organ", "Sistem organ"]),
            ("Siapa penemu istilah 'sel'?", "Robert Hooke", ["Schwann", "Schleiden", "Virchow", "Robert Hooke"]),
            ("Sel prokariotik tidak memiliki...", "Inti sejati", ["Sitoplasma", "Inti sejati", "DNA", "Membran sel"]),
            ("Organel pusat kontrol sel adalah...", "Nukleus", ["Nukleus", "Lisosom", "RE", "Mitokondria"]),
            ("Sel tumbuhan memiliki...", "Dinding sel", ["Sentriol", "Lisosom", "Dinding sel", "Flagela"]),
            ("Transkripsi terjadi di...", "Inti sel", ["Sitoplasma", "RE", "Inti sel", "Ribosom"]),
            ("RE kasar berperan dalam...", "Sintesis protein", ["Respirasi", "Sintesis protein", "Pencernaan", "Duplikasi DNA"]),
            ("Meiosis terjadi pada...", "Sel kelamin", ["Sel tubuh", "Hati", "Otot", "Sel kelamin"]),
            ("Struktur penghasil energi sel adalah...", "Mitokondria", ["Nukleus", "Lisosom", "Mitokondria", "RE"]),
            ("Fungsi ribosom adalah...", "Membuat protein", ["Menghasilkan energi", "Mencerna zat", "Membuat protein", "Transport zat"]),
        ],
        # Level 2-5 bisa ditambahkan di sini nanti
    }

    if level in soal_per_level:
        tampilkan_kuis(soal_per_level[level])
    else:
        st.warning("Level ini belum tersedia. Tunggu update berikutnya.")
