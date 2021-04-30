def mencari_data_gadget(id,full_data_gadget):
    data = []
    for i in full_data_gadget:
        if (id == i[0]):
            data.append(i[1])
            return data #[nama barang]

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

def masukan_nomor_pinjam(data_pinjam):
    input_nomor_tidak_valid = True
    while(input_nomor_tidak_valid):
        nomor_pinjam = int(input("Masukkan nomor peminjaman: "))
        if (0 < nomor_pinjam < len(data_pinjam)+1):
            input_nomor_tidak_valid = False
        else:
            print("Input tidak valid. Ulangi!")
    return nomor_pinjam

def data_dan_tampilan_awal(id_user,full_data_borrow,full_data_gadget):
    nomor = 1
    data_pinjam = []
    for i in range(len(full_data_borrow)):
        if full_data_borrow[i][5] == "False" and id_user == full_data_borrow[i][1]:
            gadget = mencari_data_gadget(full_data_borrow[i][2], full_data_gadget)
            gadget.append(full_data_borrow[i][4])
            gadget.append(full_data_borrow[i][0])
            data_pinjam.append(gadget)
            print(str(nomor) + ". " + gadget[0])
            nomor += 1
    if nomor == 1:
        is_ada_pinjaman = False
    else:
        is_ada_pinjaman = True
    return data_pinjam, is_ada_pinjaman

def mengembalikan_gadget(id_user, full_data_borrow, full_data_gadget, full_data_return):
    data_pinjam, is_ada_pinjaman = data_dan_tampilan_awal(id_user,full_data_borrow,full_data_gadget)
    if (is_ada_pinjaman):
        nomor_pinjam = masukan_nomor_pinjam(data_pinjam)
        tgl_kembali = input_tanggal_valid()

        print("\n" + "Item " + data_pinjam[nomor_pinjam-1][0] + " (x" + str(data_pinjam[nomor_pinjam-1][1]) + ") telah dikembalikan.")

        for i in range(1, len(full_data_gadget)):
            if full_data_gadget[i][1] == data_pinjam[nomor_pinjam-1][0]:
                full_data_gadget[i][3] += int(data_pinjam[nomor_pinjam-1][1])
        for i in full_data_borrow:
            if i[0] == data_pinjam[nomor_pinjam-1][2]:
                i[5] = "True"

        new_return = ["R" + str(len(full_data_return)+1), data_pinjam[nomor_pinjam-1][2], tgl_kembali]
        full_data_return.append(new_return)
    else:
        print("\n Anda tidak memiliki pinjaman barang.")