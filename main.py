import os
import database as db
import uistw as st
import uimw as mw


os.system("cls")

db.verify_tables()

is_company = db.verify_company()

if not is_company:
    st.win_setup(True)

mw.win_main()
