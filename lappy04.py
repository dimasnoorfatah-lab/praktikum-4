
while True:
    print("\n=== Input Data Mahasiswa ===")
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai Tugas (0-100): "))
    uts = float(input("Masukkan nilai UTS (0-100): "))
    uas = float(input("Masukkan nilai UAS (0-100): "))

    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    data_mahasiswa.append({
        "Nama": nama,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Nilai Akhir": nilai_akhir
    })

    tambah = input("Tambah data lagi? (y/t): ").lower()
    if tambah == 't':
        break

print("\n=== Daftar Nilai Mahasiswa ===")
print("{:<20} {:<10} {:<10} {:<10} {:<10}".format("Nama", "Tugas", "UTS", "UAS", "Akhir"))
print("-" * 60)
for mhs in data_mahasiswa:
    print("{:<20} {:<10} {:<10} {:<10} {:<10.2f}".format(
        mhs["Nama"], mhs["Tugas"], mhs["UTS"], mhs["UAS"], mhs["Nilai Akhir"]
    ))

print("\nProgram selesai. Terima kasih!")
