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

if __name__ == "__main__":
    main()
