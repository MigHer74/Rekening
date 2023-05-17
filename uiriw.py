from tkinter import *

riw = Tk()
#riw.transient()
#riw.grab_set()
riw.title("Rekening - Información del Receptor")
riw.geometry("580x210")
riw.resizable(False, False)
riwicon = PhotoImage(file="icon.png")
riw.iconphoto(True,riwicon)


# Receptor Information - Window Loop
riw.mainloop()
