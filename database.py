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


def insert_company_info(valdb):
    condb = conect_db()
    curdb = condb.cursor()
    datdb = curdb.execute("INSERT INTO 'company' VALUES(?,?,?,?)", (valdb))
    condb.commit()
    condb.close()


def modify_company_info(valdb):
    condb = conect_db()
    curdb = condb.cursor()
    datdb = curdb.execute(
        "UPDATE 'company' SET com_name = ?, com_init_rec = ?, com_init_doc = ? WHERE id_com = 1", (valdb))
    condb.commit()
    condb.close()


def insert_receptor(valdb):
    condb = conect_db()
    curdb = condb.cursor()
    datdb = curdb.execute(
        "INSERT INTO 'names' VALUES(id=?, name=?, active=?)", (valdb))
    condb.commit()
    condb.close()
