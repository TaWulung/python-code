
print('\nperintah del')
daftar_film = ['Fury','300','Interstellar','The Pope']
del daftar_film[1]
for k in range(1, len(daftar_film)):
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