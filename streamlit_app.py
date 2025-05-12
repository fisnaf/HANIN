import streamlit as st
import base64
import requests

# Function to calculate Chemical Oxygen Demand (COD)
def calculate_cod(vb, vc, nfas, vsample):
    cod_value = ((vb - vc) * nfas * 8000) / vsample
    return cod_value

# Function to determine environmental quality class
def determine_quality_class(cod_value):
    if 0 <= cod_value <= 10:
        return "memenuhi Baku Mutu Lingkungan (BML) dalam Kelas 1 berdasarkan PP No.22 Tahun 2021..."
    elif 10 < cod_value <= 25:
        return "memenuhi BML dalam Kelas 2 berdasarkan PP No.22 Tahun 2021..."
    elif 25 < cod_value <= 40:
        return "memenuhi BML dalam Kelas 3 berdasarkan PP No.22 Tahun 2021..."
    elif 40 < cod_value <= 80:
        return "memenuhi BML dalam Kelas 4 berdasarkan PP No.22 Tahun 2021..."
    else:
        return "tidak memenuhi Baku Mutu Lingkungan (BML) yang ditetapkan dalam PP No.22 Tahun 2021"

# Fungsi untuk mengonversi gambar ke base64
def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Tampilan Sidebar Logo
img_path = "img/icon_aka.png"  
img_base64 = img_to_base64(img_path)
st.sidebar.markdown(
    f'<img src="data:image/png;base64,{img_base64}" style="width: 100%; height: auto;">',
    unsafe_allow_html=True,
)

# Streamlit UI
def main():
    st.sidebar.title('Main Menu')
    select_box = st.sidebar.selectbox('', ('Pengantar', 'Cara Kerja', 'Kalkulator COD', 'Our Group'))

    if select_box == 'Pengantar':
        st.markdown('# <div style="text-align: center;"> Chemical Oxygen Demand </div>', unsafe_allow_html=True)
        st.markdown("""
            :red[COD (Chemical Oxygen Demand)] adalah parameter untuk mengukur jumlah oksigen...
            ### Rumus Perhitungan
        """)
        st.image('img/rumus.png', use_column_width=True)

    elif select_box == 'Cara Kerja':
        st.markdown('# <div style="text-align: center;"> Cara Kerja COD/KOK </div>', unsafe_allow_html=True)
        st.markdown("""
            ### Proses Pengukuran COD/KOK:
            1. Persiapan Sampel ...
            2. Titrasi ...
            3. Proses Standarisasi ...
        """)
        st.image("img/animasi_pengolahan.png", caption="Ilustrasi Pengolahan COD", use_column_width=True)

    elif select_box == 'Kalkulator COD':
        st.markdown('# <div style="text-align: center;"> Kalkulator COD </div>', unsafe_allow_html=True)
        st.subheader('Masukkan Nilai Parameter:')
        vb = st.number_input('Volume larutan FAS untuk Blanko (mL)', min_value=0.0)
        vc = st.number_input('Volume larutan FAS untuk Contoh Uji (mL)', min_value=0.0)
        nfas = st.number_input('Normalitas FAS', min_value=0.0, format='%.4f')
        vsample = st.number_input('Volume Contoh Uji (mL)', min_value=0.0)

        if st.button('Hitung COD'):
            cod_result = calculate_cod(vb, vc, nfas, vsample)
            st.success(f'Nilai COD: {cod_result:.2f} mg O2/L')
            quality_class = determine_quality_class(cod_result)
            st.info(f'Hasil dari kadar COD tersebut {quality_class}')
            st.image('img/tabel.png', use_column_width=True)

    elif select_box == 'Our Group':
        st.markdown('## <div style="text-align: center;"> Kelompok 9 </div>', unsafe_allow_html=True)
        team_data = [
            {"name": "Dwi Nanda Sari","image_url": "img/wi.jpg"},
            {"name": "Elsa Anggraeni", "image_url": "img/eca.jpg"},
            {"name": "M. Ihsan Taqiyuddin", "image_url": "img/cicak2.JPG"},
            {"name": "Rasikhah Maharani Liliana Bakti", "image_url": "img/rasi.jpg"},
            {"name": "Reyhan Riselvi", "image_url": "img/ray.jpg"}
        ]
        cols = st.columns(5)
        for i, member in enumerate(team_data):
            with cols[i % 5]:
                st.image(member["image_url"], use_column_width='auto', caption=member["name"])
        st.header(" ", divider="gray")
        st.caption('<div style="text-align: center;">Powered by Politeknik AKA BOGOR</div>', unsafe_allow_html=True)

# Pastikan ini benar (sebelumnya kamu salah tulis __name__)
if __name__ == '__main__':
    main()
