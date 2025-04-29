import streamlit as st

st.set_page_config(page_title="Tur Virtual Sel", layout="wide")
st.title("🔍 Jelajahi Bagian-Bagian Sel")

organel_info = {
    "Nukleus": "Pusat pengendali sel, menyimpan DNA.",
    "Mitokondria": "Tempat produksi energi sel (ATP).",
    "Ribosom": "Tempat sintesis protein.",
    "Retikulum Endoplasma": "Tempat pengangkutan dan produksi protein/lipid.",
    "Kloroplas": "Tempat fotosintesis (pada tumbuhan).",
    "Vakuola": "Tempat penyimpanan zat.",
    "Dinding Sel": "Melindungi dan memberi bentuk (sel tumbuhan)."
}

selected = st.selectbox("Pilih bagian organel untuk dijelajahi:", list(organel_info.keys()))
st.image(f"https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Cell_structure.svg/800px-Cell_structure.svg.png", caption="Struktur Sel", use_container_width=True)
st.markdown(f"### {selected}")
st.info(organel_info[selected])
