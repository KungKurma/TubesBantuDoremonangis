# Program Menambah Item

# Menerima input untuk menambah gadget/consumable setelah dikonfirmasi valid
# I.S. Menerima database gadget dan item, serta input informasi item baru (input item divalidasi dulu)
# F.S. Item baru dimasukkan ke database gadget dan item bila input valid


# KAMUS 
# databaseG : list of list
# databaseC : list of list

# ID : string
# isGadget : boolean
# Nama : string
# Deskripsi : string
# Jumlah : string
# Rarity : string
# tahun : integer


# FUNGSI DAN PROSEDUR

def searchDatabase(Id, database):
# Fungsi yang memeriksa apakah sebuah Id ada di dalam database

# KAMUS LOKAL
# found : boolean

# ALGORITMA
    found = False
    for i in database:
        if i == database[0]:
            found = True
            break
    return found


def isInit(x):
# Fungsi yang memeriksa apakah input integer

# KAMUS LOKAL

# ALGORITMA
    return ( type(x) == type(int()) )


# PROGRAM UTAMA
def tambahItem(databaseG, databaseC):

    # Input ID
    ID = input("Masukan ID: ")
    
    # Pengecekan ID valid
    if ( (ID[0] != "G") and (ID[0] != "C") ) or not( ID[1:].isdigit() ) :
        print("Gagal menambahkan item karena ID sudah ada.")

    else:

        if (ID[0] == "G"):
            isGadget = True
        else:
            isGadget = False

        if isGadget:
            if searchDatabase(ID, databaseG):
                print("Gagal menambahkan item karena ID sudah ada")
            
            else:
                Nama = input("Masukan Nama: ")

                Deskripsi = input("Masukan Deskripsi: ")

                
    




dummyList = [ ["G1","Parametric Transformer","Sering dilupakan",10,'A',2020],
              ["G2","Iphone 20","Layarnya 40 inchi",2,'B',2054],
              ["G3","Swrirly Chair","You spin me right round, baby, right round like a record baby, right round, rpund, round.",3,'C',1776],
              ["G4","Stand Arrow","*insert any jojo meme*",3,'S',1987],
              ["G5","Handphone Nokia","Benda terkuat di dunia",100,'B',2005],
              ["G6","Go Go Gadget: Oil Slick","Prone to slip ups and combustion",2,'C',1989],
              ["G7","SUPERSEMAR","Lah, kok di sini?",1,'S',1996] ]

