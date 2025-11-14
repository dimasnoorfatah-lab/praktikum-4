# flowchart
![Image](https://github.com/user-attachments/assets/8d4c885b-4e53-48a9-8895-79fe377ce481)

## Cara Kerja Program 
1. Inisialisasi Data
Sebelum loop dimulai, sebuah list kosong bernama data_mahasiswa harus didefinisikan (meskipun tidak ada di potongan kode yang diberikan, ini adalah asumsi yang diperlukan agar kode berjalan):

      data_mahasiswa = []

    List ini berfungsi sebagai container untuk menyimpan semua data nilai mahasiswa yang diinpuT

2. Input Data Mahasiswa (Loop Utama)

    while True:
    print("\n=== Input Data Mahasiswa ===")
     ... (proses input) ...
    
     ... (proses perhitungan) ...
    
     ... (penyimpanan data) ...
    
    tambah = input("Tambah data lagi? (y/t): ").lower()
    if tambah == 't':
        break

   Program menggunakan loop while True untuk memungkinkan pengguna memasukkan data mahasiswa secara berulang.

Di setiap iterasi, pengguna diminta untuk memasukkan Nama dan nilai Tugas, UTS (Ujian Tengah Semester), dan UAS (Ujian Akhir Semester).

Nilai tugas, UTS, dan UAS diubah menjadi tipe data float untuk memungkinkan perhitungan.

Loop akan berhenti jika pengguna menginput t (tidak) saat ditanya "Tambah data lagi? (y/t):".

3. Perhitungan Nilai Akhir
Nilai Akhir (NA) dihitung menggunakan bobot persentase tertentu:

nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

4. Penyimpanan Data
Setelah perhitungan, data mahasiswa (Nama, nilai-nilai individual, dan Nilai Akhir) disimpan sebagai sebuah dictionary baru, yang kemudian ditambahkan (append) ke dalam list data_mahasiswa.

5. Menampilkan Daftar Nilai Mahasiswa

   print("\n=== Daftar Nilai Mahasiswa ===")
 ... (Header tabel) ...
for mhs in data_mahasiswa:
     ... (Cetak baris data) ...

    Setelah loop input selesai, program akan mencetak tabel daftar nilai dari semua data yang telah dimasukkan.

Fungsi print() menggunakan string formatting ({:<20}) untuk memastikan output tabel menjadi rapi dan kolom-kolom sejajar.

Nilai Akhir ditampilkan dengan dua angka di belakang koma ({:<10.2f}).

