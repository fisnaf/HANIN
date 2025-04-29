import streamlit as st

st.set_page_config(page_title="Tur Virtual ke Dalam Sel", layout="centered")

st.title("Tur Virtual ke Dalam Sel")
st.subheader("Selamat datang di dunia mikroskopis!")

st.image("https://upload.wikimedia.org/wikipedia/commons/0/05/Animal_Cell.svg", 
         caption="Klik nama organel di bawah untuk memulai tur!", use_column_width=True)

organel = st.selectbox("Pilih organel yang ingin dikunjungi:", [
    "Nukleus", "Mitokondria", "Ribosom", "Retikulum Endoplasma", 
    "Badan Golgi", "Lisosom", "Membran Sel", "Sitoplasma"
])

if organel == "Nukleus":
    st.markdown("**Nukleus** adalah pusat kendali sel. Ia menyimpan DNA dan mengatur aktivitas sel.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Cell_Nucleus_diagram_en.svg", width=300)
    st.success("Fun fact: Nukleus itu seperti 'otak'-nya sel!")
elif organel == "Mitokondria":
    st.markdown("**Mitokondria** menghasilkan energi untuk sel. Sering disebut 'pembangkit tenaga' sel.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3e/Mitochondrion_structure.svg", width=300)
    st.info("Kata kuncinya: ATP!")
elif organel == "Ribosom":
    st.markdown("**Ribosom** adalah tempat sintesis protein. Bisa ditemukan bebas atau menempel di RE kasar.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/03/Ribosome_mRNA_translation_en.svg", width=300)
    st.warning("Tanpa protein, sel nggak bisa bekerja!")
# ... lanjutkan untuk organel lainnya

st.markdown("---")
st.caption("Zafindo Edu | Belajar biologi bisa seru juga, kan?")
