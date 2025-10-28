import streamlit as st

def render():
    st.title("Materi 5: Model Warna dan Pencahayaan")
    st.markdown("---")  # Menambahkan garis pemisah
    
    with st.container():  # Menggunakan container untuk memastikan konten terorganisir
        st.subheader("Model Warna")
        st.write("""
Model warna menjelaskan cara warna direpresentasikan secara digital.

**Contoh model warna:**
- RGB (Red, Green, Blue)
- CMY(K)
- HSV / HSL
""")

st.subheader("Model Pencahayaan")
st.markdown("""
Model pencahayaan menggambarkan bagaimana cahaya berinteraksi dengan permukaan objek.

**Jenis pencahayaan:**
- Ambient Light
- Diffuse Light
- Specular Light
""")
