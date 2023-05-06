import os
import database as db

os.system("cls")

db.verify_tables()

is_company = db.verify_company()


print(is_company)
