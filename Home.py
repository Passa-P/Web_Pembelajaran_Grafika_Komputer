import streamlit as st

st.set_page_config(page_title="Grafika Komputer TI 3C", layout="wide")

st.sidebar.title("Navigasi Materi")
page = st.sidebar.radio("Pilih Materi", [
    "Home",
    "Materi 1: Pengantar Grafika Komputer",
    "Materi 2: Representasi Data Grafis & Transformasi 2D",
    "Materi 3: Algoritma Garis dan Lingkaran",
    "Materi 4: Algoritma Pengisian Poligon",
    "Materi 5: Model Warna dan Pencahayaan",
    "Materi 6: Teknik Shading (Flat, Gouraud, Phong)",
    "Materi 7: Teknik Texturing"
])

if page == "Home":
    st.title("📘 Materi Grafika Komputer Kelas TI 3C")
    st.write("Selamat datang di aplikasi pembelajaran Grafika Komputer!")
    st.markdown("---")
    st.info("Pilih materi di sidebar untuk mulai belajar.")
elif page == "Materi 1: Pengantar Grafika Komputer":
    import materi1
    materi1.render()
elif page == "Materi 2: Representasi Data Grafis & Transformasi 2D":
    import materi2
    materi2.render()
elif page == "Materi 3: Algoritma Garis dan Lingkaran":
    import materi3
    materi3.render()
elif page == "Materi 4: Algoritma Pengisian Poligon":
    import materi4
    materi4.render()
elif page == "Materi 5: Model Warna dan Pencahayaan":
    import materi5
    materi5.render()
elif page == "Materi 6: Teknik Shading (Flat, Gouraud, Phong)":
    import materi6
    materi6.render()
elif page == "Materi 7: Teknik Texturing":
    import materi7
    materi7.render()
