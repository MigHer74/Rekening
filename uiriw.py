from tkinter import *
import database as db


def win_receiver(WS_status):
    def okReceptor():
        idrec = entryval1.get()
        nomrec = entryval2.get()
        starec = entryval3.get()

        recnewid = []
        datarec = (idrec, nomrec, starec)

        recserie = int(idrec[4:7])
        recserie += 1
        recserie = "BEN-" + str(recserie).zfill(3)
        recnewid.append(recserie)
        recnewid = tuple(recnewid)

        db.insert_receptor(datarec)
        db.update_company_receptor(recnewid)

        riw.destroy()

    def noReceptor():
        riw.destroy()

    def closeDisable():
        pass

    riw = Tk()
    # riw.transient()
    # riw.grab_set()
    riw.title("Rekening - Información del Receptor")
    riw.geometry("480x165")
    riw.resizable(False, False)
    riwicon = PhotoImage(file="icon.png")
    riw.iconphoto(True, riwicon)
    riw.protocol("WM_DELETE_WINDOW", closeDisable)

    # Receptor Information - Variable Declaration

    entryval1 = StringVar()
    entryval2 = StringVar()
    entryval3 = IntVar()

    dc = db.verify_company()

    entryval1.set(dc[0][2])
    entryval3.set(1)

    # Receptor Information - LabelFrames, Labels, Entries & Checkbuttons

    riwlf = LabelFrame(riw, text=" Información General ",
                       width=458, height=95)
    riwlf.place(x=10, y=5)

    Label(riw, text="Id Receptor").place(x=17, y=30)
    Entry(riw, width=8, textvariable=entryval1,
          state=DISABLED).place(x=90, y=32)

    Label(riw, text="Nombre").place(x=17, y=60)
    Entry(riw, textvariable=entryval2, width=60).place(x=90, y=62)

    Checkbutton(riw, text="Activo", variable=entryval3,
                onvalue=1, offvalue=0).place(x=394, y=32)

    # Receptor Information - Buttons

    Button(riw, text="Aceptar", width=15,
           command=okReceptor).place(x=70, y=120)
    Button(riw, text="Cancelar", width=15,
           command=noReceptor).place(x=300, y=120)

    # Receptor Information - Window Loop
    riw.mainloop()
