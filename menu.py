import os
import tabulate as tbe


os.system("cls")

while True:
    mheader = ["Menu Principal"]
    mdata = [["[1] - Beneficiarios"], ["[2] - Cheques"],
             ["[3] - Bóveda"], [], ["[X] - Salir"]]
    mmenu = tbe.tabulate(mdata, mheader, tablefmt="simple_outline")

    print(mmenu)
    input("Elija una opción > ")

    break
