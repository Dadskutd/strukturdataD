import streamlit as st
import time

st.title("Visualisasi Searching Algorithm")
st.write("Simulasi Pencarian Data")

# Inisialisasi Data
data = [10, 50, 30, 70, 80, 60, 20, 90, 40]
st.write("Data array awal:", data)

# Input User
key = st.number_input("Masukkan angka yang dicari (Key):", step=1, value=30)
algoritma = st.selectbox("Pilih Algoritma", ["Sequential Search", "Binary Search"])

if st.button("Mulai Pencarian"):
    if algoritma == "Sequential Search":
        st.subheader("Proses Sequential Search")
        found = False
        # Pencarian dari data pertama sampai akhir
        for i in range(len(data)):
            st.text(f"Mengecek indeks ke-{i} (Nilai: {data[i]})")
            time.sleep(0.3) # Memberikan jeda untuk visualisasi
            
            if data[i] == key:
                st.success(f"Pesan: Ada. Kunci {key} ditemukan pada indeks ke-{i}.")
                found = True
                break
                
        if not found:
            st.error(f"Pesan: Tidak ada. Kunci {key} tidak ditemukan.")

    elif algoritma == "Binary Search":
        st.subheader("Proses Binary Search")
        # Data harus diurutkan terlebih dahulu
        sorted_data = sorted(data)
        st.write("Data setelah diurutkan (Sorting):", sorted_data)
        
        low = 0
        high = len(sorted_data) - 1
        found = False
        
        while low <= high:
            mid = (low + high) // 2
            st.text(f"Low: {low}, High: {high} --> Mid: {mid} (Nilai Mid: {sorted_data[mid]})")
            time.sleep(0.5)
            
            if sorted_data[mid] == key:
                st.success(f"Pesan: Ada. Kunci {key} ditemukan di indeks ke-{mid} (pada array yang terurut).")
                found = True
                break
            elif sorted_data[mid] < key:
                st.info("Kunci lebih besar dari nilai Mid, pencarian di separuh data kedua.")
                low = mid + 1
            else:
                st.info("Kunci lebih kecil dari nilai Mid, pencarian di separuh data pertama.")
                high = mid - 1
                
        if not found:
            st.error(f"Pesan: Tidak ada. Kunci {key} tidak ditemukan.")