import streamlit as st

st.set_page_config(page_title="Sintesis Protein", layout="centered")
st.title("🧬 Simulasi Sintesis Protein")

steps = [
    "1. DNA membuka gulungannya di inti sel.",
    "2. mRNA disalin dari DNA (transkripsi).",
    "3. mRNA keluar menuju ribosom.",
    "4. Ribosom membaca mRNA dan mulai menyusun protein (translasi).",
    "5. Protein dikirim melalui Retikulum Endoplasma dan dikemas oleh Badan Golgi."
]

step = st.slider("Langkah ke-", 1, len(steps), 1)
st.info(steps[step-1])

if st.button("Lihat Semua Langkah"):
    for i in steps:
        st.markdown(f"- {i}")
