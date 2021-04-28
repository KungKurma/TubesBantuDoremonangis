def modify_data(data, idx, col, value):
    data[idx][col] = value

def input_perubahan(jumlah):
    jumlah_tidak_valid = True
    while(jumlah_tidak_valid):
        jumlah_ubah = int(input("Masukkan Jumlah: "))
        if jumlah + jumlah_ubah >= 0:
            jumlah_tidak_valid = False
        else:
            print("Jumlah barang yang anda masukkan tidak sesuai. Ulangi!")
    return jumlah_ubah

def proses_perubahan(array, id_barang):
    idx_barang = ""
    for i in range(len(array)):
        if id_barang == array[i][0]:
            jumlah_barang = array[i][3]
            idx_barang  = i
    if idx_barang != "":
        id_tidak_valid = False
    else:
        print("ID tidak valid! Ulangi masukan!")

    jumlah_ubah = input_perubahan(jumlah_barang)
    jumlah_barang += jumlah_ubah
    modify_data(array, idx_barang, 3, jumlah_barang)

    for i in array:
        if i[0] == id_barang:
            nama_barang = i[1]
    if jumlah_ubah >= 0:
        print(str(abs(jumlah_ubah)) + " " + nama_barang + " berhasil ditambahkan. Stok sekarang: " + str(jumlah_barang))
    else:
        print(str(abs(jumlah_ubah)) + " " + nama_barang + " berhasil dibuang. Stok sekarang: " + str(jumlah_barang))
    return id_tidak_valid

def ubah_jumlah(full_data_gadget, full_data_consum):
    print(">>> ubahjumlah")
    id_tidak_valid = True
    while(id_tidak_valid):
        id_barang = input("Masukkan ID item: ")
        if id_barang[0] == "G":
            id_tidak_valid = proses_perubahan(full_data_gadget, id_barang)
        elif id_barang[0] == "C":
            id_tidak_valid = proses_perubahan(full_data_consum, id_barang)
        else:
            print("ID tidak valid! Ulangi masukan!")
            continue
