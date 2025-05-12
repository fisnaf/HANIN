import streamlit as st
import base64
import requests
from streamlit_lottie import st_lottie

# Function to calculate Chemical Oxygen Demand (COD)
def calculate_cod(vb, vc, nfas, vsample):
    if vsample == 0:
        return None
    cod_value = ((vb - vc) * nfas * 8000) / vsample
    return cod_value

# Fungsi untuk memproses lottie url
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to determine environmental quality class
def determine_quality_class(cod_value):
    if cod_value >= 0 and cod_value <= 10:
        return "memenuhi Baku Mutu Lingkungan (BML) dalam Kelas 1 berdasarkan PP No.22 Tahun 2021. Kelas 1: air baku air minum."
    elif cod_value > 10 and cod_value <= 25:
        return "memenuhi BML dalam Kelas 2: rekreasi air, budidaya ikan, peternakan, irigasi."
    elif cod_value > 25 and cod_value <= 40:
        return "memenuhi BML dalam Kelas 3: budidaya ikan, peternakan, irigasi."
    elif cod_value > 40 and cod_value <= 80:
        return "memenuhi BML dalam Kelas 4: untuk irigasi tanaman."
    else:
        return "tidak memenuhi Baku Mutu Lingkungan (BML) dalam PP No.22 Tahun 2021."

# Fungsi untuk konversi gambar ke base64
def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Fungsi utama
def main():
    # Menampilkan logo di sidebar
    img_path = "img/icon_aka.png"
    try:
        img_base64 = img_to_base64(img_path)
        st.sidebar.markdown(
            f'<img src="data:image/png;base64,{img_base64}" style="width: 100%; height: auto;">',
            unsafe_allow_html=True,
        )
    except:
        st.sidebar.warning("Logo tidak ditemukan.")

    # Sidebar menu
    st.sidebar.title('Main Menu')
    select_box = st.sidebar.selectbox('', 
        ('Pengantar', 'Cara Kerja', 'Kalkulator COD', 'Our Group')
    )

    # Animasi Lottie
    lottie_url = "https://lottie.host/763d8378-248d-49ea-be0a-e2f54c16261d/JhnKfnqKfV.json"
    lottie_json = load_lottie_url(lottie_url)

    if select_box == 'Pengantar':
        st.markdown('# <div style="text-align: center;"> Chemical Oxygen Demand </div>', unsafe_allow_html=True)
        st.markdown("""
            COD (Chemical Oxygen Demand) adalah parameter yang mengukur jumlah oksigen 
            yang dibutuhkan untuk mengoksidasi senyawa organik dalam air. Pengukuran ini 
            menggunakan K2Cr2O7 sebagai oksidator. COD digunakan untuk menilai tingkat pencemaran air.
        """)
        st.markdown("### Rumus Perhitungan")
        st.image('img/rumus.png', use_column_width=True)

    elif select_box == 'Cara Kerja':
        st.markdown('# <div style="text-align: center;"> Cara Kerja COD/KOK </div>', unsafe_allow_html=True)
        st.markdown("""
            1. **Persiapan Sampel**
            2. **Titrasi dengan FAS 0,02 N**
            3. **Standarisasi**
        """)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if lottie_json:
                st_lottie(lottie_json)
            else:
                st.error("Gagal memuat animasi.")

    elif select_box == 'Kalkulator COD':
        st.markdown('# <div style="text-align: center;"> Kalkulator COD </div>', unsafe_allow_html=True)
        st.subheader('Masukkan Nilai Parameter:')
        vb = st.number_input('Volume larutan FAS untuk Blanko (mL)', min_value=0.0)
        vc = st.number_input('Volume larutan FAS untuk Contoh Uji (mL)', min_value=0.0)
        nfas = st.number_input('Normalitas FAS', min_value=0.0, format='%.4f')
        vsample = st.number_input('Volume Contoh Uji (mL)', min_value=0.0)

        if st.button('Hitung COD'):
            if vsample == 0:
                st.error("Volume sampel tidak boleh 0.")
            else:
                cod_result = calculate_cod(vb, vc, nfas, vsample)
                st.success(f'Nilai Chemical Oxygen Demand sebesar {cod_result:.2f} mg O₂/L')
                quality_class = determine_quality_class(cod_result)
                st.info(f'Hasil dari Kadar COD tersebut {quality_class}')
                st.image('img/tabel.png', use_column_width=True)

    elif select_box == 'Our Group':
        st.markdown('## <div style="text-align: center;"> Kelompok 9 </div>', unsafe_allow_html=True)
        team_data = [
            {"name": "Dwi Nanda Sari", "image_url": "img/wi.jpg"},
            {"name": "Elsa Anggraeni", "image_url": "img/eca.jpg"},
            {"name": "M. Ihsan Taqiyuddin", "image_url": "img/cicak2.JPG"},
            {"name": "Rasikhah Maharani", "image_url": "img/rasi.jpg"},
            {"name": "Reyhan Riselvi", "image_url": "img/ray.jpg"}
        ]
        cols = st.columns(5)
        for col, member in zip(cols, team_data):
            with col:
                st.image(member["image_url"], use_column_width='auto', caption=member['name'])

        st.header(" ", divider="gray")
        st.caption('<div style="text-align: center;">Powered by Politeknik AKA BOGOR</div>', unsafe_allow_html=True)

# Menjalankan aplikasi
if __name__ == '__main__':
    main()
