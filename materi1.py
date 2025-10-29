import streamlit as st
import cv2
import numpy as np
import os

def main():
    st.title("Materi 1: Pengantar Grafika Komputer")
    st.markdown("---")
    st.header(" Materi 1: Pengantar Grafika Komputer (OpenCV)")
# ===========================
# Bagian Teori
# ===========================

    st.subheader("Apa itu Grafika Komputer?")
    st.write("""
    Grafika komputer adalah cabang ilmu komputer yang berfokus pada **pembuatan, manipulasi, dan representasi visual data secara digital**.
    Bidang ini memanfaatkan algoritma, matematika, serta perangkat keras grafis untuk menghasilkan gambar 2D maupun 3D yang realistis.
    """)

    st.subheader("Tujuan Grafika Komputer")
    st.markdown("""
    - Menampilkan informasi secara **visual dan interaktif**.
    - Membantu proses **simulasi, desain, dan permodelan**.
    - Meningkatkan **komunikasi antara manusia dan komputer**.
    - Mendukung **visualisasi ilmiah dan teknik** (misal: peta 3D, data medis, dll).
    """)

    st.subheader("Contoh Penerapan Grafika Komputer")
    st.markdown("""
    - **Animasi & Film** → Pixar, Disney, dan industri perfilman modern.  
    - **Desain Game** → Unity, Unreal Engine, dan sistem render real-time.  
    - **Visualisasi Data** → Grafik interaktif dan simulasi sains.  
    - **CAD (Computer-Aided Design)** → Desain arsitektur, otomotif, dan mesin.  
    - **Medis & Sains** → Rekonstruksi 3D, pencitraan medis (CT, MRI).  
    """)

    st.subheader("Sejarah Singkat Grafika Komputer")
    st.write("""
    - **1950-an** → Awal mula grafika komputer digunakan pada radar dan sistem militer.  
    - **1963** → Ivan Sutherland memperkenalkan *Sketchpad*, sistem interaktif pertama dengan tampilan grafis.  
    - **1970-an** → Munculnya teknologi *frame buffer* dan tampilan raster.  
    - **1980-an** → Grafika komputer mulai digunakan di film dan animasi 3D (misal: *Tron*).  
    - **1990-an hingga kini** → Kemajuan GPU dan software seperti OpenGL, DirectX, Blender, hingga Unreal Engine membuat grafika semakin realistis dan interaktif.  
    """)

    st.markdown("---")

# ===========================
# Bagian Praktik OpenCV
# ===========================

    st.header("Praktik Dasar Grafika Komputer dengan OpenCV")

    st.write("""
    Pada bagian ini, kita akan melakukan beberapa **transformasi dasar gambar** menggunakan pustaka **OpenCV** dan **NumPy**.
    Silakan pastikan kamu sudah memiliki file gambar bernama `foto.jpg` di folder proyek yang sama.
    """)

# Cari file gambar di folder yang sama
    current_dir = os.path.dirname(__file__)
    img_path = os.path.join(current_dir, "foto.jpg")
    img = cv2.imread(img_path)

    if img is None:
        st.error(f"Gambar 'foto.jpg' tidak ditemukan di folder: {current_dir}")
    else:
    # === Operasi 1: Putar 180 derajat + Mirror ===
        rotated = cv2.rotate(img, cv2.ROTATE_180)
        mirror_img = cv2.flip(rotated, 1)

    # === Operasi 2: RGB → Grayscale Manual ===
        b, g, r = cv2.split(img)
        grayscale_manual = (0.299*r + 0.587*g + 0.114*b).astype(np.uint8)

    # === Operasi 3: Negatif Warna ===
        negasi = 255 - img

    # === Operasi 4: Tambah Kecerahan ===
        brightness = cv2.convertScaleAbs(img, alpha=1, beta=50)

    # === Operasi 5: Tambah Kontras ===
        contrast = cv2.convertScaleAbs(img, alpha=1.5, beta=0)

    # === Tampilkan hasil dalam kolom Streamlit ===
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Gambar Asli", use_container_width=True)
            st.image(cv2.cvtColor(negasi, cv2.COLOR_BGR2RGB), caption="Negatif Warna", use_container_width=True)
        with col2:
            st.image(cv2.cvtColor(mirror_img, cv2.COLOR_BGR2RGB), caption="Mirror + Rotasi 180°", use_container_width=True)
            st.image(grayscale_manual, caption="Grayscale Manual", use_container_width=True)
        with col3:
            st.image(cv2.cvtColor(brightness, cv2.COLOR_BGR2RGB), caption="Brightness +50", use_container_width=True)
            st.image(cv2.cvtColor(contrast, cv2.COLOR_BGR2RGB), caption="Kontras x1.5", use_container_width=True)

    st.markdown("---")
    st.success("Kamu telah mempelajari dasar teori dan praktik grafika komputer pada Materi 1!")
