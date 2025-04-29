import streamlit as st

st.set_page_config(page_title="Kuis Sel", layout="centered")
st.title("🧪 Kuis Cerdas: Tentang Sel")

score = 0

q1 = st.radio("1. Organel penghasil energi disebut...", ["Nukleus", "Mitokondria", "Kloroplas"])
if q1 == "Mitokondria":
    score += 1

q2 = st.radio("2. Organel yang hanya ada di sel tumbuhan adalah...", ["Mitokondria", "Kloroplas", "Ribosom"])
if q2 == "Kloroplas":
    score += 1

q3 = st.radio("3. Tempat sintesis protein adalah...", ["Nukleus", "Ribosom", "Lisosom"])
if q3 == "Ribosom":
    score += 1

if st.button("Lihat Hasil"):
    st.success(f"Skor kamu: {score}/3")
    if score == 3:
        st.balloons()
        st.markdown("**Luar biasa! Kamu paham banget soal sel.**")
    elif score == 2:
        st.markdown("**Hampir sempurna! Tinggal sedikit lagi.**")
    else:
        st.markdown("**Yuk pelajari lagi bagian-bagian selnya!**")
