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

def modify_data(idx, col, value):
    full_data[idx][col] = value

def ubah_csv_gadget():
    string_data = header +  "\n"
    for arr_data in full_data:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    
    f = open("gadget.csv", "w")
    f.write(string_data)
    f.close

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

print(">>> pinjam")

id_tidak_valid = True
while(id_tidak_valid):
    id_pinjam = input("Masukkan ID item: ")
    nama_barang_pinjam = ""
    for i in range(len(full_data)):
        if id_pinjam == full_data[i][0]:
            barang_pinjam = full_data[i]
            idx_barang = i
            id_tidak_valid = False
    if (id_tidak_valid):
        print("ID tidak valid! Ulangi masukan!")

tgl_pinjam = input_tanggal_valid()


jumlah_tidak_valid = True
while(jumlah_tidak_valid):
    jumlah_pinjam = int(input("Jumlah peminjaman: "))
    if barang_pinjam[3] >= jumlah_pinjam:
        barang_pinjam[3] -= jumlah_pinjam
        modify_data(idx_barang, 3, barang_pinjam[3])
        jumlah_tidak_valid = False
    else:
        print("Jumlah barang yang anda masukkan tidak sesuai. Ulangi!")

print("\n"+"Item " + barang_pinjam[1] + " (x" + str(jumlah_pinjam) +") berhasil dipinjam!")

f = open("gadget_borrow_history.csv", "r")
raw_lines = f.readlines()
f.close()
lines_borrow = [raw_line.replace("\n", "") for raw_line in raw_lines]

new_data = str("B") + str(len(lines_borrow)) + ";ini id peminjam;" + id_pinjam + ";" + tgl_pinjam + ";" +str(jumlah_pinjam) + ";False"
lines_borrow.append(new_data)
new_string = ""
for arr in lines_borrow:
    new_string += arr
    new_string += "\n"

f = open("gadget_borrow_history.csv", "w")
f.write(new_string)
f.close()

ubah_csv_gadget()