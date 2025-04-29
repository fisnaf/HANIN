import streamlit as st
from PIL import Image

st.set_page_config(page_title="Eksplorasi Interaktif Sel", layout="wide")

st.title("🔬 Eksplorasi Interaktif Sel untuk SMA Kelas 11")
st.markdown("""
Aplikasi ini membantu siswa memahami struktur dan fungsi bagian-bagian sel melalui visualisasi interaktif, simulasi, dan kuis.
""")

# Tab Navigation
tab1, tab2, tab3 = st.tabs(["Struktur Sel", "Simulasi", "Kuis"])

# === TAB 1: Struktur Sel ===
with tab1:
    st.header("Struktur Sel Tumbuhan dan Hewan")

    jenis_sel = st.radio("Pilih jenis sel:", ["Sel Hewan", "Sel Tumbuhan"], horizontal=True)

    if jenis_sel == "Sel Hewan":
        image_path = "assets/cell_animal.png"
    else:
        image_path = "assets/cell_plant.png"

    img = Image.open(image_path)
    st.image(img, caption=jenis_sel, use_column_width=True)

    organel = st.selectbox("Pilih bagian sel untuk melihat penjelasannya:",
                           ["Nukleus", "Mitokondria", "Ribosom", "Retikulum Endoplasma", "Aparatus Golgi", "Lisosom", "Kloroplas", "Dinding Sel", "Membran Sel"])

    penjelasan = {
        "Nukleus": "Nukleus mengandung DNA dan mengatur aktivitas sel.",
        "Mitokondria": "Mitokondria menghasilkan energi dalam bentuk ATP melalui respirasi seluler.",
        "Ribosom": "Ribosom berperan dalam sintesis protein.",
        "Retikulum Endoplasma": "Tempat sintesis dan transportasi protein dan lipid.",
        "Aparatus Golgi": "Memodifikasi, mengemas, dan mengirim protein.",
        "Lisosom": "Mengandung enzim untuk mencerna materi yang tidak dibutuhkan.",
        "Kloroplas": "Tempat terjadinya fotosintesis (hanya ada di sel tumbuhan).",
        "Dinding Sel": "Memberi bentuk dan perlindungan pada sel tumbuhan.",
        "Membran Sel": "Mengatur keluar masuknya zat ke dalam dan luar sel."
    }

    if organel in penjelasan:
        st.success(penjelasan[organel])

# === TAB 2: Simulasi ===
with tab2:
    st.header("Simulasi Proses dalam Sel")
    st.subheader("Simulasi Osmosis")

    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Osmosis.svg/512px-Osmosis.svg.png",
             caption="Simulasi pergerakan air dari larutan hipotonik ke hipertonik melalui membran semipermeabel.",
             use_column_width=True)

    st.markdown("""
    - **Hipotonik**: Konsentrasi zat terlarut rendah, air masuk ke sel.
    - **Hipertonik**: Konsentrasi zat terlarut tinggi, air keluar dari sel.
    - **Isotonik**: Konsentrasi seimbang, tidak ada pergerakan bersih air.
    """)

# === TAB 3: Kuis ===
with tab3:
    st.header("Kuis Interaktif")
    st.markdown("Jawablah pertanyaan berikut untuk menguji pemahamanmu.")

    pertanyaan = st.radio("Organel apa yang berfungsi sebagai pusat pengendali sel?",
                          ["Mitokondria", "Nukleus", "Ribosom"])

    if st.button("Cek Jawaban"):
        if pertanyaan == "Nukleus":
            st.success("Benar! Nukleus adalah pusat pengendali sel.")
        else:
            st.error("Jawaban kurang tepat. Coba lagi!")
