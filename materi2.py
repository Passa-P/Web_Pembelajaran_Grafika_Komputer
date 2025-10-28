# materi2.py
import streamlit as st
import matplotlib.pyplot as plt
import math

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

def main():
    st.header("📘 Materi 2: Representasi Data Grafis & Transformasi 2D")
    st.subheader("Demo: Bintang 5 Sudut")

    r_outer = st.slider("Radius luar", 20, 100, 60)
    r_inner = st.slider("Radius dalam", 10, 50, 25)

    points = generate_star_points(0, 0, r_outer, r_inner)
    xs, ys = zip(*points)

    fig, ax = plt.subplots()
    ax.plot(xs, ys, color="blue", linewidth=2)
    ax.fill(xs, ys, color="skyblue", alpha=0.4)
    ax.scatter(xs, ys, color="red")
    ax.set_aspect("equal")
    ax.set_title("Bintang 5 Sudut (2D)")
    ax.grid(True, linestyle="--", alpha=0.4)

    st.pyplot(fig)
