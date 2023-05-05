import sqlite3


def conect_db():
    condb = sqlite3.connect("rekening.db")
    return condb

def verify_tables():
    condb = conect_db()
    curdb = condb.cursor()
    scrsql = open("tables.sql")
    scrvar = scrsql.read()
    curdb.executescript(scrvar)
    condb.commit()
    condb.close()

def verify_company():
    condb = conect_db()
    curdb = condb.cursor()
    datdb = curdb.execute("SELECT * FROM 'company'").fetchall()
    return datdb