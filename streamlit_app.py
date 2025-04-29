import streamlit as st

st.set_page_config(page_title="Simulasi Posisi Organel", layout="centered")
st.title("🎯 Letakkan Organel ke Tempat yang Benar (Simulasi)")

organel_lokasi = {
    "Nukleus": st.selectbox("Dimana letak Nukleus?", ["Di tengah", "Di pinggir", "Tidak ada"]),
    "Kloroplas": st.selectbox("Dimana letak Kloroplas?", ["Dekat dinding sel", "Di tengah", "Tidak ada"]),
    "Ribosom": st.selectbox("Dimana letak Ribosom?", ["Menempel RE", "Di dalam nukleus", "Tidak ada"])
}

if st.button("Periksa Jawaban"):
    benar = 0
    if organel_lokasi["Nukleus"] == "Di tengah":
        benar += 1
    if organel_lokasi["Kloroplas"] == "Dekat dinding sel":
        benar += 1
    if organel_lokasi["Ribosom"] == "Menempel RE":
        benar += 1

    st.success(f"Kamu benar: {benar}/3")
