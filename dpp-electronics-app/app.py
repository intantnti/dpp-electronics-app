import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np

# Konfigurasi Halaman
st.set_page_config(page_title="Digital Product Passport", layout="wide")

st.title("♻️ Digital Product Passport (DPP) for Electronics")
st.write("Sistem Identitas Digital dan Intelijen Daur Ulang untuk Mendukung Ekonomi Sirkular")

# Sidebar untuk Pemilihan Peran (Aktor) & Navigasi
st.sidebar.header("Navigasi & Akses Pengguna")
role = st.sidebar.selectbox("Pilih Peran Aktor:", ["Konsumen / Publik", "Teknisi / Servis", "Pengelola Limbah (E-Waste)"])
menu = st.sidebar.radio("Pilih Menu:", ["Cek Paspor Produk (DPP)", "AI Deteksi Kerusakan Komponen", "Laporan & Dokumentasi Tugas"])

if menu == "Cek Paspor Produk (DPP)":
    st.subheader("🔍 Pindai / Masukkan ID Perangkat Elektronik")
    product_id = st.text_input("Nomor Seri / Product ID:", "SPK-LAPTOP-2026")
    
    if st.button("Cari Paspor"):
        # Simulasi Data Database DPP
        st.success(f"Data ditemukan untuk ID: {product_id}")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📋 Spesifikasi & Material")
            st.write("**Merek/Tipe:** EcoBook Pro 14")
            st.write("**Komposisi Material:** 50% Aluminium Daur Ulang, 30% Plastik ABS, 20% Komponen Elektronik")
            st.write("**Skor Kemudahan Daur Ulang:** 8.5 / 10")
            
        with col2:
            st.markdown("### 🛠️ Riwayat Perbaikan")
            st.write("- **Tahun ke-1:** Kondisi Prima (Pabrik)")
            st.write("- **Tahun ke-2:** Penggantian Baterai Resmi di Authorized Service Center")

        if role == "Teknisi / Servis":
            st.markdown("---")
            st.subheader("✏️ Panel Update Teknisi")
            new_service = st.text_input("Catatan Servis Baru:")
            if st.button("Simpan Perbaikan"):
                st.success("Riwayat perbaikan berhasil diperbarui ke database DPP!")

        elif role == "Pengelola Limbah (E-Waste)":
            st.markdown("---")
            st.subheader("⚠️ Panduan Akhir Masa Pakai (End-of-Life)")
            st.warning("Perhatian: Mengandung komponen B3 (Baterai Litium). Lepaskan baterai dengan hati-hati sebelum proses shredding.")

elif menu == "AI Deteksi Kerusakan Komponen":
    st.subheader("🤖 Integrasi Computer Vision untuk Analisis Komponen")
    st.write("Unggah foto komponen perangkat untuk mendeteksi tingkat keausan atau kelayakan daur ulang.")
    
    uploaded_file = st.file_uploader("Pilih foto komponen (Format: JPG/PNG)", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Foto Komponen Diunggah", use_container_width=True)
        
        if st.button("Analisis dengan AI"):
            # Simulasi hasil prediksi model AI (TensorFlow/Keras CNN)
            st.info("Memproses gambar melalui model MobileNetV2...")
            st.success("Hasil Analisis AI:")
            st.metric(label="Status Kesehatan Komponen", value="Layak Daur Ulang (82%)")
            st.write("**Rekomendasi:** Komponen PCB dapat diekstrak untuk pemulihan logam tembaga.")

elif menu == "Laporan & Dokumentasi Tugas":
    st.subheader("📄 Ringkasan 10 Komponen Tugas Kuliah")
    st.markdown("""
    1. **Identifikasi Masalah:** Krisis e-waste dan kurangnya transparansi siklus hidup perangkat.
    2. **Analisis Kebutuhan:** Sistem berbasis web dengan hak akses bertingkat dan AI.
    3. **Aktor Pengguna:** Konsumen, Teknisi, Pengelola Limbah.
    4. **Flowchart & Use Case:** Tersedia dalam dokumen rancangan sistem kelompok.
    5. **Arsitektur & Data:** Menggunakan arsitektur 3-tier dengan basis data relasional.
    6. **Integrasi AI:** Memanfaatkan *Computer Vision* untuk klasifikasi komponen.
    7. **Analisis Keberlanjutan:** Mendukung perpanjangan umur produk dan efisiensi pemulihan material *circular economy*.
    """)