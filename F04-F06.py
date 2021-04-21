# Prosedur

# Prosedur F04
# Mencari gadget berdasarkan tahun ditemukan

# KAMUS 

# FUNGSI DAN PROSEDUR
def itemAda(id, database):
# Melihat apakah id ada di database

# KAMUS LOKAL
# found : bool

# ALGORITMA
    found = False
    for i in database:
        found = id == i[0]
    return found

def cetakSearch(id, database):
# Prosedur mencetak 
    print("Nama: ", )

# KAMUS LOKAL

# ALGORITMA
    pass


def cari():

# KAMUS LOKAL

# ALGORITMA
    tahun = int(input("Masukkan tahun: "))
    kategori = input("Masukkan kategori: ")

    print("\nHasil pencarian: \n")

    if kategori == "=":
        pass