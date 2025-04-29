import streamlit as st

st.set_page_config(page_title="Kuis Interaktif Sel", layout="centered")

st.title("Kuis Interaktif: Yuk, Uji Pengetahuanmu tentang Sel!")

# Simpan skor dan nomor soal dengan session state
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_number' not in st.session_state:
    st.session_state.question_number = 0

questions = [
    {
        "soal": "Apa fungsi utama dari mitokondria?",
        "opsi": ["Mengendalikan aktivitas sel", "Menyimpan informasi genetik", "Menghasilkan energi", "Membentuk protein"],
        "jawaban": "Menghasilkan energi"
    },
    {
        "soal": "Struktur sel apa yang menyimpan materi genetik?",
        "opsi": ["Ribosom", "Nukleus", "RE Kasar", "Membran sel"],
        "jawaban": "Nukleus"
    },
    {
        "soal": "Organel manakah yang berfungsi untuk sintesis protein?",
        "opsi": ["Mitokondria", "Lisosom", "Ribosom", "Badan Golgi"],
        "jawaban": "Ribosom"
    },
    {
        "soal": "Apa fungsi Retikulum Endoplasma Halus?",
        "opsi": ["Membentuk protein", "Membentuk lipid", "Menghasilkan energi", "Mencerna zat asing"],
        "jawaban": "Membentuk lipid"
    }
]

def tampilkan_soal(nomor):
    soal = questions[nomor]
    st.subheader(f"Soal {nomor + 1}")
    jawaban = st.radio(soal["soal"], soal["opsi"], key=nomor)
    if st.button("Kunci Jawaban", key=f"kunci_{nomor}"):
        if jawaban == soal["jawaban"]:
            st.success("Jawaban kamu benar!")
            st.session_state.score += 1
        else:
            st.error(f"Ups, jawaban yang benar: {soal['jawaban']}")
        st.session_state.question_number += 1

# Tampilkan soal satu per satu
if st.session_state.question_number < len(questions):
    tampilkan_soal(st.session_state.question_number)
else:
    st.balloons()
    st.subheader("Kuis selesai!")
    st.write(f"Skor akhir kamu: {st.session_state.score} dari {len(questions)}")
    if st.button("Ulangi kuis"):
        st.session_state.score = 0
        st.session_state.question_number = 0

st.markdown("---")
st.caption("Zafindo Edu | Belajar seru tanpa stres!")
