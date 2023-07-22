from tkinter import *
from tkinter.ttk import *

def calculate_all():
    try:
        hp = int(hpEntry.get())
        armor = int(arEntry.get())
        mr = int(mrEntry.get())
        lvl = int(clEntry.get())
        pdmg = int(rawPDmgEntry.get())
        pflatredux = int(afrEntry.get())
        ppercredux = int(aprEntry.get())
        ppercpen = int(appEntry.get())
        lethal = int(letEntry.get())
        mdmg = int(rawMDmgEntry.get())
        mflatredux = int(mrfrEntry.get())
        mpercredux = int(mrprEntry.get())
        mpercpen = int(mrppEntry.get())
        mflatpen = int(mrfpEntry.get())
        farmor = 0
        falsemr = 0
        
        pehp=(1+(armor/100))*hp
        pehp=round(pehp)
        mehp=(1+(mr/100))*hp
        mehp=round(mehp)
        pehpLabel.config(text=f"Vida Efectiva Física: {pehp}")
        mehpLabel.config(text=f"Vida Efectiva Mágica: {mehp}")

        pdredux=100/(1+(armor/100))
        pdredux=100-pdredux
        pdredux=round(pdredux)
        pdrLabel.config(text=f"Red. Daño Físico: {pdredux}%")
        mdredux=100/(1+(mr/100))
        mdredux=100-mdredux
        mdredux=round(mdredux)
        mdrLabel.config(text=f"Red. Daño Mágico: {mdredux}%")

        if pflatredux>0:
            armor = (armor/3 - pflatredux/3)+(2*armor/3 - 2*pflatredux/3)
        else:
            pass
        if ppercredux>0:
            armor = (armor/3 * (100-ppercredux)/100)+(2*armor/3 * (100-ppercredux)/100)
        else:
            pass
        if ppercpen>0:
            farmor = (armor/3 * (100-ppercpen)/100)+(2*armor/3 * (100-ppercpen)/100)
        else:
            pass
        if lethal>0:
            lethal = lethal*(0.6+(0.4 * lvl)/18)
            lethal = round(lethal)
            farmor = (armor/3 - lethal/3)+(2*armor/3 - 2*lethal/3)
        else:
            pass

        fpdr = 1 + (farmor / 100)
        pdr = 1 + (armor / 100)
        pdr = (pdr+fpdr) / 2
        pdmg = pdmg / pdr
        pdmg = round(pdmg)
        pdLabel.config(text=f"Daño Físico a Realizar: {pdmg}")

        if mflatredux>0:
            mr = mr-mflatredux
        else:
            pass
        if mpercredux>0:
            mr = (mr * (100-mpercredux)/100)
        else:
            pass
        if mpercpen>0:
            falsemr = (mr * (100-mpercpen)/100)
        else:
            pass
        if mflatpen>0:
            falsemr = falsemr + (mr-mflatpen)
        else:
            pass

        fmdr = 1+ (falsemr / 100)
        mdr = 1 + (mr / 100)
        mdr = (mdr + fmdr) / 2
        mdmg = mdmg / mdr
        mdmg = round(mdmg)
        mdLabel.config(text=f"Daño Mágico a Realizar: {mdmg}")
    except ValueError:
        if hpEntry.get() == '':
            hpEntry.delete(0, END)
            hpEntry.insert(0, 0)
        if arEntry.get() == '':
            arEntry.delete(0, END)
            arEntry.insert(0, 0)
        if mrEntry.get() == '':
            mrEntry.delete(0, END)
            mrEntry.insert(0, 0)
        if clEntry.get() == '':
            clEntry.delete(0, END)
            clEntry.insert(0, 1)
        if rawPDmgEntry.get() == '':
            rawPDmgEntry.delete(0, END)
            rawPDmgEntry.insert(0, 0)
        if afrEntry.get() == '':
            afrEntry.delete(0, END)
            afrEntry.insert(0, 0)
        if aprEntry.get() == '':
            aprEntry.delete(0, END)
            aprEntry.insert(0, 0)
        if appEntry.get() == '':
            appEntry.delete(0, END)
            appEntry.insert(0, 0)
        if letEntry.get() == '':
            letEntry.delete(0, END)
            letEntry.insert(0, 0)
        if rawMDmgEntry.get() == '':
            rawMDmgEntry.delete(0, END)
            rawMDmgEntry.insert(0, 0)
        if mrfrEntry.get() == '':
            mrfrEntry.delete(0, END)
            mrfrEntry.insert(0, 0)
        if mrprEntry.get() == '':
            mrprEntry.delete(0, END)
            mrprEntry.insert(0, 0)
        if mrppEntry.get() == '':
            mrppEntry.delete(0, END)
            mrppEntry.insert(0, 0)
        if mrfpEntry.get() == '':
            mrfpEntry.delete(0, END)
            mrfpEntry.insert(0, 0)
        calculate_all()

#TO_DO: COLOCAR LOS DELETE DE LAS ENTRADAS EN UN CICLO    
def reset_all():
    clEntry.delete(0, END)
    rawPDmgEntry.delete(0, END)
    afrEntry.delete(0, END)
    aprEntry.delete(0, END)
    appEntry.delete(0, END)
    letEntry.delete(0, END)
    rawMDmgEntry.delete(0, END)
    mrfrEntry.delete(0, END)
    mrprEntry.delete(0, END)
    mrppEntry.delete(0, END)
    mrfpEntry.delete(0, END)
    hpEntry.delete(0, END)
    arEntry.delete(0, END)
    mrEntry.delete(0, END)
    
    pdLabel.config(text="Daño Físico a Realizar: ")
    mdLabel.config(text="Daño Mágico a Realizar: ")
    pehpLabel.config(text="Vida Efectiva Física: ")
    mehpLabel.config(text="Vida Efectiva Mágica: ")
    pdrLabel.config(text="Red. Daño Físico: ")
    mdrLabel.config(text="Red. Daño Mágico: ")

