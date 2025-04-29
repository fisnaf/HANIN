import streamlit as st
import time

st.set_page_config(page_title="Belajar Sel - Biologi SMA", layout="wide")
st.title("Platform Belajar Interaktif - Materi Sel Biologi Kelas 11")

menu = st.sidebar.radio("Pilih Menu", ["Materi", "Kuis"])

if menu == "Materi":
    st.header("Materi Tentang Sel")
    subbab = st.selectbox("Pilih Sub-Bab", [
        "Pengertian Sel", "Sejarah Penemuan Sel", "Teori Sel", "Perbedaan Prokariotik dan Eukariotik", 
        "Struktur Sel Tumbuhan dan Hewan", "Organel-organel Sel", "Transportasi Membran", 
        "Pembelahan Sel (Mitosis & Meiosis)", "Sintesis Protein", "Diagram Struktur Sel"
    ])

    if subbab == "Pengertian Sel":
        st.write("Sel adalah unit struktural dan fungsional terkecil dari makhluk hidup.")

    elif subbab == "Sejarah Penemuan Sel":
        st.write("Robert Hooke pada tahun 1665 pertama kali mengamati sel melalui mikroskop.")

    elif subbab == "Teori Sel":
        st.write("""1. Sel adalah unit struktural semua makhluk hidup.
        2. Sel adalah unit fungsional terkecil kehidupan.
        3. Semua sel berasal dari sel yang sudah ada sebelumnya.""")

    elif subbab == "Perbedaan Prokariotik dan Eukariotik":
        st.table({
            "Ciri-ciri": ["Inti Sel", "Organel", "Contoh"],
            "Sel Prokariotik": ["Tidak ada", "Tidak kompleks", "Bakteri"],
            "Sel Eukariotik": ["Ada", "Kompleks", "Hewan, Tumbuhan"]
        })

    elif subbab == "Struktur Sel Tumbuhan dan Hewan":
        st.write("Sel tumbuhan memiliki dinding sel dan kloroplas, sedangkan sel hewan tidak.")

    elif subbab == "Organel-organel Sel":
        st.write("""- Nukleus: Mengontrol aktivitas sel
        - Mitokondria: Respirasi sel
        - Ribosom: Sintesis protein
        - RE: Transportasi zat
        - Badan Golgi: Modifikasi dan pengemasan protein
        - Lisosom: Pencernaan intraseluler""")

    elif subbab == "Transportasi Membran":
        st.write("Meliputi difusi, osmosis, transport aktif, endositosis, dan eksositosis.")

    elif subbab == "Pembelahan Sel (Mitosis & Meiosis)":
        st.write("""- Mitosis: pertumbuhan & perbaikan
        - Meiosis: pembentukan gamet dengan pengurangan jumlah kromosom.""")

    elif subbab == "Sintesis Protein":
        st.write("Transkripsi (DNA → mRNA) lalu Translasi (mRNA → Protein di ribosom).")

