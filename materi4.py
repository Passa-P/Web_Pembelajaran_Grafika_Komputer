# materi4.py
import streamlit as st        # Import library Streamlit untuk membuat tampilan web interaktif
import subprocess              # Untuk menjalankan perintah sistem (misalnya membuka program lain)
import os                      # Untuk mengatur file dan path (lokasi file)

def main():
    # Judul halaman dan deskripsi singkat
    st.header("🐢 Materi 4: Algoritma Pengisian Poligon (Turtle Demo)")
    st.write("""
    Demo ini menggunakan **Python Turtle Graphics** untuk menggambar bentuk berwarna
    sebagai contoh **pengisian poligon (area fill)**.

    Karena Turtle menggunakan GUI sendiri (Tkinter), maka demo dijalankan **di luar Streamlit**.
    """)

    # Menampilkan kode contoh di halaman Streamlit
    st.code("""
import turtle

def draw_filled_polygon(t, points, color):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for x, y in points[1:]:
        t.goto(x, y)
    t.goto(points[0])
    t.end_fill()

def main():
    screen = turtle.Screen()
    screen.title("Turtle Demo - Gambar Rumah")
    screen.bgcolor("lightblue")

    t = turtle.Turtle()
    t.speed(8)

    # Dinding rumah
    wall = [(-100, -100), (100, -100), (100, 100), (-100, 100)]
    draw_filled_polygon(t, wall, "#ffcc66")

    # Atap rumah
    roof = [(-120, 100), (0, 220), (120, 100)]
    draw_filled_polygon(t, roof, "#cc3333")

    # Pintu
    door = [(-30, -100), (-30, 20), (30, 20), (30, -100)]
    draw_filled_polygon(t, door, "#663300")

    t.hideturtle()
    turtle.done()
    """, language="python")

    # Menampilkan catatan kepada pengguna
    st.info("⚠️ Klik tombol di bawah untuk menjalankan demo Turtle di jendela terpisah.")

    # Jika tombol diklik, maka jalankan kode turtle di luar Streamlit
    if st.button("🎨 Jalankan Demo Turtle"):
        file_path = os.path.join(os.getcwd(), "turtle_demo.py")  # Lokasi file turtle_demo.py

        # Jika file belum ada, maka dibuat otomatis
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(turtle_house_code())  # Menulis isi file dari fungsi turtle_house_code()

        # Menjalankan file turtle_demo.py dengan Python secara terpisah
        subprocess.Popen(["python", file_path], shell=True)
        st.success("🟢 Demo Turtle sedang dijalankan di jendela terpisah!")

def turtle_house_code():
    """Fungsi ini mengembalikan isi dari file turtle_demo.py sebagai teks."""
    return '''import turtle

def draw_filled_polygon(t, points, color):
    # Fungsi untuk menggambar poligon (bentuk tertutup) yang diwarnai
    # t      : objek turtle
    # points : daftar titik (koordinat x, y)
    # color  : warna isi poligon
    t.penup()                # Angkat pena agar tidak menggambar saat berpindah
    t.goto(points[0])        # Pindah ke titik pertama
    t.pendown()              # Turunkan pena untuk mulai menggambar
    t.fillcolor(color)       # Tentukan warna isi
    t.begin_fill()           # Mulai proses pengisian warna
    for x, y in points[1:]:  # Ulangi untuk semua titik berikutnya
        t.goto(x, y)
    t.goto(points[0])        # Kembali ke titik awal agar bentuk tertutup
    t.end_fill()             # Selesaikan proses pengisian warna

def main():
    # Buat layar (window) untuk menggambar
    screen = turtle.Screen()
    screen.title("Turtle Demo - Gambar Rumah")  # Judul jendela
    screen.bgcolor("lightblue")                  # Warna latar belakang

    t = turtle.Turtle()      # Buat objek turtle
    t.speed(8)               # Atur kecepatan menggambar

    # Dinding rumah (bentuk persegi)
    wall = [(-100, -100), (100, -100), (100, 100), (-100, 100)]
    draw_filled_polygon(t, wall, "#ffcc66")  # Warna krem untuk dinding

    # Atap rumah (bentuk segitiga)
    roof = [(-120, 100), (0, 220), (120, 100)]
    draw_filled_polygon(t, roof, "#cc3333")  # Warna merah bata untuk atap

    # Pintu rumah (bentuk persegi panjang)
    door = [(-30, -100), (-30, 20), (30, 20), (30, -100)]
    draw_filled_polygon(t, door, "#663300")  # Warna coklat untuk pintu

    t.hideturtle()     # Sembunyikan ikon turtle setelah menggambar
    turtle.done()      # Pertahankan jendela tetap terbuka

# Pastikan program dijalankan hanya jika file ini dieksekusi langsung
if __name__ == "__main__":
    main()
'''
