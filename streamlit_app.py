st.title("Eksplorasi Interaktif Sel")

tab1, tab2, tab3 = st.tabs(["Struktur Sel", "Simulasi", "Kuis"])

with tab1:
    jenis = st.radio("Pilih jenis sel:", ["Sel Hewan", "Sel Tumbuhan"])
    st.image("assets/cell_animal.png" if jenis == "Sel Hewan" else "assets/cell_plant.png", caption="Klik bagian sel untuk info")

    # Logika klik bisa ditambah untuk deteksi area gambar
    selected_organel = st.selectbox("Pilih organel untuk info:", ["Nukleus", "Mitokondria", "Ribosom"])
    st.info(f"{selected_organel}: Penjelasan fungsi organel ini...")

with tab2:
    st.subheader("Simulasi Osmosis")
    st.image("assets/osmosis_demo.gif")
    st.write("Air bergerak dari larutan hipotonik ke hipertonik...")

with tab3:
    st.subheader("Kuis Cepat")
    q = st.radio("Organel apa yang berfungsi sebagai pusat kontrol sel?", ["Mitokondria", "Nukleus", "Ribosom"])
    if st.button("Cek Jawaban"):
        st.success("Benar!") if q == "Nukleus" else st.error("Coba lagi.")
