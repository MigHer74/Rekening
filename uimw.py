from tkinter import *
import database as db

def win_main():
    def widState(state):
        if not state:
            mwes.config(state=DISABLED)
            mwlfl.config(bg="#f0f0f0")
            mwbs.config(state=DISABLED)
            mwbn.config(state=DISABLED)
            mwbm.config(state=DISABLED)
            mwbp.config(state=DISABLED)
            mwbv.config(state=DISABLED)

    def btnSearch():
        print("Search Button Pressed")
        dataSearch = mwes.get()
        print("Value to search", dataSearch)

    def btnNew():
        print("New Button Pressed")

    def btnModify():
        print("Modify Button Pressed")

    def btnPrint():
        print("Print Button Pressed")

    def btnVault():
        print("Vault Button Pressed")

    def btnSetup():
        print("SetUp Button Pressed")

    def btnExit():
        mw.destroy()

    def closeDisable():
        pass

    # Main Window
    mw = Tk()
    mw.title("Rekening - Control de Cheques")
    mw.geometry("546x575")
    mw.resizable(False, False)
    mwicon = PhotoImage(file="icon.png")
    mw.iconphoto(True, mwicon)
    mw.protocol("WM_DELETE_WINDOW", closeDisable)

    # Main Window Buttons
    mwbs = Button(mw, text="Buscar", width=15,
                  command=btnSearch)
    mwbs.place(x=400, y=23)

    mwlfb1 = LabelFrame(mw, text=" Receptor ")
    mwbn = Button(mwlfb1, text="Nuevo", width=15,
                  command=btnNew)
    mwbn.pack(padx=10, pady=10)
    mwbm = Button(mwlfb1, text="Modificar", width=15,
                  command=btnModify)
    mwbm.pack(pady=10)
    mwlfb1.place(x=388, y=80)

    mwlfb2 = LabelFrame(mw, text=" Acciones ")
    mwbp = Button(mwlfb2, text="Cheques a Imprimir", width=15,
                  command=btnPrint)
    mwbp.pack(padx=10, pady=10)
    mwbv = Button(mwlfb2, text="Boveda", width=15,
                  command=btnVault)
    mwbv.pack(pady=10)
    mwbc = Button(mwlfb2, text="Configuracion", width=15,
                  command=btnSetup)
    mwbc.pack(pady=20)
    mwlfb2.place(x=388, y=250)

    mwbx = Button(mw, text="Salir", width=15,
                  command=btnExit).place(x=400, y=500)

    # Main Window Entry & ListBox
    mwlf1 = LabelFrame(mw, text=" Receptor ")
    mwes = Entry(mwlf1, width=54)
    mwes.pack(padx=10, pady=5)
    mwlf1.pack(anchor="nw", padx=14, pady=10)

    mwlf2 = LabelFrame(mw)
    mwlfs = Scrollbar(mwlf2, orient=VERTICAL, width=18)
    mwlfl = Listbox(mwlf2, yscrollcommand=mwlfs.set,
                    width=51, height=28, activestyle=NONE)
    mwlfs.config(command=mwlfl.yview)
    mwlfs.pack(side=RIGHT, fill=Y)

    for i in range(1, 101):
        mwlfl.insert(END, f" Elemento {i} ")

    mwlfl.pack(padx=10, pady=15)
    mwlf2.place(x=14, y=56)

    # Main Window Footer
    mwft1 = Frame(mw, height=25, bg="#AF7AC5")
    mwft1.pack(fill="x", side="bottom")
    Label(mwft1, text="Desarrollado por Miguel Hernandez/MH Services",
          padx=7, bg="#AF7AC5", font=("Arial", 7, "bold")).pack(side="left")
    Label(mwft1, text="2023", padx=7, bg="#AF7AC5",
          font=("Arial", 7, "bold")).pack(side="right")
    
    # Functions when starting the window.
    initial = db.verify_company()
    
    widState(initial)

    # Main Window Loop
    mw.mainloop()
