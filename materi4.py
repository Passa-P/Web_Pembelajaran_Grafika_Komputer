import streamlit as st

st.title("Materi 4: Algoritma Pengisian Poligon (Scanline & Flood Fill)")

st.subheader("1. Algoritma Scanline Fill")
st.write("""
- Mengisi poligon baris demi baris.
- Menghitung perpotongan sisi dengan garis scanline.
""")

st.subheader("2. Algoritma Flood Fill")
st.write("""
- Mengisi area berdasarkan warna awal piksel.
- Bisa menggunakan metode **rekursif** atau **stack**.
""")

st.markdown("""
**Contoh penggunaan:** aplikasi menggambar atau pewarnaan area tertutup.
""")
