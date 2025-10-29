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
    - Simulasi interaktif **pencahayaan dan suhu warna cahaya**
    """)

    tab1, tab2, tab3, tab4 = st.tabs([
        "🎨 Model Warna RGB",
        "🔄 Konversi Warna",
        "🌈 Interaktif CMY & HSV",
        "💡 Simulasi Pencahayaan"
    ])

    # === TAB 1: MODEL WARNA ===
    with tab1:
        st.subheader("Model Warna Dasar (RGB)")

        r = st.slider("Red", 0, 255, 128)
        g = st.slider("Green", 0, 255, 128)
        b = st.slider("Blue", 0, 255, 128)

        color_rgb = np.zeros((200, 200, 3), dtype=np.uint8)
        color_rgb[:, :] = [b, g, r]  # BGR untuk OpenCV
        st.image(cv2.cvtColor(color_rgb, cv2.COLOR_BGR2RGB),
                 caption=f"RGB({r}, {g}, {b})", use_container_width=False)

        st.markdown("""
        - **RGB (Red, Green, Blue)** digunakan untuk tampilan berbasis cahaya (monitor, kamera, TV).  
        - Kombinasi ketiganya menghasilkan jutaan warna berbeda.
        """)

    # === TAB 2: KONVERSI WARNA ===
    with tab2:
        st.subheader("Konversi Antar Model Warna (RGB ↔ CMY ↔ HSV)")

        rgb_color = np.uint8([[[r, g, b]]])
        hsv_color = cv2.cvtColor(rgb_color, cv2.COLOR_RGB2HSV)[0][0]
        cmy_color = 255 - np.array([r, g, b])

        st.write("### Nilai Konversi:")
        st.write(f"- **RGB** = ({r}, {g}, {b})")
        st.write(f"- **CMY** = ({cmy_color[0]}, {cmy_color[1]}, {cmy_color[2]})")
        st.write(f"- **HSV** = (H={hsv_color[0]}, S={hsv_color[1]}, V={hsv_color[2]})")

        fig, ax = plt.subplots(1, 3, figsize=(9, 3))
        fig.suptitle("Perbandingan Model Warna")

        rgb_patch = np.ones((100, 100, 3), dtype=np.uint8) * np.array([r, g, b])
        cmy_patch = np.ones((100, 100, 3), dtype=np.uint8) * np.array(cmy_color)
        hsv_patch = np.ones((100, 100, 3), dtype=np.uint8)
        hsv_patch[:] = [hsv_color[0], 255, 255]
        hsv_patch = cv2.cvtColor(hsv_patch.astype(np.uint8), cv2.COLOR_HSV2RGB)

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
        - **HSV (Hue, Saturation, Value)** lebih intuitif untuk persepsi manusia terhadap warna.
        """)

    # === TAB 3: DEMONSTRASI INTERAKTIF CMY & HSV ===
    with tab3:
        st.subheader("Eksperimen Interaktif: CMY & HSV")

        mode = st.radio("Pilih Model Warna:", ["CMY", "HSV"], horizontal=True)

        if mode == "CMY":
            c = st.slider("Cyan", 0, 255, 128)
            m = st.slider("Magenta", 0, 255, 128)
            y = st.slider("Yellow", 0, 255, 128)

            rgb_from_cmy = 255 - np.array([c, m, y])
            color_cmy = np.zeros((200, 200, 3), dtype=np.uint8)
            color_cmy[:, :] = rgb_from_cmy[::-1]  # urutan BGR
            st.image(cv2.cvtColor(color_cmy, cv2.COLOR_BGR2RGB),
                     caption=f"CMY({c}, {m}, {y}) → RGB{tuple(rgb_from_cmy)}", use_container_width=False)

            st.info("💡 CMY merupakan kebalikan dari RGB. Semakin besar nilai C, M, Y → semakin sedikit cahaya warna aslinya.")

        else:  # HSV mode
            h = st.slider("Hue", 0, 179, 90)
            s = st.slider("Saturation", 0, 255, 255)
            v = st.slider("Value (Brightness)", 0, 255, 255)

            hsv_color = np.uint8([[[h, s, v]]])
            rgb_from_hsv = cv2.cvtColor(hsv_color, cv2.COLOR_HSV2RGB)[0][0]

            color_hsv = np.zeros((200, 200, 3), dtype=np.uint8)
            color_hsv[:, :] = rgb_from_hsv[::-1]
            st.image(cv2.cvtColor(color_hsv, cv2.COLOR_BGR2RGB),
                     caption=f"HSV({h}, {s}, {v}) → RGB{tuple(rgb_from_hsv)}", use_container_width=False)

            st.info("🎨 Hue mengatur rona warna, Saturation mengatur kejenuhan, dan Value mengatur kecerahan.")

    # === TAB 4: SIMULASI PENCAHAYAAN ===
    with tab4:
        st.subheader("Simulasi Pencahayaan (Lighting & Temperature)")

        intensity = st.slider("Intensitas Cahaya (0.0 - 2.0)", 0.0, 2.0, 1.0, step=0.1)
        temperature = st.slider("Suhu Warna Cahaya (K)", 2000, 10000, 6500, step=500)
        ambient = st.slider("Tingkat Cahaya Lingkungan (0-1)", 0.0, 1.0, 0.3, step=0.05)

        base_color = np.array([r, g, b], dtype=np.float32)

        # Fungsi suhu ke RGB (approx.)
        def kelvin_to_rgb(temp):
            t = temp / 100
            if t <= 66:
                r_c = 255
                g_c = np.clip(99.47 * np.log(t) - 161.12, 0, 255)
                b_c = 0 if t <= 19 else np.clip(138.52 * np.log(t - 10) - 305.04, 0, 255)
            else:
                r_c = np.clip(329.7 * (t - 60) ** -0.133, 0, 255)
                g_c = np.clip(288.12 * (t - 60) ** -0.0755, 0, 255)
                b_c = 255
            return np.array([r_c, g_c, b_c])

        light_color = kelvin_to_rgb(temperature)
        mixed = np.clip(base_color * intensity + ambient * light_color * 0.2, 0, 255).astype(np.uint8)

        light_img = np.ones((200, 200, 3), dtype=np.uint8)
        light_img[:, :] = mixed

        st.image(cv2.cvtColor(light_img, cv2.COLOR_BGR2RGB),
                 caption=f"Cahaya: {temperature}K | Intensitas: {intensity:.1f} | Ambient: {ambient:.2f}",
                 use_container_width=False)

        st.info("💡 Ubah slider untuk melihat bagaimana suhu warna dan intensitas cahaya memengaruhi hasil warna.")

if __name__ == "__main__":
    main()
