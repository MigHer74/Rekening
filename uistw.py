from tkinter import *

stw = Tk()
stw.title("Configuración")
stw.geometry("600x210")
stw.resizable(False, False)
stwicon = PhotoImage(file="icon.png")
stw.iconphoto(True, stwicon)


# SetUp Window General Information

stlf1 = LabelFrame(stw, text=" Información General ", width=410, height=105)
stlf1.place(x=15, y=10)

Label(stlf1, text="Id Empresa").place(x=10, y=10)
Entry(stlf1, width=3, state=DISABLED).place(x=82, y=12)

Label(stlf1, text="Empresa").place(x=10, y=50)
Entry(stlf1, width=50).place(x=83, y=53)


# SetUp Window General Information

stlf2 = LabelFrame(stw, text=" Identificadores ", width=410, height=70)
stlf2.place(x=15, y=125)

Label(stlf2, text="Id Receptor").place(x=10, y=10)
Entry(stlf2, width=10, state=DISABLED).place(x=82, y=12)

Label(stlf2, text="Folio Cheque").place(x=250, y=10)
Entry(stlf2, width=8).place(x=334, y=12)


# SetUp Window Loop
stw.mainloop()
