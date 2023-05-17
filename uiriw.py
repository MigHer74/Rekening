from tkinter import *

riw = Tk()
# riw.transient()
# riw.grab_set()
riw.title("Rekening - Información del Receptor")
riw.geometry("580x210")
riw.resizable(False, False)
riwicon = PhotoImage(file="icon.png")
riw.iconphoto(True, riwicon)

# Receptor Information - LabelFrames, Labels, Entries & Checkbuttons

riwlf = LabelFrame(riw, text=" Información General ", width=500, height=200)
riwlf.place(x=10, y=5)

Label(riw, text="Id Receptor").place(x=17, y=30)
Entry(riw, width=6, state=DISABLED).place(x=90, y=32)

Label(riw, text="Nombre").place(x=17, y=60)
Entry(riw, width=50).place(x=90, y=62)

# Receptor Information - Window Loop
riw.mainloop()
