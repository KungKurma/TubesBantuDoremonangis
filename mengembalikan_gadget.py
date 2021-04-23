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

def convert_data_to_real_value(array_data, idx): #mengubah data kuantitatif menjadi type int
    arr_cpy = array_data
    for i in range(6):
        if (i == idx) :
            arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

def line_to_real_value(lines, column, idx):
    full_data = []
    for line in lines:
        data = line_to_data(line, column)
        real_data = convert_data_to_real_value(data, idx)
        full_data.append(real_data)
    return full_data

def mencari_data_gadget(id):
    for i in range(len(full_data_gadget)):
        if (id == full_data_gadget[i][0]):
            data = full_data_gadget[i]
            return data

def input_tanggal_valid():
    tgl_tidak_valid = True
    while(tgl_tidak_valid):
        idx = 0
        tgl_kembali  = input("Tanggal pengembalian: ")
        raw_tgl = ["" for i in range(3)]
        for i in tgl_kembali:
            if i != "/" :
                raw_tgl[idx] += i
            else:
                idx += 1
                continue
        raw_tgl = [int(i) for i in raw_tgl]
        if (raw_tgl[2] % 400 == 0) or ((raw_tgl[2] % 100 != 0) and (raw_tgl[2] % 4 == 0)):
            if (raw_tgl[1] == 1) or (raw_tgl[1] == 3) or (raw_tgl[1] == 5) or (raw_tgl[1] == 7) or (raw_tgl[1] == 8) or (raw_tgl[1] == 9) or (raw_tgl[1] == 11):
                if (1 <= raw_tgl[0] <= 31):
                    tgl_tidak_valid = False
            elif raw_tgl[1] == 2 :
                if (1 <= raw_tgl[0] <= 29):
                    tgl_tidak_valid = False
            else:
                if (1 <= raw_tgl[0] <= 30):
                    tgl_tidak_valid = False
        else:
            if (raw_tgl[1] == 1) or (raw_tgl[1] == 3) or (raw_tgl[1] == 5) or (raw_tgl[1] == 7) or (raw_tgl[1] == 8) or (raw_tgl[1] == 9) or (raw_tgl[1] == 11):
                if (1 <= raw_tgl[0] <= 31):
                    tgl_tidak_valid = False
            elif raw_tgl[1] == 2 :
                if (1 <= raw_tgl[0] <= 28):
                    tgl_tidak_valid = False
            else:
                if (1 <= raw_tgl[0] <= 30):
                    tgl_tidak_valid = False
        if(tgl_tidak_valid):
            print("Tanggal tidak valid. Ulangi!")
    return tgl_kembali

def masukan_nomor_pinjam():
    input_nomor_tidak_valid = True
    while(input_nomor_tidak_valid):
        nomor_pinjam = int(input("Masukkan nomor peminjaman: "))
        if (0 < nomor_pinjam < nomor):
            input_nomor_tidak_valid = False
        else:
            print("Input tidak valid. Ulangi!")
    return nomor_pinjam

def add_data_return_csv():
    lines_return = csv_to_line("gadget_return_history.csv")
    new_data = ("R" + str(len(lines_return)) + ";"+ id_pinjam[nomor_pinjam-1]  + ";" + tgl_kembali)
    lines_return.append(new_data)
    new_string = ""
    for arr in lines_return:
        new_string += arr + "\n"
    g = open("gadget_return_history.csv", "w")
    g.write(new_string)
    g.close()

def ubah_csv_gadget():
    string_data = header_gadget +  "\n"
    for arr_data in full_data_gadget:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    
    f = open("gadget.csv", "w")
    f.write(string_data)
    f.close

def is_returned(): #mengisi True jika barang sudah dikembalikan
    for arr in full_data_borrow:
        if arr[0] == id_pinjam[nomor_pinjam-1]:
            arr[5] = "True"
    string_data = header_borrow +  "\n"
    for arr_data in full_data_borrow:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
        
    f = open("gadget_borrow_history.csv", "w")
    f.write(string_data)
    f.close

print(">>> kembalikan")
lines_borrow = csv_to_line("gadget_borrow_history.csv")
header_borrow = lines_borrow.pop(0)
full_data_borrow = line_to_real_value(lines_borrow, 6, 4)

lines_gadget = csv_to_line("gadget.csv")
header_gadget = lines_gadget.pop(0)
full_data_gadget = line_to_real_value(lines_gadget, 6, 3)

nomor = 1
data_pinjam = []
id_pinjam = []
for i in range(len(full_data_borrow)):
    if full_data_borrow[i][5] == "False":
        gadget = mencari_data_gadget(full_data_borrow[i][2])
        gadget[3] = full_data_borrow[i][4]
        data_pinjam.append(gadget)
        id_peminjaman = full_data_borrow[i][0]
        id_pinjam.append(id_peminjaman)
        print(str(nomor) + ". " + gadget[1])
        nomor += 1

nomor_pinjam = masukan_nomor_pinjam()
tgl_kembali = input_tanggal_valid()
print("Item " + data_pinjam[nomor_pinjam-1][1] + " (x" + str(data_pinjam[nomor_pinjam-1][3]) + ") telah dikembalikan.")
add_data_return_csv()

full_data_gadget = line_to_real_value(lines_gadget, 6, 3)
for i in full_data_gadget:
    if i[0] == data_pinjam[nomor_pinjam-1][0]:
        i[3] += data_pinjam[nomor_pinjam-1][3]

ubah_csv_gadget()
is_returned()