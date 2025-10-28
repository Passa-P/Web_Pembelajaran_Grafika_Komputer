# materi3.py
import streamlit as st
import matplotlib.pyplot as plt

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


# === FUNGSI UTAMA UNTUK STREAMLIT ===
def main():
    st.header("📘 Materi 3: Algoritma Garis dan Lingkaran")
    st.write("""
    Di bawah ini adalah demo interaktif untuk menampilkan hasil dari:
    - Algoritma Garis **DDA**
    - Algoritma Garis **Bresenham**
    - Algoritma Lingkaran **Bresenham**
    """)

    tab1, tab2, tab3 = st.tabs(["🔹 DDA", "🔹 Bresenham Line", "🔹 Bresenham Circle"])

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
            ax.set_aspect("equal", adjustable="box")
            ax.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig)

    # === TAB 2: Bresenham Line ===
    with tab2:
        st.subheader("Algoritma Garis Bresenham")
        x1 = st.number_input("x1_b", value=0)
        y1 = st.number_input("y1_b", value=0)
        x2 = st.number_input("x2_b", value=10)
        y2 = st.number_input("y2_b", value=6)

        if st.button("Gambar Garis Bresenham"):
            points = bresenham_line(x1, y1, x2, y2)
            xs, ys = zip(*points)

            fig, ax = plt.subplots()
            ax.plot(xs, ys, marker="s", color="green")
            ax.set_title("Algoritma Garis Bresenham")
            ax.set_aspect("equal", adjustable="box")
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
            ax.set_aspect("equal", adjustable="box")
            ax.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig)
