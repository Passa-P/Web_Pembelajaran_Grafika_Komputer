# materi7.py
import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

# ---------- TEXTURE → SPHERE PROJECTION ----------
def generate_sphere_texture(texture_img, size=200):
    """Proyeksikan tekstur (BGR) ke bola 2D. Aman dari IndexError."""
    h, w, _ = texture_img.shape
    tex = texture_img  # biarkan ukuran asli; u,v akan diskalakan ke (w,h)
    sphere = np.zeros((size, size, 3), dtype=np.uint8)

    # grid koordinat (x,y)
    y, x = np.indices((size, size))
    cx = cy = size // 2
    r = size // 2

    # mask lingkaran (area bola)
    mask = (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2

    # posisi ter-normalisasi [-1,1]
    xn = (x - cx) / r
    yn = (y - cy) / r

    # z dari persamaan bola (x^2 + y^2 + z^2 = 1)
    z = np.zeros_like(xn, dtype=np.float64)
    inside = (xn**2 + yn**2) <= 1
    z[inside] = np.sqrt(1.0 - (xn[inside]**2 + yn[inside]**2))

    # spherical coords
    theta = np.arctan2(yn, xn)                      # [-pi, pi]
    phi = np.arccos(np.clip(z, -1.0, 1.0))          # [0, pi]

    # UV [0,1]
    u = (theta + np.pi) / (2.0 * np.pi)
    v = (phi / np.pi)

    # ke indeks gambar
    u = (u * (w - 1)).astype(int)
    v = (v * (h - 1)).astype(int)

    # kunci agar selalu valid
    u = np.clip(u, 0, w - 1)
    v = np.clip(v, 0, h - 1)

    sphere[mask] = tex[v[mask], u[mask]]
    return sphere, mask


# ---------- STREAMLIT MAIN ----------
def main():
    st.header("📘 Materi 7: Teknik Texturing")
    st.write("""
    **Texturing** adalah teknik memberikan gambar (tekstur) pada permukaan objek
    untuk menambah realisme. Contohnya: kulit bumi di bola dunia, bata di dinding, dsb.
    """)

    tab1, tab2 = st.tabs(["🧱 Konsep Dasar", "🌍 Demo Tekstur pada Bola"])

    # ---------- TAB 1: KONSEP DASAR ----------
    with tab1:
        st.subheader("🧩 Apa itu Texturing?")
        st.markdown("""
        - **Texturing**: proses memproyeksikan gambar (texture map) ke permukaan objek 3D.  
        - Gambar ini disebut **texture map**, dan setiap titik di permukaan memiliki koordinat **(u, v)** untuk mengambil warna dari gambar.  
        - Model 3D yang diberi tekstur terlihat lebih realistis dibanding warna polos.
        """)

        os.makedirs("assets", exist_ok=True)

        # dukung format jpeg/jpg/png
        def find_asset(name):
            for ext in ["png", "jpg", "jpeg"]:
                path = os.path.join("assets", f"{name}.{ext}")
                if os.path.exists(path):
                    return path
            return None

        uv_path = find_asset("uvmap")
        cube_path = find_asset("cube")

        if uv_path and cube_path:
            st.image(
                [uv_path, cube_path],
                caption=["Proyeksi UV Mapping", "Contoh hasil texturing pada kubus"],
                use_container_width=True
            )
        else:
            st.warning("⚠️ Ilustrasi tidak ditemukan. Pastikan file 'uvmap' dan 'cube' ada di folder assets.")

    # ---------- TAB 2: DEMO SPHERE ----------
    with tab2:
        st.subheader("🌍 Demo Penerapan Tekstur pada Bola (Simulasi 2D)")

        uploaded_file = st.file_uploader(
            "Unggah gambar tekstur (jpg/png). Contoh: peta dunia, pola kain, marmer, kayu.",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_file is not None:
            file_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
            texture = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            if texture is None:
                st.error("Gagal membaca file yang diunggah.")
                return
        else:
            st.info("Tidak ada file diunggah → gunakan tekstur default (checkerboard) 🧱")
            size = 400
            tile = 40
            texture = np.zeros((size, size, 3), dtype=np.uint8)
            for yy in range(size):
                for xx in range(size):
                    if (xx // tile + yy // tile) % 2 == 0:
                        texture[yy, xx] = (240, 240, 240)
                    else:
                        texture[yy, xx] = (50, 50, 50)

        sphere, _ = generate_sphere_texture(texture, size=300)

        fig, ax = plt.subplots(1, 2, figsize=(9, 4))
        ax[0].imshow(cv2.cvtColor(texture, cv2.COLOR_BGR2RGB))
        ax[0].set_title("Texture Map (2D)")
        ax[0].axis("off")

        ax[1].imshow(cv2.cvtColor(sphere, cv2.COLOR_BGR2RGB))
        ax[1].set_title("Textured Sphere (Simulasi)")
        ax[1].axis("off")

        st.pyplot(fig)

        st.markdown("""
        - Kiri: tekstur datar (2D).  
        - Kanan: hasil pemetaan ke permukaan bola (2D).  
        - Koordinat **(u, v)** digunakan untuk sampling warna dari tekstur.
        """)

    st.markdown("""
    ---
    ### 🧠 Ringkasan:
    | Aspek | Penjelasan |
    |------|------------|
    | **Texture Map** | Gambar 2D yang digunakan sebagai kulit objek 3D |
    | **UV Mapping**  | Pemetaan titik permukaan ke koordinat (u, v) pada gambar |
    | **Hasil**       | Permukaan objek terlihat detail & realistis |
    """)


if __name__ == "__main__":
    main()
