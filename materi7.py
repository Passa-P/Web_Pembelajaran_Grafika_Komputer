# materi7.py
import streamlit as st           # Untuk membuat tampilan web interaktif
import numpy as np               # Untuk operasi matematika dan array
import cv2                       # OpenCV, untuk membaca dan memproses gambar
import matplotlib.pyplot as plt   # Untuk menampilkan gambar/plot
import os                        # Untuk akses dan pengecekan file/folder

# ---------- TEXTURE → SPHERE PROJECTION ----------
def generate_sphere_texture(texture_img, size=200):
    """Proyeksikan tekstur (BGR) ke bola 2D. Aman dari IndexError."""
    # Ambil ukuran gambar tekstur
    h, w, _ = texture_img.shape
    tex = texture_img  # Gunakan tekstur asli (tidak diubah ukurannya)
    sphere = np.zeros((size, size, 3), dtype=np.uint8)  # Buat kanvas kosong untuk bola

    # Buat grid koordinat (x,y) dari 0 sampai size
    y, x = np.indices((size, size))
    cx = cy = size // 2  # Titik tengah bola
    r = size // 2        # Jari-jari bola

    # Buat mask berbentuk lingkaran (area di dalam bola)
    mask = (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2

    # Normalisasi koordinat ke range [-1, 1]
    xn = (x - cx) / r
    yn = (y - cy) / r

    # Hitung nilai z dari persamaan bola (x² + y² + z² = 1)
    z = np.zeros_like(xn, dtype=np.float64)
    inside = (xn**2 + yn**2) <= 1  # hanya titik yang berada di dalam bola
    z[inside] = np.sqrt(1.0 - (xn[inside]**2 + yn[inside]**2))

    # Ubah koordinat kartesian ke koordinat bola (spherical coordinates)
    theta = np.arctan2(yn, xn)             # sudut arah horizontal ([-π, π])
    phi = np.arccos(np.clip(z, -1.0, 1.0)) # sudut vertikal ([0, π])

    # Ubah ke koordinat UV (0–1) → digunakan untuk mapping tekstur
    u = (theta + np.pi) / (2.0 * np.pi)
    v = (phi / np.pi)

    # Ubah u,v menjadi indeks gambar (piksel)
    u = (u * (w - 1)).astype(int)
    v = (v * (h - 1)).astype(int)

    # Pastikan indeks tidak keluar batas array
    u = np.clip(u, 0, w - 1)
    v = np.clip(v, 0, h - 1)

    # Isikan warna dari tekstur ke permukaan bola (berdasarkan u,v)
    sphere[mask] = tex[v[mask], u[mask]]
    return sphere, mask  # Kembalikan hasil bola dan mask-nya


# ---------- STREAMLIT MAIN ----------
def main():
    # Judul halaman Streamlit
    st.header(" Materi 7: Teknik Texturing")
    st.write("""
    **Texturing** adalah teknik memberikan gambar (tekstur) pada permukaan objek
    untuk menambah realisme. Contohnya: kulit bumi di bola dunia, bata di dinding, dsb.
    """)

    # Buat dua tab untuk pembelajaran: konsep dasar & demo
    tab1, tab2 = st.tabs([" Konsep Dasar", "🌍 Demo Tekstur pada Bola"])

    # ---------- TAB 1: KONSEP DASAR ----------
    with tab1:
        st.subheader(" Apa itu Texturing?")
        st.markdown("""
        - **Texturing**: proses memproyeksikan gambar (texture map) ke permukaan objek 3D.  
        - Gambar ini disebut **texture map**, dan setiap titik di permukaan memiliki koordinat **(u, v)** untuk mengambil warna dari gambar.  
        - Model 3D yang diberi tekstur terlihat lebih realistis dibanding warna polos.
        """)

        os.makedirs("assets", exist_ok=True)  # Pastikan folder assets ada

        # Fungsi bantu untuk mencari file gambar di folder assets
        def find_asset(name):
            for ext in ["png", "jpg", "jpeg"]:
                path = os.path.join("assets", f"{name}.{ext}")
                if os.path.exists(path):
                    return path
            return None  # Jika tidak ditemukan

        # Coba cari dua gambar ilustrasi
        uv_path = find_asset("uvmap")
        cube_path = find_asset("cube")

        # Jika gambar ada, tampilkan keduanya
        if uv_path and cube_path:
            st.image(
                [uv_path, cube_path],
                caption=["Proyeksi UV Mapping", "Contoh hasil texturing pada kubus"],
                use_container_width=True
            )
        else:
            # Jika tidak ada, beri peringatan
            st.warning(" Ilustrasi tidak ditemukan. Pastikan file 'uvmap' dan 'cube' ada di folder assets.")

    # ---------- TAB 2: DEMO SPHERE ----------
    with tab2:
        st.subheader(" Demo Penerapan Tekstur pada Bola (Simulasi 2D)")

        # Upload gambar dari pengguna
        uploaded_file = st.file_uploader(
            "Unggah gambar tekstur (jpg/png). Contoh: peta dunia, pola kain, marmer, kayu.",
            type=["jpg", "jpeg", "png"]
        )

        # Jika pengguna mengunggah file
        if uploaded_file is not None:
            file_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
            texture = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)  # Baca gambar menggunakan OpenCV
            if texture is None:
                st.error("Gagal membaca file yang diunggah.")
                return
        else:
            # Jika tidak ada file diunggah, gunakan pola checkerboard sebagai default
            st.info("Tidak ada file diunggah → gunakan tekstur default (checkerboard) 🧱")
            size = 400
            tile = 40
            texture = np.zeros((size, size, 3), dtype=np.uint8)
            for yy in range(size):
                for xx in range(size):
                    # Pola kotak hitam putih
                    if (xx // tile + yy // tile) % 2 == 0:
                        texture[yy, xx] = (240, 240, 240)  # kotak terang
                    else:
                        texture[yy, xx] = (50, 50, 50)      # kotak gelap

        # Proses tekstur agar diproyeksikan ke bentuk bola 2D
        sphere, _ = generate_sphere_texture(texture, size=300)

        # Tampilkan hasil perbandingan gambar
        fig, ax = plt.subplots(1, 2, figsize=(9, 4))
        ax[0].imshow(cv2.cvtColor(texture, cv2.COLOR_BGR2RGB))
        ax[0].set_title("Texture Map (2D)")      # Gambar asli
        ax[0].axis("off")

        ax[1].imshow(cv2.cvtColor(sphere, cv2.COLOR_BGR2RGB))
        ax[1].set_title("Textured Sphere (Simulasi)")  # Gambar hasil proyeksi
        ax[1].axis("off")

        st.pyplot(fig)  # Tampilkan di halaman Streamlit

        # Penjelasan tambahan
        st.markdown("""
        - Kiri: tekstur datar (2D).  
        - Kanan: hasil pemetaan ke permukaan bola (2D).  
        - Koordinat **(u, v)** digunakan untuk sampling warna dari tekstur.
        """)

    # Ringkasan akhir dalam bentuk tabel
    st.markdown("""
    ---
    ###  Ringkasan:
    | Aspek | Penjelasan |
    |------|------------|
    | **Texture Map** | Gambar 2D yang digunakan sebagai kulit objek 3D |
    | **UV Mapping**  | Pemetaan titik permukaan ke koordinat (u, v) pada gambar |
    | **Hasil**       | Permukaan objek terlihat detail & realistis |
    """)


# Pastikan kode hanya dijalankan ketika file ini dieksekusi langsung
if __name__ == "__main__":
    main()
