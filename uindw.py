from tkinter import *


def okBtn():
    pass


def cancelBtn():
    ndw.destroy()


def closeDisable():
    pass


ndw = Tk()
ndw.title("Rekening - Nuevo Cheque")
ndw.geometry("720x220")
ndwicon = PhotoImage(file="icon.png")
ndw.iconphoto(True, ndwicon)
ndw.protocol("WM_DELETE_WINDOW", closeDisable)

# Data Examples
idValue = StringVar()
idValue.set("BN-001")

nameValue = StringVar()
nameValue.set("El nombre del receptor")


# New Document Window - Label Frame & Receptor Data

ndlf1 = LabelFrame(ndw, text=" Receptor ", width=380,
                   height=65).place(x=10, y=10)
Label(ndlf1, textvariable=idValue, font=(
    "Arial", 10, "bold")).place(x=20, y=35)
Label(ndlf1, text="-", font=("Arial", 10, "bold")).place(x=68, y=35)
Label(ndlf1, textvariable=nameValue, font=(
    "Arial", 10, "bold")).place(x=80, y=35)


# New Document Window - Label Frame & Entry Document Data

ndlf2 = LabelFrame(ndw, text=" Información del Cheque",
                   width=700, height=115).place(x=10, y=85)
Label(ndlf2, text="Fecha:").place(x=20, y=115)
Entry(ndlf2, width=12).place(x=65, y=117)

Label(ndlf2, text="Importe:").place(x=175, y=115)
Entry(ndlf2, width=15).place(x=235, y=117)

Label(ndlf2, text="Concepto:").place(x=20, y=155)
Entry(ndlf2, width=100).place(x=85, y=157)


# New Document Window - Buttons Ok & Cancel

Button(ndw, text="Aceptar", width=15, command=okBtn).place(x=420, y=33)
Button(ndw, text="Cancelar", width=15,
       command=cancelBtn).place(x=570, y=33)


# New Document Window Loop
ndw.mainloop()
