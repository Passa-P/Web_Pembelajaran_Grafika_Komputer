# materi1.py
import streamlit as st
import cv2
import numpy as np
import os

def main():
    st.header("📘 Materi 1: Pengantar Grafika Komputer (OpenCV)")

    current_dir = os.path.dirname(__file__)
    img_path = os.path.join(current_dir, "foto.jpg")
    img = cv2.imread(img_path)

    if img is None:
        st.error(f"Gambar 'foto.jpg' tidak ditemukan di folder: {current_dir}")
        return

    # === 2. Putar 180 derajat + mirror ===
    rotated = cv2.rotate(img, cv2.ROTATE_180)
    mirror_img = cv2.flip(rotated, 1)

    # === 3. RGB → Grayscale manual ===
    b, g, r = cv2.split(img)
    grayscale_manual = (0.299*r + 0.587*g + 0.114*b).astype(np.uint8)

    # === 4. RGB → Negasi ===
    negasi = 255 - img

    # === 5. Lebih cerah ===
    brightness = cv2.convertScaleAbs(img, alpha=1, beta=50)

    # === 6. Lebih kontras ===
    contrast = cv2.convertScaleAbs(img, alpha=1.5, beta=0)

    # === 7. Tampilkan hasil ===
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Gambar Asli", use_container_width=True)
    st.image(cv2.cvtColor(mirror_img, cv2.COLOR_BGR2RGB), caption="Mirror + Rotasi 180°", use_container_width=True)
    st.image(grayscale_manual, caption="Grayscale Manual", use_container_width=True)
    st.image(cv2.cvtColor(negasi, cv2.COLOR_BGR2RGB), caption="Negatif Warna", use_container_width=True)
    st.image(cv2.cvtColor(brightness, cv2.COLOR_BGR2RGB), caption="Brightness +50", use_container_width=True)
