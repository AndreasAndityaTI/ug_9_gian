# Gaji Partime
# itung-itungannya
#===============================

gaji = int(input("gaji perjam = "))
jam_kerja = int(input("jam kerja dalam satu minggu = "))

#selama 5 minggu
gaji_total = gaji * jam_kerja * 5
print("Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak = ",gaji_total)

pajak = 0.14
gaji_potong_pajak = gaji_total - (gaji_total * pajak)
print("Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak  = ",gaji_potong_pajak)

belanja = gaji_potong_pajak * 0.1
print("Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris = ",belanja)

alat_tulis = gaji_potong_pajak * 0.01
print("Jumlah uang yang akan Budi habiskan untuk membeli alat tulis = ",alat_tulis)

sisa_gaji = gaji_potong_pajak - belanja - alat_tulis
print ("sisa gaji", sisa_gaji)

sedekah = (sisa_gaji*0.25)
print("Jumlah uang yang akan Budi sedekahkan ", sedekah)

#tiap 1000 jatah anak yatim 30% duafa 70%
anakyatim = 1000*0.3
duafa = 1000*0.7

jatah_anak_yatim = ((sedekah//1000)*anakyatim)
jatah_duafa = ((sedekah//1000)*duafa)

print("Jumlah uang yang akan diterima anak yatim ", jatah_anak_yatim)
print("Jumlah uang yang akan diterima kaum dhuafa ", jatah_duafa)
