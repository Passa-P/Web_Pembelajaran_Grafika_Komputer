import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.title("Materi 3: Algoritma Garis (Bresenham, DDA) dan Lingkaran")
    st.markdown("---")

# ========================
# Bagian Teori
# ========================

    st.subheader("Algoritma DDA (Digital Differential Analyzer)")
    st.write("""
    Algoritma DDA digunakan untuk menggambar garis antara dua titik dengan pendekatan **incremental** (menambah nilai koordinat sedikit demi sedikit).
    """)    

    st.markdown("""
    **Langkah-langkah:**
    1. Hitung Δx = x2 - x1 dan Δy = y2 - y1  
    2. Tentukan jumlah langkah = nilai maksimum antara |Δx| dan |Δy|  
    3. Tambahkan x dan y secara bertahap hingga mencapai titik akhir  

    **Kelebihan:**  
    - Mudah dipahami  
    - Dapat digunakan untuk semua jenis garis  

    **Kekurangan:**  
    - Menggunakan operasi pecahan (floating point) → kurang efisien
    """)

    st.markdown("---")

    st.subheader("Algoritma Garis Bresenham")
    st.write("""
    Bresenham lebih efisien dibanding DDA karena hanya menggunakan **operasi integer**.  
    Algoritma ini menghitung titik terdekat terhadap garis ideal berdasarkan nilai kesalahan (error).
    """)

    st.markdown("""
    **Langkah-langkah:**
    1. Tentukan titik awal (x1, y1) dan titik akhir (x2, y2)  
    2. Hitung Δx dan Δy  
    3. Gunakan variabel keputusan `p` untuk memilih pixel berikutnya  
    4. Update posisi x dan y secara iteratif  

    **Kelebihan:**  
    - Cepat dan efisien  
    - Digunakan dalam banyak aplikasi grafika (OpenGL, rasterizer)
    """)

    st.markdown("---")

    st.subheader("Algoritma Lingkaran (Midpoint Circle / Bresenham Circle)")
    st.write("""
    Digunakan untuk menggambar **lingkaran simetris** berdasarkan 8 bagian (octant).  
    Dengan hanya menghitung 1/8 bagian, titik lain didapat dari simetri.
    """)

    st.markdown("""
    **Langkah-langkah:**
    1. Tentukan titik awal (0, r)  
    2. Hitung nilai keputusan awal `d = 3 - 2r`  
    3. Gunakan iterasi hingga x ≥ y  
    4. Gambar semua 8 titik simetris untuk setiap iterasi  

    **Kelebihan:**  
    - Menghindari operasi trigonometri  
    - Cepat dan mudah diimplementasikan
    """)

    st.markdown("---")

# ========================
# Bagian Demo Interaktif
# ========================

    st.header("Demo Interaktif: DDA, Bresenham Line, dan Bresenham Circle")

# === ALGORITMA GARIS DDA ===
    def dda_line(x1, y1, x2, y2):
        points = []
        dx = x2 - x1
        dy = y2 - y1
        steps = int(max(abs(dx), abs(dy)))
        x_inc = dx / steps
        y_inc = dy / steps
        x, y = x1, y1
        for _ in range(steps + 1):
            points.append((round(x), round(y)))
            x += x_inc
            y += y_inc
        return points


# === ALGORITMA GARIS BRESENHAM ===
    def bresenham_line(x1, y1, x2, y2):
        points = []
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        x, y = x1, y1
        sx = 1 if x2 > x1 else -1
        sy = 1 if y2 > y1 else -1
        if dx > dy:
            p = 2 * dy - dx
            for _ in range(dx + 1):
                points.append((x, y))
                if p >= 0:
                    y += sy
                    p -= 2 * dx
                x += sx
                p += 2 * dy
        else:
            p = 2 * dx - dy
            for _ in range(dy + 1):
                points.append((x, y))
                if p >= 0:
                    x += sx
                    p -= 2 * dy
                y += sy
                p += 2 * dx
        return points


# === ALGORITMA LINGKARAN BRESENHAM ===
    def bresenham_circle(xc, yc, r):
        x, y = 0, r
        d = 3 - 2 * r
        points = []
        while y >= x:
            points.extend([
                (xc + x, yc + y), (xc - x, yc + y),
                (xc + x, yc - y), (xc - x, yc - y),
                (xc + y, yc + x), (xc - y, yc + x),
                (xc + y, yc - x), (xc - y, yc - x)
            ])
            if d < 0:
                d += 4 * x + 6
            else:
                d += 4 * (x - y) + 10
                y -= 1
            x += 1
        return points


# === TABS UNTUK DEMO ===
    tab1, tab2, tab3 = st.tabs(["DDA", "Bresenham Line", "Bresenham Circle"])

# === TAB 1: DDA ===
    with tab1:
        st.subheader("Algoritma Garis DDA (Digital Differential Analyzer)")
        x1 = st.number_input("x1", value=0)
        y1 = st.number_input("y1", value=0)
        x2 = st.number_input("x2", value=10)
        y2 = st.number_input("y2", value=6)

        if st.button("Gambar Garis DDA"):
            points = dda_line(x1, y1, x2, y2)
            xs, ys = zip(*points)
            fig, ax = plt.subplots()
            ax.plot(xs, ys, marker="s", color="blue")
            ax.set_title("Algoritma Garis DDA")
            ax.set_aspect("equal")
            ax.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig)

# === TAB 2: Bresenham Line ===
    with tab2:
        st.subheader("Algoritma Garis Bresenham")
        x1b = st.number_input("x1_b", value=0)
        y1b = st.number_input("y1_b", value=0)
        x2b = st.number_input("x2_b", value=10)
        y2b = st.number_input("y2_b", value=6)

        if st.button("Gambar Garis Bresenham"):
            points = bresenham_line(x1b, y1b, x2b, y2b)
            xs, ys = zip(*points)
            fig, ax = plt.subplots()
            ax.plot(xs, ys, marker="s", color="green")
            ax.set_title("Algoritma Garis Bresenham")
            ax.set_aspect("equal")
            ax.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig)

# === TAB 3: Bresenham Circle ===
    with tab3:
        st.subheader("Algoritma Lingkaran Bresenham")
        xc = st.number_input("Pusat X (xc)", value=0)
        yc = st.number_input("Pusat Y (yc)", value=0)
        r = st.number_input("Jari-jari (r)", value=10, min_value=1)

        if st.button("Gambar Lingkaran"):
            points = bresenham_circle(xc, yc, r)
            xs, ys = zip(*points)
            fig, ax = plt.subplots()
            ax.scatter(xs, ys, color="red", s=20)
            ax.set_title("Algoritma Lingkaran Bresenham")
            ax.set_aspect("equal")
            ax.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig)

    st.markdown("---")
    st.success("Kamu telah mempelajari teori dan praktik dasar dari Algoritma Garis (DDA & Bresenham) serta Lingkaran Bresenham!")
