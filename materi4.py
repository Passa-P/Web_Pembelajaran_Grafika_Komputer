# materi4.py
import streamlit as st
import subprocess
import os

def main():
    st.title("Materi 4: Algoritma Pengisian Poligon")

    st.header("Pengantar Pengisian Poligon")
    st.write("""
    **Algoritma Pengisian Poligon (Polygon Filling)** adalah metode dalam grafika komputer
    untuk mewarnai area tertutup yang dibentuk oleh garis atau sisi poligon.  
    Tujuannya adalah untuk memberikan tampilan solid pada bentuk, bukan hanya kerangkanya saja.

    Beberapa teknik umum yang digunakan:
    - **Flood Fill** → Mengisi area berdasarkan warna awal (misalnya pada Paint).
    - **Boundary Fill** → Mengisi area sampai batas (garis tepi).
    - **Scanline Fill** → Menggunakan baris horizontal untuk menentukan area yang akan diisi.

    Contoh penggunaan:
    - Rendering bentuk 2D di game atau simulasi.
    - Mewarnai area tertutup dalam desain CAD.
    - Menampilkan objek solid pada grafik vektor.
    """)

    st.header("Contoh Implementasi: Menggambar Rumah dengan Turtle")
    st.write("""
    Pada contoh ini, kita menggunakan **Python Turtle Graphics**
    untuk menggambar rumah berwarna yang terdiri dari dinding, atap, dan pintu.
    """)

    # --- tampilkan kode contoh
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

    st.info("Klik tombol di bawah untuk menjalankan demo Turtle di jendela terpisah.")

    # --- tombol jalankan demo turtle
    if st.button("Jalankan Demo Turtle"):
        file_path = os.path.join(os.getcwd(), "turtle_demo.py")

        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(turtle_house_code())

        subprocess.Popen(["python", file_path], shell=True)
        st.success("Demo Turtle sedang dijalankan di jendela terpisah!")

    st.header("Kesimpulan")
    st.write("""
    Dengan algoritma pengisian poligon, grafika komputer dapat menampilkan bentuk 2D yang tampak **solid dan realistis**.
    Teknik ini menjadi dasar bagi rendering 3D dan efek visual modern.
    """)


def turtle_house_code():
    """Isi otomatis untuk file turtle_demo.py"""
    return '''import turtle

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

if __name__ == "__main__":
    main()
'''

# Jalankan fungsi utama Streamlit
if __name__ == "__main__":
    main()
