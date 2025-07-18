# Kalkulator Logika Proposisi - UAS Logika Informatika

Repositori ini berisi kode sumber untuk aplikasi web interaktif yang berfungsi sebagai kalkulator tabel kebenaran. Aplikasi ini dibangun untuk memenuhi tugas Ujian Akhir Semester (UAS) mata kuliah Logika Informatika.

## 👤 Identitas Mahasiswa

* **Nama**: Arfianda Firsta Satritama
* **NIM**: 312410377
* **Kelas**: TI 24 A3
* **Mata Kuliah**: Logika Informatika
* **Dosen Pengampu**: Muhammad Najamuddin Dwi Miharja, S.Kom, M.Kom.
* **Universitas**: Universitas Pelita Bangsa

## 📝 Deskripsi Proyek

Kalkulator Logika Proposisi adalah sebuah alat bantu berbasis web yang dirancang untuk mempermudah mahasiswa dan siapa pun yang mempelajari logika dalam menganalisis ekspresi logika. Pengguna dapat memasukkan ekspresi logika, dan aplikasi akan secara otomatis:
1.  Menghasilkan tabel kebenaran lengkap.
2.  Menganalisis apakah hasil dari ekspresi tersebut merupakan **Tautologi**, **Kontradiksi**, atau **Kontingensi**.

Aplikasi ini mengambil contoh studi kasus dari sebuah berita untuk menunjukkan penerapan praktis dari analisis logika dalam memahami argumen di dunia nyata.

## ✨ Fitur Utama

* **Tabel Kebenaran Otomatis**: Menghasilkan tabel kebenaran untuk ekspresi logika apa pun dengan proposisi yang valid.
* **Analisis Hasil Instan**: Secara otomatis menentukan apakah suatu ekspresi adalah tautologi, kontradiksi, atau kontingensi.
* **Antarmuka Interaktif**: UI yang bersih dan mudah digunakan dibangun dengan Streamlit, memungkinkan input yang mudah dan visualisasi hasil yang jelas.
* **Dukungan Operator Logika**: Mendukung operator logika umum, termasuk:
    * `∧` (Konjungsi / DAN)
    * `∨` (Disjungsi / ATAU)
    * `¬` (Negasi / TIDAK)
    * `→` (Implikasi)
    * `↔` (Bi-implikasi)
* **Error Handling**: Memberikan peringatan jika input atau format ekspresi tidak valid.

## 🛠️ Teknologi yang Digunakan

* **Bahasa Pemrograman**: Python 3
* **Framework Web**: Streamlit
* **Library**: Pandas (untuk manajemen dan tampilan tabel kebenaran)

## 🚀 Setup dan Instalasi

Untuk menjalankan aplikasi ini di komputer lokal Anda, ikuti langkah-langkah berikut:

**1. Clone atau Unduh Repositori**
```bash
git clone [URL_REPOSITORY_ANDA]
# atau unduh ZIP dan ekstrak
