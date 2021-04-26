# Program Menambah Item

# I.S. Menerima database gadget dan item, serta input informasi item baru (input item divalidasi dulu)
# F.S. Item baru dimasukkan ke database gadget dan item bila input valid


# KAMUS 
# databaseG : list of list
# databaseC : list of list

"""
Kommen yang benar
"""
# ID : string
# isGadget : boolean
# Nama : string
# Deskripsi : string
# Jumlah : string
# Rarity : string
# Tahun : integer
# Item : list


# FUNGSI DAN PROSEDUR

def searchDatabase(Id, database):
# Fungsi yang memeriksa apakah sebuah Id ada di dalam database

# KAMUS LOKAL
# found : boolean
    """
    Kommen yang benar
    """
# ALGORITMA
    found = False
    for i in database:
        if i[0] == Id:
            found = True
            break
    return found


def rarityValid(x):
# Fungsi yang memeriksa apakah input integer

# KAMUS LOKAL

# ALGORITMA
    return (x == "S") or (x == "A") or (x == "B") or (x == "C")


def sortInsert(Database, Entry):
# Fungsi yang memeriksa apakah input integer

    """
    Kommen yang benar
    """
# KAMUS LOKAL
# panjang : integer
# idNo : integer
# entryNo : integer
# temp : list

# ALGORITMA
    temp = []
    entNo = int(Entry[0][1:])
    panjang = len(Database)

    for i in range(panjang):
        idNo = int(Database[i][0][1:])

        if entNo < idNo:
            temp.append(Entry)
            for j in Database[i:]:
                temp.append(j)
            break
        else:
            temp.append(Database[i])
            if  i == (panjang - 1):
                temp.append(Entry)
    
    return temp
    

# PROGRAM UTAMA
def tambahItem(databaseG, databaseC):

    # Input ID
    ID = input("Masukan ID: ")
    
    # Pengecekan ID valid
    if ((ID[0] != "G") and (ID[0] != "C")) or not( ID[1:].isdigit() ) :
        print("\nGagal menambahkan item karena ID tidak valid.")
        return (databaseG, databaseC)

    if (searchDatabase(ID, databaseC) or searchDatabase(ID, databaseG)):
        print("\nGagal menambahkan item karena ID sudah ada.")
        return (databaseG, databaseC)
    
    isGadget = (ID[0] == "G")
        
    Nama = input("Masukan Nama: ")

    Deskripsi = input("Masukan Deskripsi: ")

    Jumlah = input("Masukan Jumlah: ")
    if not(Jumlah.isdigit()):
        print("\nInput jumlah tidak valid!")
        return (databaseG, databaseC)
            
    Rarity = input("Masukan Rarity: ")
    if not(rarityValid(Rarity)):
        print("\nInput rarity tidak valid!")
        return (databaseG, databaseC)

    if isGadget:
        Tahun = input("Masukan tahun ditemukan: ")
        if not(Tahun.isdigit()):
            print("\nInput tahun tidak valid!")
            return (databaseG, databaseC)
        
        Item = [ID, Nama, Deskripsi, int(Jumlah), Rarity, int(Tahun)]
        databaseG = sortInsert(databaseG, Item)
        print("\nItem telah berhasil ditambahkan ke database.")
        return (databaseG, databaseC)
    
    else:
        Item = [ID, Nama, Deskripsi, int(Jumlah), Rarity]
        databaseC = sortInsert(databaseC, Item)
        print("\nItem telah berhasil ditambahkan ke database.")
        return (databaseG, databaseC)
    

        



dumG = [ ["G1","Parametric Transformer","Sering dilupakan",10,'A',2020],
         ["G2","Iphone 20","Layarnya 40 inchi",2,'B',2054],
         ["G3","Swrirly Chair","You spin me right round, baby, right round like a record baby, right round, rpund, round.",3,'C',1776],
         ["G4","Stand Arrow","*insert any jojo meme*",3,'S',1987],
         ["G5","Handphone Nokia","Benda terkuat di dunia",100,'B',2005],
         ["G6","Go Go Gadget: Oil Slick","Prone to slip ups and combustion",2,'C',1989],
         ["G8","SUPERSEMAR","Lah, kok di sini?",1,'S',1996]]

dumC = [ ["C1","Parametric Transformer","Sering dilupakan",10,'A'],
         ["C2","Iphone 20","Layarnya 40 inchi",2,'B'],
         ["C3","Swrirly Chair","You spin me right round, baby, right round like a record baby, right round, rpund, round.",3,'C'],
         ["C4","Stand Arrow","*insert any jojo meme*",3,'S'],
         ["C5","Handphone Nokia","Benda terkuat di dunia",100,'B'],
         ["C6","Go Go Gadget: Oil Slick","Prone to slip ups and combustion",2,'C'],
         ["C8","SUPERSEMAR","Lah, kok di sini?",1,'S'] ]
