import streamlit as st

# ⬇️ Harus paling atas
st.set_page_config(page_title="Grafika Komputer TI-3C", page_icon="💻", layout="wide")

# Import file materi
import materi1
import materi2
import materi3
import materi4
import materi5
import materi6
import materi7
import materi8

# === SIDEBAR NAVIGASI ===
st.sidebar.title("Navigasi Materi")
menu = st.sidebar.radio(
    "Pilih Materi:",
    [
        "Home",
        "Materi 1: Pengantar Grafika Komputer",
        "Materi 2: Representasi Data Grafis & Transformasi 2D",
        "Materi 3: Algoritma Garis dan Lingkaran",
        "Materi 4: Algoritma Pengisian Poligon",
        "Materi 5: Model Warna dan Pencahayaan",
        "Materi 6: Teknik Shading (Flat, Gouraud, Phong)",
        "Materi 7: Teknik Texturing",
        "Materi 8: Simulasi Bola 3D Realistis (Lighting + Shading + Texturing)"
    ]
)

# === TAMPILKAN KONTEN SESUAI PILIHAN ===
if menu == "Home":
    st.title("Grafika Komputer - TI 3C")
    st.write("""
    Selamat datang di aplikasi pembelajaran interaktif **Grafika Komputer**!  
    Aplikasi ini dibuat untuk membantu mahasiswa memahami konsep visualisasi komputer, 
    transformasi 2D & 3D, serta simulasi pencahayaan dan tekstur.
    """)
    st.info("Gunakan sidebar di sebelah kiri untuk memilih materi yang ingin kamu pelajari.")
    st.markdown("---")
    st.markdown("**Dibuat oleh:** Kelompok Grafika Komputer TI-3C  \n*UTS Semester Ganjil 2025/2026*")

elif menu.startswith("Materi 1"):
    materi1.main()
elif menu.startswith("Materi 2"):
    materi2.main()
elif menu.startswith("Materi 3"):
    materi3.main()
elif menu.startswith("Materi 4"):
    materi4.main()
elif menu.startswith("Materi 5"):
    materi5.main()
elif menu.startswith("Materi 6"):
    materi6.main()
elif menu.startswith("Materi 7"):
    materi7.main()
elif menu.startswith("Materi 8"):
    materi8.main()
