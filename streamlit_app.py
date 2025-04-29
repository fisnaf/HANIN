import streamlit as st

# Judul aplikasi
st.title("Pembelajaran Materi Sel untuk Kelas 11 SMA")

# Penjelasan materi
st.header("Apa itu Sel?")
st.write("""
Sel adalah unit terkecil dari makhluk hidup yang menjadi penyusun semua organisme. 
Sel memiliki berbagai bagian penting seperti membran sel, sitoplasma, dan inti sel yang memiliki fungsi masing-masing.
""")

# Menampilkan gambar sel (gunakan gambar lokal atau URL)
st.image("https://upload.wikimedia.org/wikipedia/commons/3/3a/Animal_cell_structure_en.svg", caption="Struktur Sel Hewan", use_column_width=True)

# Penjelasan bagian-bagian sel
st.subheader("Bagian-Bagian Sel dan Fungsinya")
bagian_sel = {
    "Membran Sel": "Melindungi sel dan mengatur keluar masuk zat.",
    "Sitoplasma": "Tempat berlangsungnya reaksi kimia dalam sel.",
    "Inti Sel (Nukleus)": "Mengatur aktivitas sel dan menyimpan informasi genetik.",
    "Mitokondria": "Pembangkit energi sel.",
    "Ribosom": "Tempat sintesis protein."
}
for bagian, fungsi in bagian_sel.items():
    st.markdown(f"**{bagian}**: {fungsi}")

# Quiz interaktif sederhana
st.header("Quiz Singkat")
jawaban = st.radio(
    "Bagian sel manakah yang berfungsi sebagai pembangkit energi?",
    ("Membran Sel", "Mitokondria", "Ribosom", "Inti Sel")
)

if st.button("Cek Jawaban"):
    if jawaban == "Mitokondria":
        st.success("Benar! Mitokondria adalah pembangkit energi sel.")
    else:
        st.error("Salah. Coba lagi ya!")

# Footer
st.write("Semoga pembelajaran ini membantu kamu memahami materi sel dengan lebih mudah!")

