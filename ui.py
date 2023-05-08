from tkinter import *
from tkinter.ttk import Separator


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

# Main Window Labels
mwl1 = Label(mw, text="Beneficiario", font=("Arial", 8, "bold")).place(x=25, y=7)

# Main Window Buttons
mwbs = Button(mw, text="Buscar", width=15, command=btnSearch).place(x=500, y=23)

# Main Window Entry
mwes = Entry(mw, width=50)
mwes.place(x=28, y=27)

# Main Window ListBox
mwf1 = Frame(mw)
mws1 = Scrollbar(mwf1,orient=VERTICAL)
mwlb1 = Listbox(mwf1,yscrollcommand=mws1.set,width=50,height=34,activestyle=NONE)
mws1.config(command=mwlb1.yview)
mws1.pack(side=RIGHT, fill=Y)

for i in range(1,101):
    mwlb1.insert(END,f"Elemento {i}")

mwlb1.pack()
mwf1.place(x=28,y=55)

# Main Window Footer
mwft1 = Frame(mw,height=25,bg="#AF7AC5")
mwft1.pack(fill="x",side="bottom")
Label(mwft1,text="Desarrollado por Miguel Hernandez/MH Services", padx=7,bg="#AF7AC5",font=("Arial",7,"bold")).pack(side="left")
Label(mwft1,text="2023", padx=7,bg="#AF7AC5",font=("Arial",7,"bold")).pack(side="right")

# Main Window Loop
mw.mainloop()