root = Tk()
root.title("Calculadora de Daños League of Legends")

mainframe = Frame(root)
mainframe.pack()

EntriesFrame = LabelFrame(mainframe, text="Entradas")
EntriesFrame.grid(padx=5, pady=5, row=0, column=0)
clLabel = Label(EntriesFrame, text="Lvl Campeón:").grid(padx=5, pady=5, row=0, column=0)
clEntry = Entry(EntriesFrame, width=5)
clEntry.grid(padx=5, pady=5, row=0, column=1)
rawPDmgLabel = Label(EntriesFrame, text="Daño Físico:").grid(padx=5, pady=5, row=1, column=0)
rawPDmgEntry = Entry(EntriesFrame, width=5)
rawPDmgEntry.grid(padx=5, pady=5, row=1, column=1)
afrLabel = Label(EntriesFrame, text="Red. Armadura Plana:").grid(padx=5, pady=5, row=2, column=0)
afrEntry = Entry(EntriesFrame, width=5)
afrEntry.grid(padx=5, pady=5, row=2, column=1)
aprLabel = Label(EntriesFrame, text="Red. Armadura %:").grid(padx=5, pady=5, row=3, column=0)
aprEntry = Entry(EntriesFrame, width=5)
aprEntry.grid(padx=5, pady=5, row=3, column=1)
appLabel = Label(EntriesFrame, text="Pen. % Armadura:").grid(padx=5, pady=5, row=4, column=0)
appEntry = Entry(EntriesFrame, width=5)
appEntry.grid(padx=5, pady=5, row=4, column=1)
letLabel = Label(EntriesFrame, text="Letalidad:").grid(padx=5, pady=5, row=5, column=0)
letEntry = Entry(EntriesFrame, width=5)
letEntry.grid(padx=5, pady=5, row=5, column=1)
rawMDmgLabel = Label(EntriesFrame, text="Daño Mágico:").grid(padx=5, pady=5, row=1, column=3)
rawMDmgEntry = Entry(EntriesFrame, width=5)
rawMDmgEntry.grid(padx=5, pady=5, row=1, column=4)
mrfrLabel = Label(EntriesFrame, text="Red. MR Plana:").grid(padx=5, pady=5, row=2, column=3)
mrfrEntry = Entry(EntriesFrame, width=5)
mrfrEntry.grid(padx=5, pady=5, row=2, column=4)
mrprLabel = Label(EntriesFrame, text="Red. MR %:").grid(padx=5, pady=5, row=3, column=3)
mrprEntry = Entry(EntriesFrame, width=5)
mrprEntry.grid(padx=5, pady=5, row=3, column=4)
mrppLabel = Label(EntriesFrame, text="Pen. % MR:").grid(padx=5, pady=5, row=4, column=3)
mrppEntry = Entry(EntriesFrame, width=5)
mrppEntry.grid(padx=5, pady=5, row=4, column=4)
mrfpLabel = Label(EntriesFrame, text="Pen. MR Plana:").grid(padx=5, pady=5, row=5, column=3)
mrfpEntry = Entry(EntriesFrame, width=5)
mrfpEntry.grid(padx=5, pady=5, row=5, column=4)

hpLabel = Label(EntriesFrame, text="Vida Nominal:").grid(padx=5, pady=5, row=1, column=6)
hpEntry = Entry(EntriesFrame, width=5)
hpEntry.grid(padx=5, pady=5, row=1, column=7)
arLabel = Label(EntriesFrame, text="Armadura:").grid(padx=5, pady=5, row=2, column=6)
arEntry = Entry(EntriesFrame, width=5)
arEntry.grid(padx=5, pady=5, row=2, column=7)
mrLabel = Label(EntriesFrame, text="Res. Mágica:").grid(padx=5, pady=5, row=3, column=6)
mrEntry = Entry(EntriesFrame, width=5)
mrEntry.grid(padx=5, pady=5, row=3, column=7)

calcButtonsFrame = Frame(mainframe)
calcButtonsFrame.grid(padx=5, pady=5, row=1, column=0)
calcAll = Button(calcButtonsFrame, text="Calcular Todo", command=calculate_all)
calcAll.grid(padx=5, pady=5, row=0, column=0)
resetB = Button(calcButtonsFrame, text="Reiniciar", command=reset_all)
resetB.grid(padx=5, pady=5, row=0, column=1)

resultFrame = LabelFrame(mainframe, text="Resultados")
resultFrame.grid(padx=5, pady=5, row=0, column=1)
pdLabel = Label(resultFrame, text="Daño Físico a Realizar: ")
pdLabel.grid(padx=5, pady=5, row=0, column=0)
mdLabel = Label(resultFrame, text="Daño Mágico a Realizar: ")
mdLabel.grid(padx=5, pady=5, row=1, column=0)
rseFrame = LabelFrame(resultFrame, text="Red. Daños")
rseFrame.grid(padx=5, pady=5, row=2, column=0, columnspan=2)
pehpLabel = Label(rseFrame, text="Vida Efectiva Física: ")
pehpLabel.grid(padx=5, pady=5, row=0, column=0)
mehpLabel = Label(rseFrame, text="Vida Efectiva Mágica: ")
mehpLabel.grid(padx=5, pady=5, row=1, column=0)
pdrLabel = Label(rseFrame, text="Red. Daño Físico: ")
pdrLabel.grid(padx=5, pady=5, row=2, column=0)
mdrLabel = Label(rseFrame, text="Red. Daño Mágico: ")
mdrLabel.grid(padx=5, pady=5, row=3, column=0)

mainloop()
