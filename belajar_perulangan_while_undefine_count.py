""""
perulangan_dengan_while
"""
book_count = 4
print('mom said, "read all your books".')
read_count = 0
understood_count = 0
print(f'understood count {understood_count}')

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 3:
        print(f'book {understood_count + 1} not understood')
    else:
        understood_count = understood_count + 1
        print(f'book {understood_count} understand')
print(f'understood {understood_count}')
if understood_count == book_count:
    print('i was read all books')
else:
    print(f'i was read all books but, understood {understood_count} books')
