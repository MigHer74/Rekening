from tkinter import *

# Main Window
mw = Tk()
mw.title("Rekening - Control de Cheques")
mw.geometry("1000x700")
mw.resizable(False, False)
mw.configure(background="#f0f0f0")
mwicon = PhotoImage(file="icon.png")
mw.iconphoto(True, mwicon)

# Main Windod Labels
mwl1 = Label(mw, text="Buscar Beneficiario", font=(
    "Arial", 10, "bold")).place(x=25, y=25)


mw.mainloop()
