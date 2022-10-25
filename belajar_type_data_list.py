daftar_film = ['Fury','300','Interstellar','The Pope']
print('tampilkan variabel daftar_film')
print(daftar_film)

print('\nproses semua dengan for in')
for film  in daftar_film:
    print(film)

print('\ntampilkan isi daftar_film pada indeks tertentu')
print(daftar_film[-1])
print(daftar_film[0])

print('\ntampilkan dengan for in range')
for k in range(0, len(daftar_film)):
    print(daftar_film[k])

print('\ntambahkan 1 film baru')
daftar_film.append('One Punch Man')
for k in range(0, len(daftar_film)):
    print(daftar_film[k])

print('\nclear list')
daftar_film.clear()
for k in range(0, len(daftar_film)):
    print(daftar_film[k])

print('\nganti nama film')
daftar_film = ['Fury','300','Interstellar','The Pope']
daftar_film[1] = 'Miracle in cell no. 7'
for k in range(0, len(daftar_film)):
    print(daftar_film[k])

print('\nambil nama film')
film = daftar_film.pop(1)
for k in range(0, len(daftar_film)):
    print(daftar_film[k])

print('\nnama film yang diambil diatas')
print(film)

print('\npop tanpa variabel')
daftar_film = ['Fury','300','Interstellar','The Pope']
daftar_film.pop()
for k in range(0, len(daftar_film)):
    print(daftar_film[k])

print('\nperintah del')
daftar_film = ['Fury','300','Interstellar','The Pope']
del daftar_film[0]
for k in range(0, len(daftar_film)):
    print(daftar_film[k])

print('\nperintah del dengan list comprehension')
daftar_film = ['Fury','300','Interstellar','The Pope']
del daftar_film[:]
for k in range(0, len(daftar_film)):
    print(daftar_film[k])

print('\nperintah del dengan list comprehension start')
daftar_film = ['Fury','300','Interstellar','The Pope']
del daftar_film[0:3]
for k in range(0, len(daftar_film)):
    print(daftar_film[k])

print('\nperintah del dengan list comprehension start pake step')
daftar_film = ['Fury','300','Interstellar','The Pope']
del daftar_film[0::2]
for k in range(0, len(daftar_film)):
    print(daftar_film[k])