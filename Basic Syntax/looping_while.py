jumlah_buku = 10
print('ibu berkata : "baca semua buku"')
jumlah_baca = 0

jumlah_dipahami= 0
print(f'jumlah buku yang sudah dibaca{jumlah_dipahami}')

while jumlah_baca < jumlah_buku * 2:
    jumlah_baca = jumlah_baca + 1
    if jumlah_dipahami == 9:
        print(f"Buku ke {jumlah_dipahami + 1} belum paham")
    else:
        jumlah_dipahami= jumlah_dipahami + 1
        print(f"buku ke {jumlah_dipahami} sudah dibaca dan dipahami")

print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_dipahami}')
if jumlah_dipahami==jumlah_buku:
    print('semua buku paham')
else:
    print(f'saya hanya bisa memahami {jumlah_dipahami} buku')


