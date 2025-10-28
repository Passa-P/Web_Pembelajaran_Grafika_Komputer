import streamlit as st

st.title("Materi 3: Algoritma Garis dan Lingkaran")

st.subheader("Algoritma DDA (Digital Differential Analyzer)")
st.code("""
Langkah-langkah:
1. Hitung dx dan dy.
2. Tentukan langkah terbesar (step).
3. Inisialisasi titik awal.
4. Tambahkan increment x dan y.
""")

st.subheader("Algoritma Bresenham")
st.code("""
Menggunakan operasi integer untuk menggambar garis yang lebih efisien.
""")

st.subheader("Algoritma Lingkaran (Midpoint Circle Algorithm)")
st.write("""
Digunakan untuk menggambar lingkaran dengan efisien berdasarkan simetri delapan arah.
""")
