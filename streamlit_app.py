import streamlit as st
import math
# Fungsi untuk menghitung jumlah titik sampling
def calculate_sampling_points(diameter_cm, height_m):
diameter_m = diameter_cm / 100 # Convert cm to meters
if diameter_m <= 0 or height_m <= 0:
return None, "Diameter dan tinggi cerobong harus lebih besar dari nol."
if diameter_m < 0.6:
return None, "Diameter terlalu kecil untuk sampling yang akurat."
# Panduan umum untuk titik sampling
if diameter_m <= 2.5:
points = 3
elif diameter_m <= 5:
points = 4
elif diameter_m <= 10:
points = 6
elif diameter_m <= 15:
points = 8
else:
points = 12
# Tambahan untuk tinggi cerobong (untuk menghindari aliran yang tidak seragam)
if height_m > 20:
points += 2
return points, None
# Fungsi untuk menghitung jarak antar titik sampling per titik
def calculate_spacing_per_point(diameter_cm, points):
return diameter_cm / points

# Streamlit UI
st.set_page_config(page_title="Perhitungan Titik Sampling Cerobong", layout="wide")
# Tambahkan CSS untuk latar belakang gambar dan teks hitam,
termasuk header
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image:
url("https://images.unsplash.com/photo-1501426026826-31c667b
df23d");
background-size: cover;
}
[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p, [data-testid="stSidebar"] li {
color: white;
}
.stMarkdown {
color: black;
}
.stNumberInput div {
color: white; /* Mengubah warna teks input menjadi putih */
}
h2 {
color: black;
border-bottom: 4px solid black;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
# Sidebar menu
st.sidebar.title('Menu')
menu = st.sidebar.radio('Pilih Menu', ['Selamat Datang',
'Pengertian Titik Sampling', 'Penjelasan Baku Mutu', 'Perhitungan dan Hasil'])
# Fungsi untuk membuat header dengan garis tebal hitam
def bold_black_header(text):
st.markdown(f"<h2 style='border-bottom: 4px solid black; color: black;'>{text}</h2>", unsafe_allow_html=True)
if menu == 'Selamat Datang':
bold_black_header('Selamat Datang')
st.write(
"""\
Selamat datang di aplikasi perhitungan titik sampling pada cerobong.
Kelompok 5:
1. Alvina Adinda Putri (2330484)
2. Azzahra Aulia Putri (2330492)
3. Fadhil Zhafran Ramadhani (2330497)
4. Landi Hidayat (2330507)
5. Muhammad Fadhil Khoirurrizal (2150016)
6. Sabrina Putri Faradhilla (2330528)
"""
)
elif menu == 'Pengertian Titik Sampling':
bold_black_header('Pengertian Titik Sampling pada Cerobong')
st.write(
"""\
Penentuan titik sampling pada cerobong adalah proses
penting dalam pengukuran emisi gas dari cerobong industri.
Titik-titik ini ditentukan untuk memastikan bahwa sampel
yang diambil representatif dari keseluruhan aliran gas.
Secara umum, titik sampling harus didistribusikan secara
merata pada penampang cerobong dan pada area yang mewakili
aliran gas di cerobong. Pemilihan titik sampling yang tepat
sangat penting untuk mendapatkan hasil yang akurat dan dapat
diandalkan.
"""
)
elif menu == 'Penjelasan Baku Mutu':
bold_black_header('Penjelasan Baku Mutu Berdasarkan SNI 7117.13:2009')
st.write(
"""\
Baku mutu berdasarkan SNI 7117.13:2009 mengatur cara
pengambilan sampel untuk pengukuran emisi dari cerobong
industri.
Berikut adalah poin-poin penting dari baku mutu tersebut:
1. Jumlah Titik Sampling:
- Diameter ≤ 0.6 m: 1 titik
- Diameter > 0.6 m dan ≤ 2.5 m: 3 titik
- Diameter > 2.5 m dan ≤ 5 m: 4 titik
- Diameter > 5 m dan ≤ 10 m: 6 titik
- Diameter > 10 m: 8 titik (atau lebih sesuai kebutuhan
teknis)
2. Distribusi Titik Sampling:
- Titik-titik sampling harus didistribusikan pada posisi
yang mewakili aliran gas di seluruh penampang cerobong.
- Titik-titik tersebut biasanya ditempatkan pada jarak yang
sama di seluruh penampang cerobong.
3. Jarak Antar Titik Sampling:
- Jarak antar titik sampling ditentukan berdasarkan
diameter cerobong dan jumlah titik sampling.
- Jarak harus cukup untuk mendapatkan data yang
representatif dan tidak saling tumpang tindih.
4. Ketinggian Pengambilan Sampel:
- Titik sampling pada cerobong harus diambil pada
ketinggian yang mewakili aliran gas secara keseluruhan.
- Biasanya tidak lebih dari 1/3 atau 1/2 dari tinggi
cerobong.
5. Standar Prosedur Pengambilan Sampel:
- Prosedur pengambilan sampel harus mengikuti pedoman
teknis yang tercantum dalam SNI 7117.13:2009 untuk
memastikan akurasi dan konsistensi hasil pengukuran.
- Pengambilan sampel harus dilakukan dengan peralatan
yang memenuhi standar dan dioperasikan oleh personel yang
terlatih.
"""
)
elif menu == 'Perhitungan dan Hasil':
bold_black_header('Perhitungan dan Hasil Titik Sampling')
# Input dari pengguna
diameter_cm = st.number_input('Masukkan diameter cerobong (cm):', min_value=0.0)
height_m = st.number_input('Masukkan tinggi cerobong (meter):', min_value=0.0)
if st.button('Hitung Jumlah Titik Sampling dan Jarak Antar Titik'):
points, error_message =
calculate_sampling_points(diameter_cm, height_m)
if error_message:
st.write(error_message)
else:
spacing_per_point =
calculate_spacing_per_point(diameter_cm, points)
st.write(f'Jumlah titik sampling yang direkomendasikan:{points}')
st.write(f'Jarak antar titik sampling per titik (sekitar):
{spacing_per_point:.2f} cm')
