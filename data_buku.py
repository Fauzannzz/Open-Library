def baca_file():

    # Membuka file data.txt dan membacanya
    f = open("data.txt","r")

    my_list = []

    # Membaca setiap baris dan kolom dari data.txt
    for line in f:
        num, stok, d1, d2, d3, d4, d5, d6 = line.split()

        # Casting d1 - d6
        list_total = [d1, d2, d3, d4, d5, d6]
        for i in range(0, len(list_total)):
            list_total[i] = int(list_total[i])

        # Membuat List Of Dictionary
        my_list.append({
            'ISBN': num,
            'Stok Buku': int(stok),
            'Senin': int(d1),
            'Selasa': int(d2),
            'Rabu': int(d3),
            'Kamis': int(d4),
            'Jumat': int(d5),
            'Sabtu': int(d6),
            'Total peminjaman': sum(list_total)
        })
    
    # Menutup file
    f.close()
    return my_list

def data_buku_favorit(data):
    
    dict_favorit = {}

    for i in range(0, len(data)):
        dict_favorit.update({data[i]['ISBN']: data[i]['Total peminjaman']})
    
    return max(dict_favorit, key=dict_favorit.get)

def data_total_favorit(data):

    list_favorit = []

    for i in range(0, len(data)):
        list_favorit.append(data[i]['Total peminjaman'])
    
    return max(list_favorit)

def rata_rata(data):

    list_ISBN = []
    list_rata = []
    dict_rata = {}

    for i in range(0, len(data)):
        list_ISBN.append(data[i]['ISBN'])
        list_rata.append(round(data[i]['Total peminjaman']/6, 2))
        zip_iterator = zip(list_ISBN, list_rata)
        dict_rata = dict(zip_iterator)

    return dict_rata

def main():

    # Membuat fungsi membaca data
    print('\n', 'DATA PEMINJAMAN BUKU SELAMA SATU PEKAN :', '\n')
    data_buku = baca_file()

    i = 0
    while i < len(data_buku):
        print(data_buku[i])
        i += 1

    # Membuat fungsi buku favorit dan totalnya
    buku_favorit = data_buku_favorit(data_buku)
    total_favorit = data_total_favorit(data_buku)

    print('\n', 'BUKU TERFAVORIT :', '\n')
    print('-> Buku terfavorit memiliki ISBN =', buku_favorit, 'dengan total peminjaman mencapai', total_favorit, 'eksemplar')

    # Membuat fungsi rata-rata setiap buku
    laporan = rata_rata(data_buku)

    print('\n', 'RATA-RATA PEMINJAMAN SETIAP BUKU :', '\n')
    for k, v in laporan.items():
        print('-> Buku dengan ISBN =', k, 'memiliki rata-rata :', v)


# Memanggil fungsi main
if __name__ == '__main__':
    main()