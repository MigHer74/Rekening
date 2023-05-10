import os
import database as db
import uistw as scr

os.system("cls")

db.verify_tables()

is_company = db.verify_company()

if not is_company:
    scr.win_setup()
