from tkinter import *

def btnSearch():
    print("Search Button Pressed")
    dataSearch = mwes.get()
    print("Value to search", dataSearch)


# Main Window
mw = Tk()
mw.title("Rekening - Control de Cheques")
mw.geometry("700x650")
mw.resizable(False, False)
mwicon = PhotoImage(file="icon.png")
mw.iconphoto(True, mwicon)


# Main Window Buttons
mwbs = Button(mw, text="Buscar", width=15,
              command=btnSearch).place(x=500, y=23)


# Main Window Entry & ListBox
mwlf1 = LabelFrame(mw, text=" Receptor ")
mwes = Entry(mwlf1, width=54).pack(padx=10, pady=5)
mwlf1.pack(anchor="nw", padx=10, pady=10)

mwlf2 = LabelFrame(mw)
mwlfs = Scrollbar(mwlf2, orient=VERTICAL, width=18)
mwlfl = Listbox(mwlf2, yscrollcommand=mwlfs.set,
                width=51, height=33, activestyle=NONE)
mwlfs.config(command=mwlfl.yview)
mwlfs.pack(side=RIGHT, fill=Y)

for i in range(1, 101):
    mwlfl.insert(END, f" Elemento {i} ")

mwlfl.pack(padx=10, pady=15)
mwlf2.place(x=10, y=56)


# Main Window Footer
mwft1 = Frame(mw, height=25, bg="#AF7AC5")
mwft1.pack(fill="x", side="bottom")
Label(mwft1, text="Desarrollado por Miguel Hernandez/MH Services",
      padx=7, bg="#AF7AC5", font=("Arial", 7, "bold")).pack(side="left")
Label(mwft1, text="2023", padx=7, bg="#AF7AC5",
      font=("Arial", 7, "bold")).pack(side="right")


# Main Window Loop
mw.mainloop()
