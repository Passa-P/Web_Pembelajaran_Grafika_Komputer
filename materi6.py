# materi6.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def generate_surface(size=50):
    """Membuat permukaan simulasi (gelombang 3D di 2D grid)"""
    x = np.linspace(-3, 3, size)
    y = np.linspace(-3, 3, size)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X**2 + Y**2)
    return X, Y, Z

def normalize(v):
    """Normalisasi vektor"""
    return v / np.linalg.norm(v)

def compute_normals(X, Y, Z):
    """Hitung normal permukaan dari turunan parsial"""
    dx, dy = np.gradient(Z)
    normals = np.dstack((-dx, -dy, np.ones_like(Z)))
    n_norm = np.linalg.norm(normals, axis=2)
    normals /= n_norm[:, :, np.newaxis]
    return normals

def shading_flat(normals, light_dir):
    """Flat shading: 1 nilai intensitas per poligon"""
    avg_normal = np.mean(normals, axis=(0, 1))
    intensity = np.dot(avg_normal, light_dir)
    return np.clip(intensity, 0, 1)

def shading_gouraud(normals, light_dir):
    """Gouraud shading: intensitas dihitung per vertex"""
    intensity = np.sum(normals * light_dir, axis=2)
    intensity = np.clip(intensity, 0, 1)
    return intensity

def shading_phong(normals, light_dir):
    """Phong shading: normal diinterpolasi lalu dihitung ulang (simulasi halus)"""
    intensity = np.sum(normals * light_dir, axis=2)
    intensity = np.clip(intensity, 0, 1)
    # Simulasi specular highlight sederhana
    specular = intensity ** 8
    return np.clip(intensity + 0.3 * specular, 0, 1)

def main():
    st.header(" Materi 6: Teknik Shading (Flat, Gouraud, dan Phong)")
    st.write("""
    **Shading** adalah teknik untuk memberikan efek pencahayaan pada permukaan objek 3D agar terlihat lebih realistis.
    
    Di sini kita akan membandingkan tiga metode populer:
    -  **Flat Shading** — satu warna rata per bidang (terlihat datar)
    -  **Gouraud Shading** — warna diinterpolasi antar vertex
    -  **Phong Shading** — normal diinterpolasi, menghasilkan pencahayaan halus
    """)

    # === Pengaturan Cahaya ===
    st.subheader(" Pengaturan Cahaya")
    lx = st.slider("Arah Cahaya X", -1.0, 1.0, 0.5)
    ly = st.slider("Arah Cahaya Y", -1.0, 1.0, 0.5)
    lz = st.slider("Arah Cahaya Z", 0.1, 1.0, 1.0)
    light_dir = normalize(np.array([lx, ly, lz]))

    # === Generate Permukaan ===
    X, Y, Z = generate_surface(80)
    normals = compute_normals(X, Y, Z)

    # === Hitung tiap shading ===
    flat_intensity = shading_flat(normals, light_dir)
    gouraud_intensity = shading_gouraud(normals, light_dir)
    phong_intensity = shading_phong(normals, light_dir)

    # === Visualisasi ===
    fig, ax = plt.subplots(1, 3, figsize=(12, 4))
    fig.suptitle("Perbandingan Teknik Shading", fontsize=14)

    # Flat shading: warna seragam
    ax[0].imshow(np.ones_like(Z) * flat_intensity, cmap="plasma", origin="lower")
    ax[0].set_title("Flat Shading")

    # Gouraud shading: interpolasi antar titik
    ax[1].imshow(gouraud_intensity, cmap="plasma", origin="lower")
    ax[1].set_title("Gouraud Shading")

    # Phong shading: halus dengan specular
    ax[2].imshow(phong_intensity, cmap="plasma", origin="lower")
    ax[2].set_title("Phong Shading")

    for a in ax:
        a.axis("off")

    st.pyplot(fig)

    st.markdown("""
    ---
    ###  Ringkasan:
    | Teknik | Deskripsi | Kelebihan | Kekurangan |
    |---------|------------|------------|-------------|
    | **Flat** | Warna 1 per bidang | Cepat | Terlihat kasar |
    | **Gouraud** | Interpolasi warna antar vertex | Halus, ringan | Tidak akurat untuk highlight kecil |
    | **Phong** | Interpolasi normal per pixel | Realistis | Perhitungan berat |
    """)

if __name__ == "__main__":
    main()
