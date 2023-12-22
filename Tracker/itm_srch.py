from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

def searchItem():
    itm_code = str(itmCodeEntry.get()).upper()
    try:
        Reg_data = open("RegData.txt")
        regs = Reg_data.read()
        if itm_code not in regs:
            messagebox.showwarning(message="Envio no existe en los registros",
                                 title="Alerta")
        elif itm_code in regs:
            messagebox.showinfo(message="Envio existente en los registros",
                                 title="Mensaje")
    except FileNotFoundError:
        messagebox.showerror(message="Archivo de Registro no existe",
                                 title="Error: No hay registros")

    

root = Tk()
root.title("Encontrar Envío")

mainframe = Frame(root)
mainframe.pack()

itmDataFrame = LabelFrame(mainframe, text="Datos del Envío")
itmDataFrame.grid(padx=10, pady=10, row=0, column=0)
itmCodeLabel = Label(itmDataFrame, text="Código de Rastreo:")
itmCodeLabel.grid(padx=10, pady=10, row=0, column=0)
itmCodeEntry = Entry(itmDataFrame)
itmCodeEntry.grid(row=0, column=1)

btnsFrame = Frame(mainframe)
btnsFrame.grid(padx=10, pady=10, row=1, column=0)
savebtn = Button(btnsFrame, text="Buscar",
                 command=searchItem).grid(padx=10, pady=10, row=0, column=0)

mainloop()
