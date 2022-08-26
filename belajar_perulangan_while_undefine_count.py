""""
perulangan_dengan_while
"""
Jumlah_buku = 13
print('ibu berkata, "baca semua bukumu".')
Total_jumlah_baca = 0
Jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {Jumlah_buku_yang_sudah_dibaca_dan_dipahami}')

while Total_jumlah_baca < Jumlah_buku * 2:
    Total_jumlah_baca = Total_jumlah_baca + 1
    if Jumlah_buku_yang_sudah_dibaca_dan_dipahami == 12:
        print(f'buku ke {Jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1} belum paham')
    else:
        Jumlah_buku_yang_sudah_dibaca_dan_dipahami = Jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f'buku ke {Jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami')
print(f'Jumlah buku yang sudah dibaca dan dipahami {Jumlah_buku_yang_sudah_dibaca_dan_dipahami}')
if Jumlah_buku_yang_sudah_dibaca_dan_dipahami == Jumlah_buku:
    print('saya sudah membaca semua buku')
else:
    print(f'saya sudah membaca semua buku namun hanya memahami {Jumlah_buku_yang_sudah_dibaca_dan_dipahami} buku')
