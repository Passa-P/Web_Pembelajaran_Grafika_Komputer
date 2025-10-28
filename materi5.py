import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def render():
    st.title("🎨 Model Warna dan Model Pencahayaan (Color & Lighting Models)")

    st.markdown("""
    ## 🧩 Konsep Dasar: Apa Itu Model Warna?
    Model Warna adalah sistem **matematis** untuk merepresentasikan warna.  
    Sama seperti koordinat $(x, y, z)$ untuk posisi dalam ruang, warna didefinisikan oleh koordinat seperti $(R, G, B)$.
    """)

    st.info("🔍 Pilih bagian di bawah untuk mempelajari setiap model atau mencoba demo interaktif.")

    pilihan = st.radio("Pilih Pembahasan:", [
        "Model RGB (Additive)",
        "Model CMYK (Subtractive)",
        "Model HSV (Perseptual)",
        "Simulasi Interaktif Model Warna",
        "Model Pencahayaan (Lighting Models)",
        "Simulasi Model Phong"
    ])

    # ========== BAGIAN 1: RGB ==========
    if pilihan == "Model RGB (Additive)":
        st.header("🌈 Model RGB (Red, Green, Blue)")
        st.markdown("""
        - **Tipe:** Additive (penjumlahan cahaya).  
        - **Konsep:** Dimulai dari hitam → menambahkan cahaya merah, hijau, dan biru.
        
        | Kombinasi | Warna Hasil |
        |------------|-------------|
        | R penuh | Merah |
        | G penuh | Hijau |
        | B penuh | Biru |
        | R+G | Kuning |
        | G+B | Cyan |
        | R+B | Magenta |
        | R+G+B | Putih |

        📺 **Penerapan:** Layar komputer, kamera digital, desain web.
        """)

        # Demo RGB cube
        st.subheader("🔧 Eksperimen Warna RGB")
        r = st.slider("Merah (R)", 0, 255, 128)
        g = st.slider("Hijau (G)", 0, 255, 128)
        b = st.slider("Biru (B)", 0, 255, 128)

        rgb_color = f"rgb({r}, {g}, {b})"
        st.markdown(f"""
        Warna hasil kombinasi:
        <div style='width:200px;height:100px;background:{rgb_color};border-radius:10px;'></div>
        <p>Nilai RGB: ({r}, {g}, {b})</p>
        """, unsafe_allow_html=True)

    # ========== BAGIAN 2: CMYK ==========
    elif pilihan == "Model CMYK (Subtractive)":
        st.header("🖨️ Model CMYK (Cyan, Magenta, Yellow, Key/Black)")
        st.markdown("""
        - **Tipe:** Subtractive (pengurangan cahaya).
        - **Konsep:** Dimulai dari putih → tinta menyerap sebagian cahaya.
        - **Digunakan pada:** Printer, percetakan, buku, majalah.

        ⚫ Mengapa ada huruf **K (Key/Black)?**
        - Warna hitam murni tidak bisa diperoleh sempurna dari campuran C+M+Y.
        - Jadi tinta hitam ditambahkan agar teks dan bayangan lebih tajam.
        """)

        c = st.slider("Cyan (C)", 0.0, 1.0, 0.2)
        m = st.slider("Magenta (M)", 0.0, 1.0, 0.2)
        y = st.slider("Yellow (Y)", 0.0, 1.0, 0.2)
        k = st.slider("Black (K)", 0.0, 1.0, 0.0)

        r = 255 * (1 - c) * (1 - k)
        g = 255 * (1 - m) * (1 - k)
        b = 255 * (1 - y) * (1 - k)

        st.markdown(f"""
        Warna hasil konversi:
        <div style='width:200px;height:100px;background:rgb({r:.0f},{g:.0f},{b:.0f});border-radius:10px;'></div>
        <p>RGB ≈ ({r:.0f}, {g:.0f}, {b:.0f})</p>
        """, unsafe_allow_html=True)

    # ========== BAGIAN 3: HSV ==========
    elif pilihan == "Model HSV (Perseptual)":
        st.header("🎨 Model HSV (Hue, Saturation, Value)")
        st.markdown("""
        - **Hue (H):** Jenis warna (0°-360°).  
        - **Saturation (S):** Seberapa pekat warnanya (0-100%).  
        - **Value (V):** Seberapa terang warnanya (0-100%).  
        """)

        h = st.slider("Hue (0°–360°)", 0, 360, 180)
        s = st.slider("Saturation (%)", 0, 100, 100)
        v = st.slider("Value/Brightness (%)", 0, 100, 100)

        import colorsys
        rgb = colorsys.hsv_to_rgb(h/360, s/100, v/100)
        rgb_scaled = tuple(int(x * 255) for x in rgb)

        st.markdown(f"""
        Warna hasil:
        <div style='width:200px;height:100px;background:rgb{rgb_scaled};border-radius:10px;'></div>
        <p>RGB ≈ {rgb_scaled}</p>
        """, unsafe_allow_html=True)

    # ========== BAGIAN 4: MODEL PENGCAHAYAAN ==========
    elif pilihan == "Model Pencahayaan (Lighting Models)":
        st.header("💡 Model Pencahayaan: Phong Reflection Model")
        st.markdown(r"""
        Warna akhir dari sebuah piksel dihitung dengan:
        $$ I_{final} = I_{ambient} + I_{diffuse} + I_{specular} $$

        ### Komponen:
        - **Ambient:** Cahaya latar yang menyebar di seluruh ruang.  
          \( I_{ambient} = K_a \cdot I_a \)
        - **Diffuse:** Pantulan dari permukaan matte.  
          \( I_{diffuse} = K_d \cdot I_L \cdot (\hat{L} \cdot \hat{N}) \)
        - **Specular:** Pantulan mengkilap (highlight).  
          \( I_{specular} = K_s \cdot I_L \cdot (\hat{R} \cdot \hat{V})^n \)
        """)

        st.success("Model ini digunakan di OpenGL, Blender, Unity, dan banyak mesin grafis lainnya.")

    # ========== BAGIAN 5: SIMULASI PHONG ==========
    elif pilihan == "Simulasi Model Phong":
        st.header("💎 Simulasi Interaktif Phong Lighting")

        Ka = st.slider("Koefisien Ambient (Ka)", 0.0, 1.0, 0.2)
        Kd = st.slider("Koefisien Diffuse (Kd)", 0.0, 1.0, 0.7)
        Ks = st.slider("Koefisien Specular (Ks)", 0.0, 1.0, 0.5)
        n = st.slider("Shininess (n)", 1, 200, 50)

        angle = st.slider("Sudut datang cahaya (°)", 0, 180, 45)
        LdotN = max(0, np.cos(np.radians(angle)))

        I_ambient = Ka * 0.2
        I_diffuse = Kd * LdotN
        I_specular = Ks * (LdotN ** n)
        I_final = I_ambient + I_diffuse + I_specular

        st.markdown(f"""
        **Intensitas Cahaya Akhir:**
        - Ambient = {I_ambient:.3f}
        - Diffuse = {I_diffuse:.3f}
        - Specular = {I_specular:.3f}
        - Total = **{I_final:.3f}**
        """)

        # Visualisasi gradient cahaya
        fig, ax = plt.subplots(figsize=(4, 1))
        ax.imshow([[I_ambient, I_diffuse, I_specular, I_final]], cmap='inferno', extent=[0,4,0,1])
        ax.set_xticks([0.5,1.5,2.5,3.5])
        ax.set_xticklabels(["Ambient", "Diffuse", "Specular", "Final"])
        ax.set_yticks([])
        st.pyplot(fig)

    else:
        st.warning("Pilih topik untuk mulai belajar.")

# Untuk pengujian langsung
if __name__ == "__main__":
    render()
