beli = int (input("berapa kg anda membeli mangga:"))
if beli <= 2:
  harga = 20_000
elif beli <= 5:
  harga = 18_000  
elif beli  >= 5:
  harga = 16_000   
else:
  harga =0
hasil = beli * harga

print ("harga yang harus anda bayar untuk membeli %i kg mangga adalah %i" % (beli,hasil))