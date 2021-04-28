def csv_to_line(nama_csv):
    f = open(nama_csv, "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    return lines

def line_to_data(line, column): #Seperti fungsi split
    idx = 0
    raw_line = ["" for i in range(column)]
    for i in line:
        if i != ";":
            raw_line[idx] += i
        else:
            idx += 1
            continue
        line = raw_line
    return line

def convert_data_to_real_value(array_data): #mengubah data kuantitatif menjadi type int
    arr_cpy = array_data
    for i in range(6):
        if (i == 3) :
            arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

def line_to_real_value(lines, column):
    full_data = []
    for line in lines:
        data = line_to_data(line, column)
        real_data = convert_data_to_real_value(data)
        full_data.append(real_data)
    return full_data

def modify_data(data, idx, col, value):
    data[idx][col] = value

def input_perubahan(jumlah_barang):
    jumlah_tidak_valid = True
    while(jumlah_tidak_valid):
        jumlah_ubah = int(input("Masukkan Jumlah: "))
        if jumlah_barang + jumlah_ubah >= 0:
            jumlah_barang += (jumlah_ubah)
            jumlah_tidak_valid = False
        else:
            print("Jumlah barang yang anda masukkan tidak sesuai. Ulangi!")
    return jumlah_barang

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
    modify_data(array, idx_barang, 3, input_perubahan(jumlah_barang))
    return id_tidak_valid

lines_consum = csv_to_line("consumables.csv")
header_consum = lines_consum.pop(0)
full_data_consum = line_to_real_value(lines_consum, 5)

lines_gadget = csv_to_line("gadget.csv")
header_gadget = lines_gadget.pop(0)
full_data_gadget = line_to_real_value(lines_gadget, 6)

def ubah_jumlah():
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

ubah_jumlah()