elif menu == "Kuis":
    st.header("Kuis Interaktif Biologi - Materi Sel")
    level = st.selectbox("Pilih Level", ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5"])

    def tampilkan_kuis(soal_list):
        score = 0
        jawaban_user = [None] * len(soal_list)

        for i, (soal, benar, pilihan) in enumerate(soal_list):
            st.markdown(f"**{i+1}. {soal}**")
            if jawaban_user[i] is None:
                if st.button(f"Pilih jawaban untuk Soal {i+1}", key=f"btn_{i}"):
                    jawaban_user[i] = st.radio("Pilih jawaban:", pilihan, key=f"radio_{i}")
            else:
                jawaban_user[i] = st.radio("Pilih jawaban:", pilihan, key=f"radio_{i}", index=pilihan.index(jawaban_user[i]))

        if st.button("Submit Jawaban"):
            for i, (soal, benar, pilihan) in enumerate(soal_list):
                if jawaban_user[i] == benar:
                    score += 1
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
        "Level 2": [
            ("Apa fungsi dari badan golgi?", "Pengemasan dan modifikasi protein", ["Sintesis protein", "Modifikasi dan pengemasan protein", "Transportasi zat", "Pencernaan"]),
            ("Fungsi kloroplas pada sel tumbuhan adalah?", "Fotosintesis", ["Respirasi", "Pencernaan", "Fotosintesis", "Transkripsi"]),
            ("Apa yang dimaksud dengan difusi?", "Perpindahan zat dari konsentrasi tinggi ke rendah", ["Perpindahan zat dari konsentrasi tinggi ke rendah", "Penggunaan energi dalam perpindahan zat", "Perpindahan air melalui membran", "Perpindahan zat dari konsentrasi rendah ke tinggi"]),
            ("Pada tahap mitosis, di mana kromosom berjejer di tengah sel?", "Metafase", ["Profase", "Metafase", "Anafase", "Telofase"]),
            ("Organisme yang memiliki sel prokariotik adalah...", "Bakteri", ["Manusia", "Bakteri", "Hewan", "Tumbuhan"]),
        ],
        "Level 3": [
            ("Apa yang terjadi pada sel selama fase G1 dalam siklus sel?", "Pertumbuhan sel", ["Sintesis protein", "Pertumbuhan sel", "Pembelahan sel", "Replikasi DNA"]),
            ("Apa yang dimaksud dengan osmosis?", "Perpindahan air melalui membran semipermeabel", ["Perpindahan air melalui membran semipermeabel", "Transportasi zat menggunakan energi", "Perpindahan zat melalui membran", "Transportasi air dengan pompa"]),
            ("Apa yang terjadi pada tahap anafase mitosis?", "Pemecahan kromatid menjadi kromosom", ["Kromosom berjejer", "Kromosom saling berpisah", "Kromatid saling berpisah", "Pembentukan dua inti sel"]),
            ("Organel yang berperan dalam sintesis protein adalah...", "Ribosom", ["Mitokondria", "Ribosom", "Lisosom", "Badan Golgi"]),
            ("Sel kelamin memiliki...", "Setengah jumlah kromosom", ["Jumlah kromosom penuh", "Setengah jumlah kromosom", "Jumlah kromosom yang tidak tetap", "Kromosom X dan Y"]),
        ],
        "Level 4": [
            ("Proses pembelahan sel yang menghasilkan dua sel anak identik adalah...", "Mitosis", ["Mitosis", "Meiosis", "Amitosis", "Fase G1"]),
            ("Reaksi yang menghasilkan ATP dalam mitokondria disebut...", "Respirasi seluler", ["Fotosintesis", "Respirasi seluler", "Reaksi Kimia", "Transkripsi"]),
            ("Apa yang terjadi selama fase G2 pada siklus sel?", "Pemeriksaan dan perbaikan DNA", ["Replikasi DNA", "Pemeriksaan dan perbaikan DNA", "Pembelahan inti", "Penyusunan protein"]),
            ("Apa perbedaan utama antara mitosis dan meiosis?", "Meiosis menghasilkan sel dengan setengah jumlah kromosom", ["Mitosis menghasilkan 2 sel identik", "Meiosis menghasilkan 4 sel identik", "Mitosis menghasilkan sel dengan setengah kromosom", "Meiosis menghasilkan sel dengan setengah jumlah kromosom"]),
            ("Apa yang dimaksud dengan teori sel?", "Sel adalah unit dasar kehidupan", ["Sel adalah unit dasar kehidupan", "Sel hanya ditemukan pada tumbuhan", "Sel tidak memiliki struktur", "Semua sel berasal dari sel lain"]),
        ],
        "Level 5": [
            ("Apa yang terjadi selama transkripsi?", "DNA diubah menjadi mRNA", ["DNA diubah menjadi mRNA", "mRNA diubah menjadi protein", "DNA berpisah", "Protein menjadi ribosom"]),
            ("Bagaimana peran mitokondria dalam sel?", "Menyediakan energi dalam bentuk ATP", ["Menyediakan energi dalam bentuk ATP", "Sintesis protein", "Penyimpanan materi genetik", "Modifikasi protein"]),
            ("Sel tumbuhan berbeda dari sel hewan karena adanya...", "Dinding sel dan kloroplas", ["Lisosom", "Flagela", "Dinding sel dan kloroplas", "Nukleus"]),
            ("Organel yang terlibat dalam pembentukan protein adalah...", "RE Kasar dan Ribosom", ["RE Kasar dan Ribosom", "Lisosom", "Badan Golgi", "Nukleus"]),
            ("Apa yang dimaksud dengan transport aktif?", "Perpindahan zat melawan gradien konsentrasi", ["Perpindahan air", "Perpindahan zat melawan gradien konsentrasi", "Perpindahan zat dengan konsentrasi tinggi", "Transport pasif"]),
        ]
    }

    if level in soal_per_level:
        tampilkan_kuis(soal_per_level[level])
    else:
        st.warning("Level ini belum tersedia. Tunggu update berikutnya.")
