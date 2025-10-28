# materi5.py
import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.header("📘 Materi 5: Model Warna dan Pencahayaan")
    st.write("""
    Pada materi ini kamu akan mempelajari:
    - Model warna **RGB, CMY, dan HSV**
    - Cara konversi antar model warna
    - Simulasi sederhana efek **pencahayaan (lighting intensity)**
    """)

    tab1, tab2, tab3 = st.tabs(["🎨 Model Warna", "🔄 Konversi Warna", "💡 Simulasi Pencahayaan"])

    # === TAB 1: MODEL WARNA ===
    with tab1:
        st.subheader("Model Warna Dasar (RGB)")

        r = st.slider("Red", 0, 255, 128)
        g = st.slider("Green", 0, 255, 128)
        b = st.slider("Blue", 0, 255, 128)

        color_rgb = np.zeros((200, 200, 3), dtype=np.uint8)
        color_rgb[:, :] = [b, g, r]  # BGR untuk OpenCV

        st.image(cv2.cvtColor(color_rgb, cv2.COLOR_BGR2RGB), caption=f"RGB({r}, {g}, {b})", use_container_width=False)

        st.markdown("""
        - **RGB (Red, Green, Blue)** digunakan untuk tampilan berbasis cahaya (monitor, kamera, TV).  
        - Kombinasi tiga komponen ini menghasilkan jutaan warna berbeda.
        """)

    # === TAB 2: KONVERSI WARNA ===
    with tab2:
        st.subheader("Konversi Antar Model Warna (RGB ↔ CMY ↔ HSV)")

        # Warna acuan
        rgb_color = np.uint8([[[r, g, b]]])
        hsv_color = cv2.cvtColor(rgb_color, cv2.COLOR_RGB2HSV)[0][0]
        cmy_color = 255 - np.array([r, g, b])

        st.write("### Nilai Konversi:")
        st.write(f"- **RGB** = ({r}, {g}, {b})")
        st.write(f"- **CMY** = ({cmy_color[0]}, {cmy_color[1]}, {cmy_color[2]})")
        st.write(f"- **HSV** = (H={hsv_color[0]}, S={hsv_color[1]}, V={hsv_color[2]})")

        # Visualisasi warna
        fig, ax = plt.subplots(1, 3, figsize=(9, 3))
        fig.suptitle("Perbandingan Model Warna")

        rgb_patch = np.ones((100, 100, 3), dtype=np.uint8) * np.array([r, g, b], dtype=np.uint8)
        cmy_patch = np.ones((100, 100, 3), dtype=np.uint8) * np.array(cmy_color, dtype=np.uint8)
        hsv_patch = np.ones((100, 100, 3), dtype=np.uint8) * np.array([[[hsv_color[0], 255, 255]]], dtype=np.uint8)
        hsv_patch = cv2.cvtColor(hsv_patch, cv2.COLOR_HSV2RGB)

        ax[0].imshow(rgb_patch)
        ax[0].set_title("RGB")
        ax[1].imshow(cmy_patch)
        ax[1].set_title("CMY")
        ax[2].imshow(hsv_patch)
        ax[2].set_title("HSV")
        for a in ax:
            a.axis("off")

        st.pyplot(fig)

        st.markdown("""
        - **CMY (Cyan, Magenta, Yellow)** digunakan untuk sistem berbasis tinta (printer).  
        - **HSV (Hue, Saturation, Value)** lebih intuitif untuk menggambarkan persepsi manusia terhadap warna.
        """)

    # === TAB 3: SIMULASI PENCAHAYAAN ===
    with tab3:
        st.subheader("Simulasi Pencahayaan (Lighting Intensity)")

        intensity = st.slider("Intensitas Cahaya (0.0 - 2.0)", 0.0, 2.0, 1.0, step=0.1)

        base_img = np.zeros((200, 200, 3), dtype=np.uint8)
        base_img[:, :] = [b, g, r]
        light_img = cv2.convertScaleAbs(base_img, alpha=intensity, beta=0)

        st.image(cv2.cvtColor(light_img, cv2.COLOR_BGR2RGB), caption=f"Intensitas: {intensity:.1f}", use_container_width=False)

        st.markdown("""
        - **α (alpha)** mengontrol *kontras / intensitas pencahayaan*  
        - Semakin tinggi nilai α → semakin terang objek  
        - Nilai < 1 → objek terlihat lebih gelap (*underexposure*)  
        """)

        st.info("💡 Coba ubah slider intensitas untuk melihat efek terang–gelap secara langsung.")
