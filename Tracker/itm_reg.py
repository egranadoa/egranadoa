from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

def itemRegister():
    Codentry = str(itmCodeEntry.get()).upper()
    KgEntry = str(itmKgEntry.get())
    DestEntry = str(itmDstCb.get())
    itmRegData = open("RegData.txt", "a")
    
    if not itmRegData:
        itmRegData = open("RegData.txt", "w")
        if Codentry == "" or KgEntry == "" or DestEntry == "":
            messagebox.showerror(message="Alguno de los valores está en blanco",
                                 title="Error: Bloque Vacío")
        else:
            itmRegData.write("\n=====Entrada=====\n")
            itmRegData.write(f"Código de Rastreo: {Codentry}\n")
            itmRegData.write(f"Peso(Kg.): {KgEntry}\n")
            itmRegData.write(f"Destino(Estado): {DestEntry}\n")
            itmRegData.write("=====FinEntrada=====\n")
            itmRegData.close()

            itmCodeEntry.delete(0, END)
            itmKgEntry.delete(0, END)
            itmDstCb.set("Elija un Destino")
    else:
        if Codentry == "" or KgEntry == "" or DestEntry == "":
            messagebox.showerror(message="Alguno de los valores está en blanco",
                                 title="Error: Bloque Vacío")
        else:
            itmRegData.write("\n=====Entrada=====\n")
            itmRegData.write(f"Código de Rastreo: {Codentry}\n")
            itmRegData.write(f"Peso(Kg.): {KgEntry}\n")
            itmRegData.write(f"Destino(Estado): {DestEntry}\n")
            itmRegData.write("=====FinEntrada=====\n")
            itmRegData.close()

            itmCodeEntry.delete(0, END)
            itmKgEntry.delete(0, END)
            itmDstCb.set("Elija un Destino")
    return itmRegData

EstadosVzla = ["", "Amazonas", "Anzoátegui", "Apure", "Aragua",
                "Barinas", "Bolívar", "Carabobo", "Cojedes",
                "Delta Amacuro", "Dependencias Federales",
                "Distrito Capital", "Falcón", "Guárico", "La Guaira", "Lara",
                "Mérida", "Miranda", "Monagas", "Nueva Esparta",
                "Portuguesa", "Sucre", "Táchira", "Trujillo",
                "Yaracuy", "Zulia"]

root = Tk()
root.title("Registro de Envío")

mainframe = Frame(root)
mainframe.pack()

itmDataFrame = LabelFrame(mainframe, text="Datos del Envío")
itmDataFrame.grid(padx=10, pady=10, row=0, column=0)
itmCodeLabel = Label(itmDataFrame, text="Código de Rastreo:")
itmCodeLabel.grid(padx=10, pady=10, row=0, column=0)
itmCodeEntry = Entry(itmDataFrame)
itmCodeEntry.grid(row=0, column=1)
itmKgLabel = Label(itmDataFrame, text="Peso(Kg.):")
itmKgLabel.grid(padx=10, pady=10, row=1, column=0)
itmKgEntry = Entry(itmDataFrame)
itmKgEntry.grid(padx=10, pady=10, row=1, column=1)
itmDstLabel = Label(itmDataFrame, text="Destino:")
itmDstLabel.grid(padx=10, pady=10, row=2, column=0)
itmDstCb = Combobox(itmDataFrame, state="readonly",
                    values=EstadosVzla, width=30)
itmDstCb.set("Elija un Destino")
itmDstCb.grid(padx=10, pady=10, row=2, column=1)

btnsFrame = Frame(mainframe)
btnsFrame.grid(padx=10, pady=10, row=1, column=0)
savebtn = Button(btnsFrame, text="Guardar",
                 command=itemRegister).grid(padx=10, pady=10, row=0, column=0)

mainloop()
