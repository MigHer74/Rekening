from tkinter import *
import database as db


def win_setup():
    def oksetup():
        idcomp = entryval1.get()
        nomcom = entryval2.get()
        idrece = entryval3.get()
        numfol = entryval4.get()

        datacom = (idcomp, nomcom, idrece, numfol)

        db.insert_company_info(datacom)

        stw.destroy()

    def nosetup():
        stw.destroy()

    def closeDisable():
        pass

    stw = Tk()
    stw.title("Rekening - Configuración")
    stw.geometry("580x210")
    stw.resizable(False, False)
    stwicon = PhotoImage(file="icon.png")
    stw.iconphoto(True, stwicon)
    stw.protocol("WM_DELETE_WINDOW", closeDisable)

    # SetUp Windows - Variables Declaration

    entryval1 = IntVar()
    entryval2 = StringVar()
    entryval3 = StringVar()
    entryval4 = IntVar()

    entryval1.set(1)
    entryval3.set("BEN-001")

    # SetUp Window - General Information

    stlf1 = LabelFrame(stw, text=" Información General ",
                       width=410, height=105)
    stlf1.place(x=15, y=10)

    Label(stlf1, text="Id Empresa").place(x=10, y=10)
    Entry(stlf1, width=3, textvariable=entryval1,
          state=DISABLED).place(x=82, y=12)

    Label(stlf1, text="Empresa").place(x=10, y=50)
    Entry(stlf1, textvariable=entryval2, width=50).place(x=83, y=53)

    # SetUp Window - Initial Values Receptor and Document

    stlf2 = LabelFrame(stw, text=" Identificadores ", width=410, height=70)
    stlf2.place(x=15, y=125)

    Label(stlf2, text="Id Receptor").place(x=10, y=10)
    Entry(stlf2, textvariable=entryval3, width=10,
          state=DISABLED).place(x=82, y=12)

    Label(stlf2, text="Folio Cheque").place(x=250, y=10)
    Entry(stlf2, textvariable=entryval4, width=8).place(x=334, y=12)

    # SetUp Window - Ok & Cancel Buttons

    stbok = Button(stw, text="Aceptar", command=oksetup,
                   width=15).place(x=450, y=60)
    stbcancel = Button(stw, text="Cancelar", width=15,
                       command=nosetup).place(x=450, y=110)

    # SetUp Window Loop
    stw.mainloop()
