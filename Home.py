# Home.py
import streamlit as st
import materi1
import materi2
import materi3
import materi4
import materi5
import materi6
import materi7
import materi8

st.set_page_config(page_title="Grafika Komputer TI 3C", layout="wide")

st.sidebar.title("Navigasi Materi")
materi = st.sidebar.radio(
    "Pilih Materi",
    [
        "Home",
        "Materi 1: Pengantar Grafika Komputer",
        "Materi 2: Representasi Data Grafis & Transformasi 2D",
        "Materi 3: Algoritma Garis dan Lingkaran",
        "Materi 4: Algoritma Pengisian Poligon",
        "Materi 5: Model Warna dan Pencahayaan",
        "Materi 6: Teknik Shading (Flat, Gouraud, Phong)",
        "Materi 7: Teknik Texturing",
        "Materi 8: Simulasi Bola 3D Realistis",
    ]
)

if materi == "Home":
    st.title("🎨 Grafika Komputer TI 3C")
    st.write("""
    Selamat datang di aplikasi pembelajaran interaktif Grafika Komputer.
    Gunakan menu di samping kiri untuk memilih materi.
    """)

elif materi.startswith("Materi 1"):
    materi1.main()

elif materi.startswith("Materi 2"):
    materi2.main()

elif materi.startswith("Materi 3"):
    materi3.main()

elif materi.startswith("Materi 4"):
    materi4.main()

elif materi.startswith("Materi 5"):
    materi5.main()

elif materi.startswith("Materi 6"):
    materi6.main()

elif materi.startswith("Materi 7"):
    materi7.main()

elif materi.startswith("Materi 8"):
    materi8.main()
