import streamlit as st

def render():
    st.title("🖥️ Materi 1: Pengantar Grafika Komputer")
    st.markdown("---")

    # ====== Pengertian ======
    st.subheader("Apa itu Grafika Komputer?")
    st.write("""
    Grafika komputer adalah cabang ilmu komputer yang berfokus pada **pembuatan, manipulasi, penyimpanan, dan representasi visual data**
    menggunakan komputer.  
    Dengan grafika komputer, kita dapat menghasilkan gambar, animasi, simulasi, serta visualisasi yang membantu komunikasi dan analisis data.
    """)

    # ====== Tujuan ======
    st.subheader("Tujuan Grafika Komputer")
    st.markdown("""
    - 🎨 Menampilkan informasi secara **visual dan interaktif**.  
    - 🧠 Membantu **simulasi dan pemodelan** dalam berbagai bidang (medis, arsitektur, teknik).  
    - 💬 Meningkatkan **interaksi antara manusia dan komputer** (Human-Computer Interaction).  
    - 📊 Menyediakan **visualisasi data kompleks** agar lebih mudah dipahami.  
    - 🎮 Mendukung **hiburan digital** seperti animasi, film, dan video game.
    """)

    # ====== Sejarah ======
    st.subheader("Sejarah Perkembangan Grafika Komputer")
    st.write("""
    Perkembangan grafika komputer dimulai sejak tahun 1950-an dan terus berkembang hingga kini.
    
    #### 🕰️ 1950–1960: Awal Mula
    - Tahun 1950-an, komputer hanya mampu menampilkan teks sederhana.
    - Tahun 1951, muncul **komputer Whirlwind** di MIT yang dapat menampilkan titik cahaya di layar CRT.
    - Tahun 1963, **Ivan Sutherland** menciptakan *Sketchpad*, sistem grafis pertama yang memungkinkan menggambar langsung di layar dengan pena cahaya (*light pen*).
    
    #### 💾 1970–1980: Era Grafik Vektor dan Warna
    - Muncul teknologi **raster graphics** yang memungkinkan tampilan berbasis piksel.
    - Komputer pribadi seperti **Apple II** dan **IBM PC** mulai mendukung tampilan warna.
    - Banyak algoritma grafika dasar ditemukan, seperti algoritma **Bresenham**, **DDA**, dan **Scanline**.

    #### 🧩 1990–2000: Revolusi 3D
    - Teknologi grafis 3D mulai digunakan secara luas dalam film dan game.
    - Perkembangan **OpenGL** dan **DirectX** memungkinkan pengembangan aplikasi grafis secara real-time.
    - Film seperti *Toy Story (1995)* menjadi film animasi 3D penuh pertama di dunia.

    #### 🚀 2000–Sekarang: Realisme dan Virtualisasi
    - GPU semakin canggih dengan arsitektur paralel.
    - Munculnya teknologi seperti **Ray Tracing**, **Virtual Reality (VR)**, **Augmented Reality (AR)**, dan **AI-assisted rendering**.
    - Software modern seperti **Blender**, **Unity**, dan **Unreal Engine** menjadi standar industri.
    """)

    # ====== Aplikasi ======
    st.subheader("Aplikasi Grafika Komputer dalam Kehidupan Nyata")
    st.markdown("""
    Grafika komputer digunakan hampir di semua bidang kehidupan modern:

    | Bidang | Contoh Aplikasi | Deskripsi |
    |--------|------------------|------------|
    | 🎮 **Hiburan & Game** | Unity, Unreal Engine, Blender | Pembuatan animasi, film, efek visual, dan video game. |
    | 🏗️ **Arsitektur & Desain** | AutoCAD, SketchUp, Revit | Membuat model 3D bangunan dan simulasi desain. |
    | 🧬 **Medis & Sains** | MRI Visualization, Simulation Tools | Menampilkan data medis secara visual 3D untuk analisis. |
    | 🚗 **Otomotif & Industri** | CAD/CAM Systems | Simulasi desain produk dan proses manufaktur. |
    | 📊 **Data Science & Analisis** | Tableau, Power BI, Matplotlib | Menyajikan data besar menjadi grafik dan dashboard interaktif. |
    | 🧠 **Pendidikan & Penelitian** | Simulasi 3D, e-Learning | Membantu pembelajaran interaktif dan visualisasi konsep kompleks. |

    """)

    # ====== Ringkasan ======
    st.markdown("---")
    st.subheader("🧭 Ringkasan")
    st.write("""
    - Grafika komputer merupakan bidang penting dalam perkembangan teknologi visual modern.  
    - Berawal dari sistem sederhana berbasis vektor, kini berkembang menjadi **grafis 3D real-time dan AI rendering**.  
    - Aplikasinya sangat luas, dari **film animasi, simulasi ilmiah, hingga augmented reality**.
    """)

    st.info("Lanjutkan ke **Materi 2** untuk mempelajari Representasi Data Grafis dan Transformasi 2D.")
