import sqlite3


def conect_db():
    condb = sqlite3.connect("rekening.db")
    return condb