import streamlit as st

st.set_page_config(page_title="Tur Virtual ke Dalam Sel", layout="centered")

st.title("Tur Virtual ke Dalam Sel")
st.subheader("Selamat datang di dunia mikroskopis!")

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Animal_Cell.png/800px-Animal_Cell.png",
    caption="Klik nama organel di bawah untuk memulai tur!",
    use_container_width=True
)

organel = st.selectbox("Pilih organel yang ingin dikunjungi:", [
    "Nukleus", "Mitokondria", "Ribosom", "Retikulum Endoplasma", 
    "Badan Golgi", "Lisosom", "Membran Sel", "Sitoplasma"
])

if organel == "Nukleus":
    st.markdown("**Nukleus** adalah pusat kendali sel. Ia menyimpan DNA dan mengatur aktivitas sel.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Cell_Nucleus_diagram_en.svg/512px-Cell_Nucleus_diagram_en.svg.png", width=300)
    st.success("Fun fact: Nukleus itu seperti 'otak'-nya sel!")
elif organel == "Mitokondria":
    st.markdown("**Mitokondria** menghasilkan energi untuk sel. Sering disebut 'pembangkit tenaga' sel.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Mitochondrion_structure.svg/512px-Mitochondrion_structure.svg.png", width=300)
    st.info("Kata kuncinya: ATP!")
elif organel == "Ribosom":
    st.markdown("**Ribosom** adalah tempat sintesis protein. Bisa ditemukan bebas atau menempel di RE kasar.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Ribosome_mRNA_translation_en.svg/512px-Ribosome_mRNA_translation_en.svg.png", width=300)
    st.warning("Tanpa protein, sel nggak bisa bekerja!")
elif organel == "Retikulum Endoplasma":
    st.markdown("**Retikulum Endoplasma (RE)** adalah jalur transportasi dalam sel.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Endoplasmic_reticulum.svg/512px-Endoplasmic_reticulum.svg.png", width=300)
    st.info("Ada dua jenis RE: kasar & halus!")
elif organel == "Badan Golgi":
    st.markdown("**Badan Golgi** berfungsi untuk memproses dan mengemas protein.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Golgi_apparatus_diagram_en.svg/512px-Golgi_apparatus_diagram_en.svg.png", width=300)
    st.success("Pabrik pengepakan sel!")
elif organel == "Lisosom":
    st.markdown("**Lisosom** adalah sistem pencernaan mini dalam sel.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Lysosome.svg/512px-Lysosome.svg.png", width=300)
    st.warning("Seperti tukang bersih-bersih!")
elif organel == "Membran Sel":
    st.markdown("**Membran Sel** mengatur apa yang boleh masuk dan keluar dari sel.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Cell_membrane_detailed_diagram_en.svg/512px-Cell_membrane_detailed_diagram_en.svg.png", width=300)
    st.info("Seperti satpam di pintu gerbang!")
elif organel == "Sitoplasma":
    st.markdown("**Sitoplasma** adalah cairan di dalam sel tempat organel mengambang.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Cell_organelles_structure.svg/512px-Cell_organelles_structure.svg.png", width=300)
    st.success("Tempat segala aktivitas kimia terjadi!")

st.markdown("---")
st.caption("Zafindo Edu | Belajar biologi bisa seru juga, kan?")
