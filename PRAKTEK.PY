Nilai_Tugas =int(input("masukkan Nilai Tugas : "))
Uts = int(input("masukkan nilai UTS : "))
Uas = int(input("masukkan nilai UAS : "))
KehadiranMahasiswa = int(input("masukkan nilai kehadiran : "))

nilai_akhir = (20 / 100 * Nilai_Tugas) + (30 / 100 * Uts) + (50 / 100 * Uas)


print("======HASIL======")
print("Nilai akhir =", nilai_akhir)
print (KehadiranMahasiswa,"%")

if nilai_akhir >= 85 and KehadiranMahasiswa >= 90:

    if nilai_akhir >= 85 and KehadiranMahasiswa >= 90 and nilai_akhir % 2 == 0:
        print("status      : Lulus Dengan Predikat")
    elif nilai_akhir >= 75 and KehadiranMahasiswa >= 80:
        print("status        : Lulus")
    else:
        print("status     : Belum Lulus")  