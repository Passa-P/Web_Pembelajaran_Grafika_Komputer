import streamlit as st

st.title("Materi 6: Teknik Shading (Flat, Gouraud, Phong)")

st.subheader("1. Flat Shading")
st.write("""
- Setiap poligon diberi satu warna rata.
- Cepat namun tampak tidak halus.
""")

st.subheader("2. Gouraud Shading")
st.write("""
- Warna dihitung di tiap vertex lalu diinterpolasi antar titik.
- Lebih halus dibanding Flat Shading.
""")

st.subheader("3. Phong Shading")
st.write("""
- Normal dihitung di setiap piksel.
- Hasil paling realistis dan halus, tetapi paling berat dihitung.
""")
