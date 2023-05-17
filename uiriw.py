from tkinter import *

riw = Tk()
# riw.transient()
# riw.grab_set()
riw.title("Rekening - Información del Receptor")
riw.geometry("480x165")
riw.resizable(False, False)
riwicon = PhotoImage(file="icon.png")
riw.iconphoto(True, riwicon)

# Receptor Information - LabelFrames, Labels, Entries & Checkbuttons

riwlf = LabelFrame(riw, text=" Información General ", width=458, height=95)
riwlf.place(x=10, y=5)

Label(riw, text="Id Receptor").place(x=17, y=30)
Entry(riw, width=6, state=DISABLED).place(x=90, y=32)

Label(riw, text="Nombre").place(x=17, y=60)
Entry(riw, width=60).place(x=90, y=62)

Checkbutton(riw, text="Activo", onvalue=1, offvalue=0).place(x=394, y=32)

# Receptor Information - Buttons

Button(riw, text="Aceptar", width=15).place(x=70, y=120)
Button(riw, text="Cancelar", width=15).place(x=300, y=120)

# Receptor Information - Window Loop
riw.mainloop()
