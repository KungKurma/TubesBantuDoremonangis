# KAMUS
# files = list nama file (csv)
# db = matriks dari tiap isi file (csv)

from ModulFungsi import *

files = get_files()
db = get_db()

# index db dan files:
# [0] consumable.csv
# [1] consumable_history.csv
# [2] gadget.csv
# [3] gadget_borrow_history.csv
# [4] gadget_return_history.csv
# [5] user.csv

db_consumable = convert(db[0], Int=True)
db_consumable_history = convert(db[1], Int=True)
db_gadget = convert(db[2], Int=True)
db_gadget_borrow_history = convert(db[3], Int=True)
db_gadget_return_history = convert(db[4], Int=True)
db_user = convert(db[5], Int=True)

# PROGRAM UTAMA

while 1:
	command = input('>>> ')
	if command == 'login':
		user = login(db_user)
		while user != False:
			action = input('>>> ')
			if action == 'register' and user[5] == 'Admin':
				path = get_path('user.csv')
				register(path,db_user)
			# elif action == '...' and user[6] == (Admin/User): (...)
			# elif action == '...': (...) -> untuk role Admin dan User
			elif action == 'carirarity':
				carirarity(db_gadget)
			elif action == 'Help':
				Help()
			elif action == 'save':
				db[0] = convert(db_consumable,Str=True)
				db[1] = convert(db_consumable_history,Str=True)
				db[2] = convert(db_gadget,Str=True)
				db[3] = convert(db_gadget_borrow_history,Str=True)
				db[4] = convert(db_gadget_return_history,Str=True)
				db[5] = convert(db_user,Str=True)
				save(files,db)
			elif action == 'exit':
				exit()
			else:
				print("Error: Command not found.")
	elif command == 'Help':
		Help()
	elif command == 'exit':
		exit()
	else:
		print("Error: Command not found.")
		print('\nKetik "Help" untuk melihat command yang tersedia! ')
