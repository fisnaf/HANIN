import streamlit as st

st.set_page_config(page_title="Escape Room: Jelajahi Dunia Sel", layout="wide")

st.title("🧬 Escape Room: Jelajahi Dunia Sel")
st.markdown("""
Kamu terjebak di dalam sebuah sel! Untuk keluar, kamu harus memecahkan teka-teki yang berkaitan dengan struktur dan fungsi organel.
Setiap jawaban benar akan membawamu lebih dekat ke pintu keluar!
""")

# Level 1: Pintu Nukleus
st.header("Level 1: Pintu Nukleus")
q1 = st.text_input("Aku adalah pusat pengendali semua aktivitas dalam sel. Siapakah aku?").strip().lower()
if q1:
    if "nukleus" in q1:
        st.success("Benar! Kamu telah membuka pintu pertama dan memasuki sitoplasma...")

        # Level 2: Mitokondria
        st.header("Level 2: Mitokondria")
        q2 = st.text_input("Aku menghasilkan energi untuk sel, bagaikan pembangkit tenaga. Siapakah aku?").strip().lower()
        if q2:
            if "mitokondria" in q2:
                st.success("Bagus! Energi kamu cukup untuk melanjutkan ke organel berikutnya...")

                # Level 3: Ribosom
                st.header("Level 3: Ribosom")
                q3 = st.text_input("Aku membantu membuat protein. Aku bisa bebas atau menempel di RE kasar. Siapakah aku?").strip().lower()
                if q3:
                    if "ribosom" in q3:
                        st.success("Hebat! Protein sudah cukup untuk bertahan hidup...")

                        # Level 4: Gerbang Membran Sel
                        st.header("Level 4: Gerbang Membran Sel")
                        q4 = st.text_input("Aku menjaga keluar masuknya zat. Aku adalah pelindung utama sel. Siapakah aku?").strip().lower()
                        if q4:
                            if "membran sel" in q4 or "membran" in q4:
                                st.balloons()
                                st.success("Selamat! Kamu berhasil keluar dari sel! Sekarang kamu bebas!")
                            else:
                                st.error("Jawaban belum tepat. Coba lagi!")
                    else:
                        st.error("Jawaban kurang tepat. Coba lagi!")
            else:
                st.error("Bukan itu organelnya. Coba lagi!")
    else:
        st.error("Masih salah. Coba pikirkan siapa yang mengatur sel!")
else:
    st.info("Masukkan jawabanmu untuk mulai permainan.")
