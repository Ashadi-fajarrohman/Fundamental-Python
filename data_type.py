# list

list_buah = ['apel', 'jeruk', 'mangga', 'anggur', 'melon']

# proses dangan for in

for buah in list_buah:
    print(buah)

# menampilkan list pada indeks tertentu
print(list_buah[2])

# menampilkan list pada indeks tertentu dengan for in

for i in range(0, len(list_buah)):
    print(list_buah[i])

print('\nmembuat list baru')
list_buah_baru = list_buah[:]
for i in range(0, len(list_buah_baru)):
    print(list_buah[i])