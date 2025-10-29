import streamlit as st
import matplotlib.pyplot as plt
import math

def main():
    st.title("Materi 2: Representasi Data Grafis & Transformasi 2D")
    st.markdown("---")

# ======================
# Bagian Teori
# ======================

    st.subheader("Representasi Data Grafis")
    st.write("""
    Representasi data grafis adalah **cara penyimpanan dan penggambaran objek visual** dalam bentuk data numerik atau matematis.
    Tiap objek 2D atau 3D diwakili oleh sekumpulan titik, garis, dan bidang.
    """)

    st.markdown("""
    #### Jenis Representasi:
    1. **Raster Graphics**  
    - Disusun dari kumpulan pixel (titik kecil).  
    - Contoh: foto digital, citra bitmap.  
    - Cocok untuk gambar kompleks tapi sulit diskalakan.

    2. **Vector Graphics**  
    - Disusun dari garis, kurva, dan bentuk matematis.  
    - Cocok untuk desain, logo, dan ilustrasi karena bisa diperbesar tanpa kehilangan kualitas.
    """)

    st.markdown("---")

    st.subheader("Transformasi 2D")
    st.write("""
    Transformasi digunakan untuk **mengubah posisi, orientasi, atau ukuran objek 2D** di bidang koordinat.  
    Beberapa transformasi dasar:
    """)

    st.markdown("""
    - **Translasi (Pergeseran):** memindahkan posisi objek.  
    Rumus:  
    \\[
    x' = x + t_x, \\quad y' = y + t_y
    \\]

    - **Rotasi (Perputaran):** memutar objek terhadap titik asal.  
    \\[
    x' = x\\cos(θ) - y\\sin(θ), \\quad y' = x\\sin(θ) + y\\cos(θ)
    \\]

    - **Skala (Perbesaran):** mengubah ukuran objek.  
    \\[
    x' = S_x \\cdot x, \\quad y' = S_y \\cdot y
    \\]

    - **Shearing (Kemiringan):** mengubah bentuk tanpa mengubah ukuran.  
    \\[
    x' = x + Sh_x \\cdot y, \\quad y' = y + Sh_y \\cdot x
    \\]
    """)

    st.markdown("---")

# ======================
# Bagian Demo Interaktif
# ======================

    st.header("Demo: Pembuatan Bentuk Bintang 5 Sudut (2D)")
    st.write("""
    Berikut contoh sederhana pembuatan bentuk **bintang 5 sudut** menggunakan representasi koordinat titik (x, y).
    Gunakan slider untuk mengubah ukuran radius luar dan dalam.
    """)

    def generate_star_points(xc, yc, r_outer, r_inner, n=5):
        """Buat koordinat bintang"""
        points = []
        angle = math.pi / n
        for i in range(2 * n):
            r = r_outer if i % 2 == 0 else r_inner
            theta = i * angle - math.pi / 2
            x = xc + r * math.cos(theta)
            y = yc + r * math.sin(theta)
            points.append((x, y))
        points.append(points[0])
        return points

# Slider kontrol
    r_outer = st.slider("Radius luar (r_outer)", 20, 100, 60)
    r_inner = st.slider("Radius dalam (r_inner)", 10, 50, 25)

# Generate bentuk
    points = generate_star_points(0, 0, r_outer, r_inner)
    xs, ys = zip(*points)

# Gambar dengan matplotlib
    fig, ax = plt.subplots()
    ax.plot(xs, ys, color="blue", linewidth=2)
    ax.fill(xs, ys, color="skyblue", alpha=0.4)
    ax.scatter(xs, ys, color="red")
    ax.set_aspect("equal")
    ax.set_title("Bintang 5 Sudut (Representasi Titik 2D)")
    ax.grid(True, linestyle="--", alpha=0.4)

    st.pyplot(fig)

    st.markdown("---")
    st.success("Kamu telah mempelajari teori dan praktik dasar Representasi Data Grafis & Transformasi 2D!")
