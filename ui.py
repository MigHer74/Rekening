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
mw.configure(background="#f0f0f0")
mwicon = PhotoImage(file="icon.png")
mw.iconphoto(True, mwicon)

# Main Window Labels
mwl1 = Label(mw, text="Buscar Beneficiario", font=(
    "Arial", 10, "bold")).place(x=25, y=25)

# Main Window Buttons
mwbs = Button(mw, text="Buscar", width=15,
              command=btnSearch).place(x=500, y=23)

# Main Window Entry
mwes = Entry(mw, width=50)
mwes.place(x=160, y=27)

# Main Window ListBox
mwf1 = Frame()
mws1 = Scrollbar(mwf1,orient=VERTICAL)
mwlb1 = Listbox(mwf1,yscrollcommand=mws1.set,width=50,height=34,activestyle=NONE)
mws1.config(command=mwlb1.yview)
mws1.pack(side=RIGHT, fill=Y)

for i in range(1,101):
    mwlb1.insert(END,f"Elemento {i}")

mwlb1.pack()
mwf1.place(x=160,y=55)


mw.mainloop()
