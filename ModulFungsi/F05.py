# Program Menambah Item

# I.S. Menerima database gadget dan item, serta input informasi item baru (input item divalidasi dulu)
# F.S. Item baru dimasukkan ke database gadget dan item bila input valid


# KAMUS
# type type gadget : <ID        : string, 
#                     Nama      : string,
#                     Deskripsi : string,
#                     Jumlah    : string,
#                     Rarity    : string,
#                     Tahun     : string>

# type dbG : array of gadget

# type type consumable : <ID        : string, 
#                         Nama      : string,
#                         Deskripsi : string,
#                         Jumlah    : string,
#                         Rarity    : string>

# type dbC : array of consumable

# databaseG : dbG 
# databaseC : dbC

# isGadget : boolean
# ID, Nama, Deskripsi, Jumlah, Rarity, Tahun : string
# Item : (dbG/dbC)


# FUNGSI DAN PROSEDUR

def searchDatabase(Id, database):
# Fungsi yang memeriksa apakah sebuah Id ada di dalam database

# KAMUS LOKAL
# found : boolean

# ALGORITMA
    found = False
    for i in database:
        if i[0] == Id: 
            found = True
            break
    return found


def rarityValid(x):
# Fungsi yang memeriksa apakah x input rarity yang valid

# KAMUS LOKAL

# ALGORITMA
    return (x == "S") or (x == "A") or (x == "B") or (x == "C")


def sortInsert(Database, Entry):
# Fungsi memasukan entry baru ke database sesuai urutan ID

# KAMUS LOKAL
# panjang : integer
# idNo    : integer
# entryNo : integer
# temp    : (dbG/dbC)

# ALGORITMA
    temp    = [Database[0]]    # Memasukkan bagian awal ([id, nama, deskripsi, ...])
    entNo   = int(Entry[0][1:])   # Nomor id Entry
    panjang = len(Database) - 1

    for i in range(1,(panjang + 1)):
        idNo = int(Database[i][0][1:])    # Nomor id dari rekaman i
        
        if (entNo < idNo):  # Jika entry mempunyai urutan di tengah
            temp.append(Entry)
            for j in Database[i:]:  # Memasukkan sisa dari database
                temp.append(j)
            break

        else:
            temp.append(Database[i]) 

            if  i == panjang: # Jika entry mempunyai urutan terakhir
                temp.append(Entry)
    
    return temp
    

# PROGRAM UTAMA
def tambahItem(databaseG, databaseC):
    ID = input("Masukan ID: ")
    
    # Pengecekan ID valid
    if ((ID[0] != "G") and (ID[0] != "C")) or not( ID[1:].isdigit() ) :     # Masukkan sudah ada di database
        print("\nGagal menambahkan item karena ID tidak valid.")

    elif (searchDatabase(ID, databaseC) or searchDatabase(ID, databaseG)):  # Masukkan sudah ada di database
        print("\nGagal menambahkan item karena ID sudah ada.")
    
    else:            
        Nama = input("Masukan Nama: ")
        Deskripsi = input("Masukan Deskripsi: ")
        Jumlah = input("Masukan Jumlah: ")

        if not(Jumlah.isdigit()):   # Masukkan bukan integer
            print("\nInput jumlah tidak valid!")

        else:
            Rarity = input("Masukan Rarity: ")

            if not(rarityValid(Rarity)):    # Masukkan bukan rarity yang valid
                print("\nInput rarity tidak valid! (Rarity yang ada adalah S, A, B, C)")

            else:
                if (ID[0] == "G"):    # Jika item baru berupa gadget
                    Tahun = input("Masukan tahun ditemukan: ")

                    if not(Tahun.isdigit()):    # Masukkan bukan integer
                        print("\nInput tahun tidak valid!")

                    else:
                        Item = [ID, Nama, Deskripsi, Jumlah, Rarity, Tahun]
                        databaseG = sortInsert(databaseG, Item)
                        print("\nItem telah berhasil ditambahkan ke database.")
                
                else:   # Jika item baru berupa consumable
                    Item = [ID, Nama, Deskripsi, Jumlah, Rarity]
                    databaseC = sortInsert(databaseC, Item)
                    print("\nItem telah berhasil ditambahkan ke database.")
                    
    return (databaseG, databaseC)
