umur = int (input("Masukan umur: "))
if umur <=2:
    Dipanggil = "Bayi"
elif umur <=5:
    Dipanggil = "Balita"
elif umur <=12:
    Dipanggil = "Anak Anak"
elif umur <=17:
    Dipanggil = "Remaja"
elif umur >17 and umur <=30:
    Dipanggil ="Dewasa"
elif umur >30 :
    Dipanggil = "Orang tua"

print("dipanggil: ",Dipanggil) 
    