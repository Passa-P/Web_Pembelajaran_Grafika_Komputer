# materi4.py
import streamlit as st
import subprocess
import os

def main():
    st.header("🐢 Materi 4: Algoritma Pengisian Poligon (Turtle Demo)")
    st.write("""
    Demo ini menggunakan **Python Turtle Graphics** untuk menggambar bentuk berwarna
    sebagai contoh **pengisian poligon (area fill)**.

    Karena Turtle menggunakan GUI sendiri (Tkinter), maka demo dijalankan **di luar Streamlit**.
    """)

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

    st.info("⚠️ Klik tombol di bawah untuk menjalankan demo Turtle di jendela terpisah.")

    if st.button("🎨 Jalankan Demo Turtle"):
        file_path = os.path.join(os.getcwd(), "turtle_demo.py")

        # Cek kalau file belum ada, buat otomatis
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(turtle_house_code())

        subprocess.Popen(["python", file_path], shell=True)
        st.success("🟢 Demo Turtle sedang dijalankan di jendela terpisah!")

def turtle_house_code():
    """Isi file turtle_demo.py otomatis."""
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
