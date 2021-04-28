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

def input_tanggal_valid():
    tgl_tidak_valid = True
    while(tgl_tidak_valid):
        idx = 0
        tgl_pinjam  = input("Tanggal peminjaman: ")
        raw_tgl = ["" for i in range(3)]
        for i in tgl_pinjam:
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
    return tgl_pinjam

def ubah_csv_gadget():
    string_data = header +  "\n"
    for arr_data in full_data:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    
    f = open("gadget.csv", "w")
    f.write(string_data)
    f.close

def input_item(id_user):
    id_tidak_valid = True
    data_pinjam = []
    while(id_tidak_valid):
        id_barang = input("Masukkan ID item: ")
        for i in range(len(full_data)):
            if id_barang == full_data[i][0]:
                data_pinjam.append(id_barang)
                data_pinjam.append(full_data[i][1])
                data_pinjam.append(full_data[i][3])
                data_pinjam.append(i)
                id_tidak_valid = False
        for i in full_data_borrow:
            if ((id_barang == i[2]) and (id_user == i[1]) and i[5] == "False"):
                id_tidak_valid = True
        if (id_tidak_valid):
            print("ID tidak valid! Ulangi masukan!")
    return data_pinjam

def input_jumlah_peminjaman(data):
    jumlah_tidak_valid = True
    while(jumlah_tidak_valid):
        jumlah_pinjam = int(input("Jumlah peminjaman: "))
        if data[2] >= jumlah_pinjam:
            data[2] -= jumlah_pinjam
            full_data[data[3]][3] = data[2]
            jumlah_tidak_valid = False
        else:
            print("Jumlah barang yang anda masukkan tidak sesuai. Ulangi!")
    return jumlah_pinjam

f = open("gadget.csv", "r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
header = lines.pop(0)               
full_data = []
for line in lines:
    data = line_to_data(line, 6)
    real_data = convert_data_to_real_value(data)
    full_data.append(real_data)

f = open("gadget_borrow_history.csv", "r")
raw_lines = f.readlines()
f.close()
lines_borrow = [raw_line.replace("\n", "") for raw_line in raw_lines]
header_borrow = lines_borrow.pop(0)
full_data_borrow = []
for line in lines_borrow:
    data = line_to_data(line, 6)
    full_data_borrow.append(data)

print(">>> pinjam")

def meminjam_gadget():
    #MEMASUKKAN ID USER (nanti dihapus)
    id_user = input("Masukkan id user: ")

    data_pinjam = input_item(id_user)
    tgl_pinjam = input_tanggal_valid()
    jumlah_pinjam = input_jumlah_peminjaman(data_pinjam)

    print("\n"+"Item " + data_pinjam[1] + " (x" + str(jumlah_pinjam) +") berhasil dipinjam!")
    new_borrow  = ["B" + str(len(full_data_borrow)+1), id_user, data_pinjam[0], tgl_pinjam, jumlah_pinjam, "False"]
    full_data_borrow.append(new_borrow)

"""new_data = str("B") + str(len(lines_borrow)+1) + ";" + id_user + ";" + data_pinjam[0] + ";" + tgl_pinjam + ";" +str(jumlah_pinjam) + ";False"
lines_borrow.append(new_data)
new_string = header_borrow + "\n"
for arr in lines_borrow:
    new_string += arr
    new_string += "\n"

f = open("gadget_borrow_history.csv", "w")
f.write(new_string)
f.close()

ubah_csv_gadget()"""

meminjam_gadget()
