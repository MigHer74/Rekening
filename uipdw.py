from tkinter import *


pdlw = Tk()
pdlw.title("Rekening - Cheques Por Imprimir")
pdlw.geometry("700x575")
pdlw.resizable(False, False)
pdlwicon = PhotoImage(file="icon.png")
pdlw.iconphoto(True, pdlwicon)

# Print Document List Window  - Label Frame

pdlwlf = LabelFrame(pdlw, text=" Información de Cheques ",
                    width=678, height=450)
pdlwlf.place(x=12, y=5)


# Print Document List Window Loop

pdlw.mainloop()
