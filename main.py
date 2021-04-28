from function import *

files = get_files()
db = get_db()

# index db dan files:
# [0] consumable.csv
# [1] consumable_history.csv
# [2] gadget.csv
# [3] gadget_borrow_history.csv
# [4] gadget_return_history.csv
# [5] user.csv

db_consumable = db[0]
db_consumable_history = db[1]
db_gadget = db[2]
db_gadget_borrow_history = db[3]
db_gadget_return_history = db[4]
db_user = db[5]

# PROGRAM UTAMA

while 1:
	command = input('>>> ')
	if command == 'login':
		user = login()
		while user[0]:
			action = input('>>> ')
			if action == 'register' and user[6] == 'Admin':
				register(db_user)
			# elif action == '...' and user[6] == (Admin/User): (...)
			# elif action == '...': (...) -> untuk role Admin dan User
			elif action == 'carirarity':
				carirarity(db_gadget)
			elif action == 'Help':
				Help()
			elif command == 'save':
				db[0] = db_consumable
				db[1] = db_consumable_history
				db[2] = db_gadget
				db[3] = db_gadget_borrow_history
				db[4] = db_gadget_return_history
				db[5] = db_user
				save(files,db)
			elif command == 'exit':
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
