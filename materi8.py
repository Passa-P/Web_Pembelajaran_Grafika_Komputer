# materi8.py
import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt

# ---------- UTIL ----------
def normalize(v, axis=-1, eps=1e-9):
    n = np.linalg.norm(v, axis=axis, keepdims=True)
    return v / (n + eps)

def make_checkerboard(size=512, tile=32):
    tex = np.zeros((size, size, 3), dtype=np.uint8)
    for y in range(size):
        for x in range(size):
            if (x // tile + y // tile) % 2 == 0:
                tex[y, x] = (235, 235, 235)  # terang (BGR)
            else:
                tex[y, x] = (40, 40, 40)     # gelap (BGR)
    return tex

def sample_texture_bgr(texture_bgr, u, v):
    """Ambil warna dari tekstur (BGR) menggunakan indeks integer u,v yang sudah diklip."""
    h, w, _ = texture_bgr.shape
    u = np.clip(u, 0, w - 1)
    v = np.clip(v, 0, h - 1)
    return texture_bgr[v, u]

# ---------- UV MAPPING KE BOLA ----------
def project_sphere_uv(size=512):
    """
    Kembalikan:
      mask: area lingkaran
      N: normal per-pixel (H x W x 3)
      uv: pasangan indeks (u,v) untuk sampling tekstur
    """
    y, x = np.indices((size, size))
    cx = cy = size // 2
    r = size // 2

    # koordinat ter-normalisasi
    xn = (x - cx) / r
    yn = (y - cy) / r
    rsq = xn**2 + yn**2
    mask = rsq <= 1.0

    z = np.zeros_like(xn, dtype=np.float64)
    z[mask] = np.sqrt(1.0 - rsq[mask])

    # normal permukaan (arah ke kamera z>=0)
    N = np.dstack([xn, yn, z])
    N = normalize(N)

    # spherical coords → UV
    theta = np.arctan2(yn, xn)           # [-pi, pi]
    phi   = np.arccos(np.clip(z, -1, 1)) # [0, pi]
    u = ((theta + np.pi) / (2.0 * np.pi)) # [0,1]
    v = (phi / np.pi)                     # [0,1]

    return mask, N, u, v

# ---------- SHADING BLINN–PHONG ----------
def shade_sphere(texture_bgr, size=512, light_dir=(0.5, 0.5, 1.0),
                 ka=0.2, kd=0.9, ks=0.3, shininess=32, spec_color=(255,255,255)):
    """
    Texturing + Blinn–Phong shading.
    Semua komputasi di ruang gambar 2D sebagai simulasi bola.
    """
    mask, N, u01, v01 = project_sphere_uv(size)

    # siapkan indeks tekstur
    h, w, _ = texture_bgr.shape
    u_idx = (u01 * (w - 1)).astype(int)
    v_idx = (v01 * (h - 1)).astype(int)

    # sample tekstur (BGR 0..255)
    base = np.zeros((size, size, 3), dtype=np.uint8)
    base[mask] = sample_texture_bgr(texture_bgr, u_idx[mask], v_idx[mask])

    # ubah ke float 0..1 untuk shading
    base_f = base.astype(np.float32) / 255.0

    # vektor cahaya & view (ke kamera)
    L = np.array(light_dir, dtype=np.float64)
    L = normalize(L)
    L = np.broadcast_to(L, N.shape)  # (H,W,3)

    V = np.array([0.0, 0.0, 1.0], dtype=np.float64)   # kamera di +Z
    V = np.broadcast_to(V, N.shape)

    # Blinn-Phong: H = normalize(L+V)
    H = normalize(L + V)

    # komponen
    NdL = np.clip(np.sum(N * L, axis=2, keepdims=True), 0.0, 1.0)         # diffuse
    NdH = np.clip(np.sum(N * H, axis=2, keepdims=True), 0.0, 1.0) ** shininess  # specular

    # warna specular (putih)
    spec = (np.array(spec_color, dtype=np.float32) / 255.0).reshape(1,1,3)

    # gabung (per channel)
    color = ka * base_f + kd * (base_f * NdL) + ks * (spec * NdH)

    # tonemap sederhana
    color = np.clip(color, 0.0, 1.0)
    out = (color * 255.0).astype(np.uint8)

    # latar transparan (hitam) di luar bola
    out[~mask] = 0
    return out, base

# ---------- STREAMLIT ----------
def main():
    st.header(" Materi 8: Simulasi Bola 3D Realistis (Lighting + Shading + Texturing)")
    st.write("""
    Demo ini menggabungkan **texturing** (UV mapping ke bola) dengan **pencahayaan Blinn–Phong** (ambient, diffuse, specular).
    Atur arah cahaya dan parameter material untuk melihat efeknya.
    """)

    # --- Sidebar controls ---
    st.sidebar.subheader(" Pengaturan")
    size        = st.sidebar.slider("Resolusi gambar", 256, 1024, 512, step=64)
    lx          = st.sidebar.slider("Arah Cahaya X", -1.0, 1.0, 0.4, step=0.05)
    ly          = st.sidebar.slider("Arah Cahaya Y", -1.0, 1.0, 0.4, step=0.05)
    lz          = st.sidebar.slider("Arah Cahaya Z",  0.1, 1.0, 0.8, step=0.05)
    ka          = st.sidebar.slider("Ambient (ka)",   0.0, 1.0, 0.20, step=0.01)
    kd          = st.sidebar.slider("Diffuse (kd)",   0.0, 1.0, 0.90, step=0.01)
    ks          = st.sidebar.slider("Specular (ks)",  0.0, 1.0, 0.30, step=0.01)
    shininess   = st.sidebar.slider("Shininess",      1,   200,  48,   step=1)

    uploaded = st.file_uploader("Unggah tekstur (jpg/png). Jika kosong, pakai checkerboard default.",
                                type=["jpg","jpeg","png"])

    if uploaded is not None:
        file_bytes = np.frombuffer(uploaded.read(), np.uint8)
        tex = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)  # BGR
        if tex is None:
            st.error("Gagal membaca berkas. Coba gambar lain.")
            return
    else:
        tex = make_checkerboard(512, 32)

    # Render
    shaded, base = shade_sphere(
        texture_bgr=tex,
        size=size,
        light_dir=(lx, ly, lz),
        ka=ka, kd=kd, ks=ks, shininess=int(shininess)
    )

    # Tampilkan
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Texture Map (2D)")
        st.image(cv2.cvtColor(tex, cv2.COLOR_BGR2RGB), use_container_width=True)
    with col2:
        st.subheader("Hasil: Bola Bertekstur + Shading")
        st.image(cv2.cvtColor(shaded, cv2.COLOR_BGR2RGB), use_container_width=True)

    st.markdown("""
    **Model Blinn–Phong:**
    \n\\( I = k_a I_a + k_d (N\\cdot L) I_t + k_s (N\\cdot H)^{\\alpha} I_s \\)
    \n- \\(k_a, k_d, k_s\\): koefisien ambient/diffuse/specular  
    - \\(N\\): normal, \\(L\\): arah cahaya, \\(H\\): half-vector, \\(\\alpha\\): shininess  
    - \\(I_t\\): warna dari tekstur per-pixel
    """)

if __name__ == "__main__":
    main()
