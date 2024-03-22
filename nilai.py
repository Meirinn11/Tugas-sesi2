nilai_inggis = int(input("Masukkan nilai bahasa Inggris Anda: "))
nilai_mtk = int(input("Masukkan nilai matematika Anda: "))
nilai_indonesia = int(input("Masukkan nilai bahasa Indonesia Anda: "))
nilai_ipa = int(input("Masukkan nilai IPA Anda: "))
nilai_ips = int(input("Masukkan nilai IPS Anda: "))

rata_rata_semua = (nilai_inggis + nilai_mtk + nilai_indonesia + nilai_ipa + nilai_ips) / 5
rata_rata_tiga_mapel = (nilai_inggis + nilai_mtk + nilai_indonesia) / 3
rata_rata_dua_mapel =(nilai_inggis + nilai_mtk ) / 2

if rata_rata_tiga_mapel >= 75:
    hasil = "lulus"
elif rata_rata_semua >= 70:
    hasil = "lulus"
elif rata_rata_dua_mapel >90:
    hasil = "lulus"
else:
    hasil = "tidak lulus"

print(hasil)
