# Modul berisi spesifikasi dan realisasi F01, F02, dan F03

def kapitalisasi(kata):
    # I.S. string yang dimasukkan berhuruf kecil
    # F.S. mengkapitalisasi setiap huruf awal
    counter = 0
    listKata = []
    for i in range(len(kata)):
    	if i == len(kata)-1:
    		listKata.append(kata[counter:i+1].capitalize())
    	if kata[i-1] == ' ':
    		listKata.append(kata[counter:i].capitalize())
    		counter = i
    return ''.join(listKata)

def matriks(csv):
    # I.S. mengimport file csv
    # F.S. file csv dijadikan matriks
    with open(csv,'r') as file:
        line = [clean_line.replace('\n','') for clean_line in file.readlines()]
        array = []
        for i in range(len(line)):
            tempArr = []
            counter = 0
            string = line[i]
            length = len(line[i])
            for j in range(length):
                if j == length-1:
                    tempArr.append(string[counter:(j+1)])
                elif string[j] == ';':
                    tempArr.append(string[counter:j])
                    counter = j + 1
            array.append(tempArr)
    return array

def convert(matriks,Str=False,Int=False,Float=False):
    # I.S. tipe data elemen pada matriks tidak sesuai keinginan
    # F.S. tipe data elemen pada matriks berubah sesua keinginan
    # Pilihan tipe: Str : String / Int : Integer / Float : float
    if Str:
        for i in matriks:
            for j in range(len(i)):
                try:
                    i[j] = str(i[j])
                except:
                    continue
    if Int:
        for i in matriks:
            for j in range(len(i)):
                try:
                    i[j] = int(i[j])
                except:
                    continue
    if Float:
        for i in matriks:
            for j in range(len(i)):
                try:
                    i[j] = float(i[j])
                except:
                    continue
    return matriks

def adding(csv,new_data):
    # I.S. diberikan data baru berupa list
    # F.S. data baru dimasukkan ke file csv dalam bentuk string
    with open(csv,'w') as file:
        for i in new_data:
            file.write(";".join(i)+"\n")

def register():
    # I.S. admin me-register-kan user baru
    # F.S. mengembalikan data user baru berupa list
    terdaftar = False
    nama = input("Masukkan nama: ")
    uname = input("Masukkan username: ")
    password = input("Masukkan password: ")
    alamat = input("Masukkan alamat: ")
    nama = kapitalisasi(nama)
    for i in range(len(db_user)):
        if uname == db_user[i][1]:
            print("User {} sudah terdaftar, silakan login.".format(uname))
            terdaftar = True
            break
    if terdaftar == False:
        print("User {} telah berhasil register ke dalam Kantong Ajaib".format(uname))
        return [id(uname),uname,nama,alamat,password,'User']

def login():
    # I.S. input uname dan password
    # F.S. mengembalikan role pengguna
    role = 'User'
    logged_in = False
    uname = input("Masukkan username: ")
    password = input("Masukkan password: ")
    for i in range(len(db_user)):
        if db_user[i][1] == uname and db_user[i][4] == password:
            print("Halo {}, selamat datang di Kantong Ajaib!".format(uname))
            logged_in = True
            user = db_user[i]
            break
    if logged_in == False:
        print("Maaf, username dan password tidak dapat ditemukan.")
    else:
    	if user[5] == 'Admin':
    		role = 'Admin'
    # --- role: Admin/User
    return role
 
def carirarity():
    # menampilkan gadget sesuai rarity yang di-input
    rarity = input("Masukkan rarity: ")
    for i in db_gadget:
        if i[4] == rarity:
            print("\nHasil pencarian:\n")
            print("Nama\t\t\t:",i[1])
            print("Deskripsi\t\t:",i[2])
            print("Jumlah\t\t\t:",int(i[3]))
            print("Rarity\t\t\t:",i[4])
            print("Tahun ditemukan\t:",i[5])

def Help():
    print("=== COMMAND ===")
    print("register - mendaftarkan akun pengguna baru")
    print("login - melakukan log-in ke dalam sistem")
    print("carirarity - mengeluarkan gadget berdasarkan rarity")
    print("caritahun - mengeluarkan gadget berdasarkan tahun ditemukan")
    print("tambahitem - melakukan penambahan item")
    print("hapus item - menghapus item")
    print("ubahjumlah - mengubah jumlah item yang ada")
    print("pinjam - meminjam gadget")
    print("kembalikan - mengembalikan gadget")
    print("minta - meminta consumable")
    print("riwayatpinjam - meilihat riwayat peminjaman gadget")
    print("riwayatkembali - melihat riwayat pengembalian gadget")
    print("riwayatambil - melihat riwayat pengambilan consumable")
    print("save - menyimpan perubahan data")
    print("exit - keluar dari program")

db_user = matriks('user.csv')
db_gadget = matriks('gadget.csv')


# PROGRAM UTAMA -> skema sementara main.py
if __name__ == '__main__':
    print('='*10+'\nSELAMAT DATANG\n'+'='*10)
    while 1:
        print('\n*Ketik "Help" untuk melihat command yang tersedia*')
        command = input('>>> ')
        # login
        if command == 'login':
            user = login()
            command2 = input('>>> ')
            if user == 'Admin':
                # tersedia fungsi-fungsi untuk admin
                if command2 == 'register':
                    new_user = register()
                    db_user.append(new_user)
                    new_data = convert(db_user,Str=True)
                    adding('user.csv',new_data)
                elif command2 == 'tambahitem':
                    # call : tambahitem()
                elif command2 == 'hapusitem':
                    # call : hapusitem()
                elif command2 == 'ubahjumlah':
                    # call : ubahjumlah()
                elif command2 == 'riwayatpinjam':
                    # call : riwayatpinjam()
                elif command2 == 'riwayatkembali':
                    # call : riwayatkembali()
                elif command2 == 'riwayatambil':
                    # call : riwayatambil()
            else:
                if command2 == 'pinjam':
                    # call : pinjam()
                elif command2 == 'kembalikan':
                    # call : kembalikan()
                elif command2 == 'minta':
                    # call : minta()
            if command2 == 'carirarity':
                carirarity()
            elif command2 == 'caritahun':
                # call : caritahun()
            elif command2 == 'save':
                # call : save()
        # Help
        elif command == 'Help':
            Help()
        # exit        
        elif command == 'exit':
            exit()
        else:
            print('Harap login terlebih dahulu untuk mulai, ketik "login".')
