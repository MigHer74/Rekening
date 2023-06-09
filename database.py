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
    condb.close()
    return datdb


def insert_company_info(valdb):
    condb = conect_db()
    curdb = condb.cursor()
    curdb.execute("INSERT INTO 'company' VALUES(?,?,?,?)", (valdb))
    condb.commit()
    condb.close()


def modify_company_info(valdb):
    condb = conect_db()
    curdb = condb.cursor()
    curdb.execute(
        "UPDATE 'company' SET com_name = ?, com_init_rec = ?, com_init_doc = ? WHERE id_com = 1", (valdb))
    condb.commit()
    condb.close()


def update_company_receptor(valdb):
    condb = conect_db()
    curdb = condb.cursor()
    curdb.execute(
        "UPDATE 'company' SET com_init_rec = ? WHERE id_com = 1", (valdb))
    condb.commit()
    condb.close()


def retrieve_all_receptor():
    condb = conect_db()
    curdb = condb.cursor()
    datadb = curdb.execute("SELECT * FROM 'receiver'").fetchall()
    condb.commit()
    condb.close()
    return datadb


def insert_receptor(valdb):
    condb = conect_db()
    curdb = condb.cursor()
    curdb.execute("INSERT INTO 'receiver' VALUES(?,?,?)", (valdb))
    condb.commit()
    condb.commit()
    condb.close()
