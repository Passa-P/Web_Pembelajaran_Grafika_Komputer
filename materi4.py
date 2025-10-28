import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

def render():
    st.title("🎨 Belajar Pengisian Poligon (Polygon Filling)")
    st.markdown("---")
    st.header("🧩 Apa Itu Pengisian Poligon?")
    st.markdown("""
    Pengisian Poligon adalah proses **mengubah bentuk garis (outline)** menjadi **bentuk padat (solid)**.  
    Dalam grafika komputer, ini digunakan saat menggambar objek seperti jendela, tombol, atau model 3D.

    Ada dua pendekatan utama:
    - 🌊 **Flood Fill** (Isi Banjir)
    - 📏 **Scanline Fill** (Garis Pindai)
    """)

    mode = st.sidebar.radio("Pilih Algoritma", ["Penjelasan Teori", "Demo Flood Fill", "Demo Scanline Fill"])

    if mode == "Penjelasan Teori":
        st.write("""
        Pengisian poligon berarti memberi warna di dalam area yang dibatasi oleh garis (outline).  
        Ada dua cara populer: **Flood Fill** dan **Scanline Fill**.
        """)
        st.header("🌊 **Flood Fill** (Isi Banjir)")
        st.write("""
        Anda mulai dari satu titik (disebut seed atau benih) di dalam poligon. 
        Dari titik itu, Anda "membanjiri" area sekitarnya dengan warna baru, berhenti ketika Anda menabrak warna batas (boundary color).
        """)
        st.image("https://upload.wikimedia.org/wikipedia/commons/4/4c/Floodfill.gif", caption="Contoh Flood Fill", use_container_width=True)
        st.markdown("""
        **Kelebihan:**
        - Sederhana dan intuitif.
        - Cocok untuk gambar tak beraturan.

        **Kekurangan:**
        - Bisa *bocor* jika batas tidak tertutup sempurna.
        - Risiko *stack overflow* jika area terlalu besar.
        - Membutuhkan titik awal (seed point).
        """)
        st.subheader("📏 Scanline Fill (Garis Pindai)")
        st.write("""
        Metode profesional yang digunakan dalam **rendering engine** dan **hardware grafis**.  
        Alih-alih membanjiri dari satu titik, algoritma ini mengisi baris demi baris secara horizontal.
        """)
        st.image("https://upload.wikimedia.org/wikipedia/commons/1/12/Polygon_Scanline_Fill_Algorithm_Illustration.gif", caption="Scanline Fill", use_container_width=True)
        st.markdown("""
        **Kelebihan:**
        - Cepat dan efisien.
        - Tidak perlu titik awal.
        - Tidak ada rekursi (aman dari stack overflow).

        **Kekurangan:**
        - Implementasi lebih kompleks.
        - Harus hati-hati menangani vertex & floating point.
        """)
        st.subheader("💡 Perbandingan Singkat")
        st.table({
            "Fitur": ["Flood Fill", "Scanline Fill"],
            "Logika": ["Banjiri dari 1 titik (seed)", "Isi baris demi baris (y)"],
            "Kecepatan": ["Lambat (tergantung area)", "Sangat cepat"],
            "Kesulitan": ["Mudah", "Sulit"],
            "Kasus Umum": ["Paint Bucket", "Rendering 2D/3D"],
        })

    elif mode == "Demo Flood Fill":
        st.header("🌊 Demo Flood Fill")
        st.write("Pilih algoritma Flood Fill dan klik tombol untuk mengisi warna.")

        grid_size = st.slider("Ukuran grid:", 5, 20, 10)
        grid = np.zeros((grid_size, grid_size), dtype=int)
        grid[0, :] = 1
        grid[-1, :] = 1
        grid[:, 0] = 1
        grid[:, -1] = 1

        x = st.number_input("Titik X Seed:", min_value=1, max_value=grid_size-2, value=grid_size//2)
        y = st.number_input("Titik Y Seed:", min_value=1, max_value=grid_size-2, value=grid_size//2)

        algoritma = st.radio("Pilih Algoritma", ["Rekursif", "Iteratif (Stack)"])

        def flood_fill_rekursif(x, y, warna_isi=2, warna_batas=1):
            warna_piksel_saat_ini = grid[x, y]
            if warna_piksel_saat_ini == warna_batas or warna_piksel_saat_ini == warna_isi:
                return
            grid[x, y] = warna_isi
            flood_fill_rekursif(x+1, y, warna_isi, warna_batas)
            flood_fill_rekursif(x-1, y, warna_isi, warna_batas)
            flood_fill_rekursif(x, y+1, warna_isi, warna_batas)
            flood_fill_rekursif(x, y-1, warna_isi, warna_batas)

        def flood_fill_iteratif(x_seed, y_seed, warna_isi=2, warna_batas=1):
            stack = []
            stack.append((x_seed, y_seed))
            while stack:
                x, y = stack.pop()
                if x < 0 or x >= grid_size or y < 0 or y >= grid_size:
                    continue
                warna_piksel_saat_ini = grid[x, y]
                if warna_piksel_saat_ini != warna_batas and warna_piksel_saat_ini != warna_isi:
                    grid[x, y] = warna_isi
                    stack.append((x+1, y))
                    stack.append((x-1, y))
                    stack.append((x, y+1))
                    stack.append((x, y-1))

        if st.button("Isi Flood Fill"):
            if algoritma == "Rekursif":
                flood_fill_rekursif(int(x), int(y))
            else:
                flood_fill_iteratif(int(x), int(y))

        fig, ax = plt.subplots()
        cmap = plt.cm.get_cmap('Set1', 3)
        ax.imshow(grid, cmap=cmap, vmin=0, vmax=2)
        ax.set_xticks([])
        ax.set_yticks([])
        st.pyplot(fig)

    elif mode == "Demo Scanline Fill":
        st.header("📏 Demo Scanline Fill")
        st.write("Demo interaktif scanline fill sederhana.")

        st.markdown("""
        <b>Petunjuk:</b> Tambahkan titik poligon di bawah, lalu klik tombol untuk mengisi dengan scanline.
        """, unsafe_allow_html=True)

        grid_size = st.slider("Ukuran grid:", 10, 40, 20)
        # Buat grid kosong
        grid = np.zeros((grid_size, grid_size), dtype=int)

        # Input titik poligon
        default_points = [(5,5), (15,5), (15,15), (10,25), (5,15)]
        pts = st.text_input("Titik poligon (format: x1,y1;x2,y2;...)",
                           ";".join([f"{x},{y}" for x,y in default_points]))
        try:
            polygon = [tuple(map(int, p.split(","))) for p in pts.split(";") if p]
        except:
            st.error("Format titik salah!")
            polygon = default_points

        def scanline_fill_polygon(polygon, grid):
            if len(polygon) < 3:
                return grid
            ys = [p[1] for p in polygon]
            y_min = max(0, min(ys))
            y_max = min(grid.shape[0]-1, max(ys))
            for y in range(y_min, y_max+1):
                xs = []
                n = len(polygon)
                for i in range(n):
                    (x1, y1) = polygon[i]
                    (x2, y2) = polygon[(i+1)%n]
                    if y1 == y2:
                        continue
                    ymin = min(y1, y2)
                    ymax = max(y1, y2)
                    if y < ymin or y >= ymax:
                        continue
                    x = x1 + (y-y1)*(x2-x1)/(y2-y1)
                    xs.append(x)
                xs.sort()
                for i in range(0, len(xs)-1, 2):
                    x_start = int(round(xs[i]))
                    x_end = int(round(xs[i+1]))
                    if x_end < x_start:
                        x_start, x_end = x_end, x_start
                    grid[y, x_start:x_end+1] = 2
            return grid

        if st.button("Isi Scanline Fill"):
            grid = scanline_fill_polygon(polygon, grid)

        # Gambar poligon
        fig, ax = plt.subplots()
        ax.imshow(grid, cmap=plt.cm.get_cmap('Set1', 3), vmin=0, vmax=2)
        poly_x = [x for x, y in polygon] + [polygon[0][0]]
        poly_y = [y for x, y in polygon] + [polygon[0][1]]
        ax.plot(poly_x, poly_y, color='black', linewidth=2)
        ax.scatter(poly_x[:-1], poly_y[:-1], color='orange', s=40)
        ax.set_xticks([])
        ax.set_yticks([])
        st.pyplot(fig)