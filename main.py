import os
import database as db
import uistw as st


os.system("cls")

db.verify_tables()

is_company = db.verify_company()

if not is_company:
    st.win_setup(True)

print("Show the main window")