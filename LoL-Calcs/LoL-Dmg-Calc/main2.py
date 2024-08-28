from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

#Función de Cálculo de Daños Según entradas
def calculate_all():
    try:
        #Establecimiento de Variables Base para cálculos
        Mhp = int(MhpEntry.get())
        nhp = int(nhpEntry.get())
        barmor = int(barEntry.get())
        aarmor = int(aarEntry.get())
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
        armor = barmor + aarmor
        
        #Cálculos de Vida Efectiva
        pehp=(1+(armor/100))*nhp
        pehp=round(pehp)
        mehp=(1+(mr/100))*nhp
        mehp=round(mehp)
        pehpLabel.config(text=f"Vida Efectiva Física: {pehp}")
        mehpLabel.config(text=f"Vida Efectiva Mágica: {mehp}")

        #Cálculos de Reducciones de Daño
        pdredux=100/(1+(armor/100))
        pdredux=100-pdredux
        pdredux=round(pdredux)
        pdrLabel.config(text=f"Red. Daño Físico: {pdredux}%")
        mdredux=100/(1+(mr/100))
        mdredux=100-mdredux
        mdredux=round(mdredux)
        mdrLabel.config(text=f"Red. Daño Mágico: {mdredux}%")

        #Cálculos de Reducción/Penetración de Armadura
        if pflatredux>0:
            armor = (barmor - pflatredux/3)+(aarmor - 2*pflatredux/3)
        else:
            pass
        if ppercredux>0:
            armor = (barmor * (100-ppercredux)/100)+(aarmor * (100-ppercredux)/100)
        else:
            pass
        if ppercpen>0:
            farmor = (barmor * (100-ppercpen)/100)+(aarmor * (100-ppercpen)/100)
        else:
            pass
        if lethal>0:
            lethal = lethal*(0.6+(0.4 * lvl)/18)
            lethal = round(lethal)
            farmor = (barmor - lethal/3)+(aarmor/3 - 2*lethal/3)
        else:
            pass

        #Validación de Amplificadores de Daño Físico
        if CritEntryEnabler.get() == True and IEEntryEnabler.get() == True:
            pdmg = pdmg + (pdmg * 1.15)
        elif CritEntryEnabler.get() == True:
            pdmg = pdmg + (pdmg * 0.75)
        
        if BRKEntryEnabler.get() == True and RangeChampEnabler.get() == True:
            pdmg = pdmg + (nhp * 0.06)
        elif BRKEntryEnabler.get() == True:
            pdmg = pdmg + (nhp * 0.1)

        if CdGEntryEnabler.get() == True:
            if nhp < Mhp * 0.4:
                pdmg = pdmg + (pdmg * 0.08)
        
        if CutEntryEnabler.get() == True:
            if nhp > Mhp * 0.5:
                pdmg = pdmg + (pdmg * 0.08)

        if PTAEntryEnabler.get() == True:
            pdmg = pdmg + (pdmg * 0.08)

        if BSEntryEnabler.get() == True and RangeChampEnabler.get() == True:
            pdmg = pdmg + (pdmg * 0.05)
        elif BSEntryEnabler.get() == True:
            pdmg = pdmg + (pdmg * 0.1)


        #Cálculos de Daño Físico Real
        fpdr = 0
        if farmor > 0:
            fpdr = 1 + (farmor / 100)

        pdr = 1 + (armor / 100)

        if fpdr > 0:
            pdr = (pdr+fpdr) / 2

        pdmg = pdmg / pdr
        pdmg = round(pdmg)
        pdLabel.config(text=f"Daño Físico a Realizar: {pdmg}")
        armor = round(armor)
        tarLabel.config(text=f"A-PR: {armor}")

        #Cálculos de Reducción/Penetración Mágica
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

        #TODO: Implementar Amplificadores de Daño Mágico Actuales
        #Validación de Amplificadores de Daño Mágico
        if HeadressEntryEnabler.get() == True:
            if int(HeadressEntry.get()) >= 1 and int(HeadressEntry.get()) <= 3:
                mdmg = mdmg + (mdmg * (0.02 * int(HeadressEntry.get())))
            else:
                showwarning('Valor Incorrecto', 'El valor del Stack de Antifaz/Liandry Debe ser entre 1 y 3')

        if RiftMEntryEnabler.get() == True:
            if int(RiftMEntry.get()) >= 1 and int(RiftMEntry.get()) <= 5:
                mdmg = mdmg + (mdmg * (0.02 * int(HeadressEntry.get())))
            else:
                showwarning('Valor Incorrecto', 'El valor del Stack de Agrietador Debe ser entre 1 y 5')

        if CdGEntryEnabler.get() == True:
            if nhp < Mhp * 0.4:
                mdmg = mdmg + (mdmg * 0.08)
        
        if CutEntryEnabler.get() == True:
            if nhp > Mhp * 0.5:
                mdmg = mdmg + (mdmg * 0.08)

        if PTAEntryEnabler.get() == True:
            mdmg = mdmg + (mdmg * 0.08)

        if BSEntryEnabler.get() == True and RangeChampEnabler.get() == True:
            mdmg = mdmg + (mdmg * 0.05)
        elif BSEntryEnabler.get() == True:
            mdmg = mdmg + (mdmg * 0.1)
        
        #Cálculos de Daño Mágico Real
        fmdr = 0
        if falsemr > 0:
            fmdr = 1+ (falsemr / 100)

        mdr = 1 + (mr / 100)

        if fmdr > 0:
            mdr = (mdr + fmdr) / 2
        
        mdmg = mdmg / mdr
        mdmg = round(mdmg)
        mdLabel.config(text=f"Daño Mágico a Realizar: {mdmg}")
        mr = round(mr)
        tmrLabel.config(text=f"RM-PR: {mr}")

    #Excepciones por Valores o Cálculos Errados 
    except ValueError:
        if MhpEntry.get() == '':
            MhpEntry.delete(0, END)
            MhpEntry.insert(0, 0)
        if nhpEntry.get() == '':
            nhpEntry.delete(0, END)
            nhpEntry.insert(0, 0)
        if barEntry.get() == '':
            barEntry.delete(0, END)
            barEntry.insert(0, 0)
        if aarEntry.get() == '':
            aarEntry.delete(0, END)
            aarEntry.insert(0, 0)
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
        #TODO: Corregir error en recursividad de Entradas Desabilitadas de Liandry/Agrietador
        if  HeadressEntry.get() == '':
            HeadressEntry.delete(0, END)
            HeadressEntry.insert(0, 0)
        if RiftMEntry.get() == '':
            RiftMEntry.delete(0, END)
            RiftMEntry.insert(0, 0)
        calculate_all()
    
#Función para Limpiar Todo
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
    MhpEntry.delete(0, END)
    nhpEntry.delete(0, END)
    barEntry.delete(0, END)
    aarEntry.delete(0, END)
    mrEntry.delete(0, END)
    HeadressEntry.delete(0, END)
    RiftMEntry.delete(0, END)
    
    pdLabel.config(text="Daño Físico a Realizar: ")
    mdLabel.config(text="Daño Mágico a Realizar: ")
    tarLabel.config(text="A-PR: ")
    tmrLabel.config(text="RM-PR: ")
    pehpLabel.config(text="Vida Efectiva Física: ")
    mehpLabel.config(text="Vida Efectiva Mágica: ")
    pdrLabel.config(text="Red. Daño Físico: ")
    mdrLabel.config(text="Red. Daño Mágico: ")


#Interfaz Gráfica
root = Tk()
root.title("Calculadora de Daños League of Legends")

#Bloque Raíz de la GUI
mainframe = Frame(root)
mainframe.pack()
#Establecimiento de Variables para Checkboxes
RangeChampEnabler = BooleanVar()
CritEntryEnabler = BooleanVar()
IEEntryEnabler = BooleanVar()
BRKEntryEnabler = BooleanVar()
CdGEntryEnabler = BooleanVar()
CutEntryEnabler = BooleanVar()
PTAEntryEnabler = BooleanVar()
BSEntryEnabler = BooleanVar()
HeadressEntryEnabler = BooleanVar()
RiftMEntryEnabler = BooleanVar()

def enableIECrit():
    if CritEntryEnabler.get() == True:
        IEChk.config(state=NORMAL)
    elif CritEntryEnabler.get() == False:
        IEChk.config(state=DISABLED, variable=IEEntryEnabler.set(False))

def enableCutCdg():
    if CdGEntryEnabler.get() == False:
        CutChk.config(state=NORMAL)
    elif CdGEntryEnabler.get() == True:
        CutChk.config(state=DISABLED, variable=CutEntryEnabler.set(False))

def enableCdgCut():
    if CutEntryEnabler.get() == False:
        CdGChk.config(state=NORMAL)
    elif CutEntryEnabler.get() == True:
        CdGChk.config(state=DISABLED, variable=CdGEntryEnabler.set(False))

def enableHeadressEntry():
    if HeadressEntryEnabler.get() == True:
        HeadressEntry.config(state=NORMAL)
    elif HeadressEntryEnabler.get() == False:
        HeadressEntry.delete(0, END)
        HeadressEntry.config(state=DISABLED)

def enableRiftMEntry():
    if RiftMEntryEnabler.get() == True:
        RiftMEntry.config(state=NORMAL)
    elif RiftMEntryEnabler.get() == False:
        RiftMEntry.delete(0, END)
        RiftMEntry.config(state=DISABLED)

#Frame de Entradas
EntriesFrame = LabelFrame(mainframe, text="Entradas")
EntriesFrame.grid(padx=5, pady=0, row=0, column=0)
#Frame de Entradas del Atacante
AtkrEntries = LabelFrame(EntriesFrame, text="Atacante")
AtkrEntries.grid(padx=5, pady=0, row=0, column=0)
clLabel = Label(AtkrEntries, text="Lvl Campeón:").grid(padx=5, pady=5, row=0, column=0)
clEntry = Entry(AtkrEntries, width=5)
clEntry.grid(padx=5, pady=5, row=0, column=1)
RangeChampChk = Checkbutton(AtkrEntries, text="Campeón a Rango", variable=RangeChampEnabler)
RangeChampChk.grid(padx=5, pady=5, row=0, column=3)
rawPDmgLabel = Label(AtkrEntries, text="Daño Físico:").grid(padx=5, pady=5, row=1, column=0)
rawPDmgEntry = Entry(AtkrEntries, width=5)
rawPDmgEntry.grid(padx=5, pady=5, row=1, column=1)
afrLabel = Label(AtkrEntries, text="Red. Armadura Plana:").grid(padx=5, pady=5, row=2, column=0)
afrEntry = Entry(AtkrEntries, width=5)
afrEntry.grid(padx=5, pady=5, row=2, column=1)
aprLabel = Label(AtkrEntries, text="Red. Armadura %:").grid(padx=5, pady=5, row=3, column=0)
aprEntry = Entry(AtkrEntries, width=5)
aprEntry.grid(padx=5, pady=5, row=3, column=1)
appLabel = Label(AtkrEntries, text="Pen. % Armadura:").grid(padx=5, pady=5, row=4, column=0)
appEntry = Entry(AtkrEntries, width=5)
appEntry.grid(padx=5, pady=5, row=4, column=1)
letLabel = Label(AtkrEntries, text="Letalidad:").grid(padx=5, pady=5, row=5, column=0)
letEntry = Entry(AtkrEntries, width=5)
letEntry.grid(padx=5, pady=5, row=5, column=1)
rawMDmgLabel = Label(AtkrEntries, text="Daño Mágico:").grid(padx=5, pady=5, row=1, column=3)
rawMDmgEntry = Entry(AtkrEntries, width=5)
rawMDmgEntry.grid(padx=5, pady=5, row=1, column=4)
mrfrLabel = Label(AtkrEntries, text="Red. MR Plana:").grid(padx=5, pady=5, row=2, column=3)
mrfrEntry = Entry(AtkrEntries, width=5)
mrfrEntry.grid(padx=5, pady=5, row=2, column=4)
mrprLabel = Label(AtkrEntries, text="Red. MR %:").grid(padx=5, pady=5, row=3, column=3)
mrprEntry = Entry(AtkrEntries, width=5)
mrprEntry.grid(padx=5, pady=5, row=3, column=4)
mrppLabel = Label(AtkrEntries, text="Pen. % MR:").grid(padx=5, pady=5, row=4, column=3)
mrppEntry = Entry(AtkrEntries, width=5)
mrppEntry.grid(padx=5, pady=5, row=4, column=4)
mrfpLabel = Label(AtkrEntries, text="Pen. MR Plana:").grid(padx=5, pady=5, row=5, column=3)
mrfpEntry = Entry(AtkrEntries, width=5)
mrfpEntry.grid(padx=5, pady=5, row=5, column=4)
#Frame de Entradas del Objetivo
ObjEntries = LabelFrame(EntriesFrame, text="Objetivo")
ObjEntries.grid(padx=5, pady=5, row=0, column=1)
MhpLabel = Label(ObjEntries, text="Vida Máxima:").grid(padx=5, pady=5, row=0, column=0)
MhpEntry = Entry(ObjEntries, width=5)
MhpEntry.grid(padx=5, pady=5, row=0, column=1)
nhpLabel = Label(ObjEntries, text="Vida Nominal:").grid(padx=5, pady=5, row=1, column=0)
nhpEntry = Entry(ObjEntries, width=5)
nhpEntry.grid(padx=5, pady=5, row=1, column=1)
barLabel = Label(ObjEntries, text="Armadura Base:").grid(padx=5, pady=5, row=2, column=0)
barEntry = Entry(ObjEntries, width=5)
barEntry.grid(padx=5, pady=5, row=2, column=1)
aarLabel = Label(ObjEntries, text="Armadura Adicional:").grid(padx=5, pady=5, row=3, column=0)
aarEntry = Entry(ObjEntries, width=5)
aarEntry.grid(padx=5, pady=5, row=3, column=1)
mrLabel = Label(ObjEntries, text="Res. Mágica:").grid(padx=5, pady=5, row=4, column=0)
mrEntry = Entry(ObjEntries, width=5)
mrEntry.grid(padx=5, pady=5, row=4, column=1)
#Frame de Amplificadores
DmgAmpFrame = LabelFrame(EntriesFrame, text="Amplificadores de Daño")
DmgAmpFrame.grid(padx=5, pady=5, row=6, column=0, columnspan=2)
critChk = Checkbutton(DmgAmpFrame, text="Crítico", variable=CritEntryEnabler, command=enableIECrit)
critChk.grid(padx=5, pady=5, row=0, column=0)
IEChk = Checkbutton(DmgAmpFrame, text="Filo Infinito", variable=IEEntryEnabler, state=DISABLED)
IEChk.grid(padx=5, pady=5, row=1, column=0)
BotRKChk = Checkbutton(DmgAmpFrame, text="E.R.A", variable=BRKEntryEnabler)
BotRKChk.grid(padx=5, pady=5, row=0, column=1)
CdGChk = Checkbutton(DmgAmpFrame, text="Golpe de Gracia", variable=CdGEntryEnabler, command=enableCutCdg)
CdGChk.grid(padx=5, pady=5, row=1, column=1)
CutChk = Checkbutton(DmgAmpFrame, text="Corte", variable=CutEntryEnabler, command=enableCdgCut)
CutChk.grid(padx=5, pady=5, row=0, column=2)
PTAChk = Checkbutton(DmgAmpFrame, text="Estr. Ofensiva", variable=PTAEntryEnabler)
PTAChk.grid(padx=5, pady=5, row=1, column=2)
BSChk = Checkbutton(DmgAmpFrame, text="Canc. Sangre", variable=BSEntryEnabler)
BSChk.grid(padx=5, pady=5, row=0, column=3)
HeadressChk = Checkbutton(DmgAmpFrame, text="Antifaz/Liandry", variable=HeadressEntryEnabler, command=enableHeadressEntry)
HeadressChk.grid(padx=5, pady=5, row=1, column=3)
HeadressLabel = Label(DmgAmpFrame, text="Stacks:").grid(row=1, column=4)
HeadressEntry = Entry(DmgAmpFrame, width=3, state=DISABLED)
HeadressEntry.grid(padx=2, pady=2, row=1, column=5)
RiftMChk = Checkbutton(DmgAmpFrame, text="Agrietador", variable=RiftMEntryEnabler, command=enableRiftMEntry)
RiftMChk.grid(padx=5, pady=5, row=0, column=6)
RiftMLabel = Label(DmgAmpFrame, text="Stacks:").grid(row=0, column=7)
RiftMEntry = Entry(DmgAmpFrame, width=3, state=DISABLED)
RiftMEntry.grid(padx=2, pady=2, row=0, column=8)

#Frame de Botones
calcButtonsFrame = Frame(mainframe)
calcButtonsFrame.grid(padx=5, pady=5, row=2, column=0)
calcAll = Button(calcButtonsFrame, text="Calcular Todo", command=calculate_all)
calcAll.grid(padx=5, pady=5, row=0, column=0)
resetB = Button(calcButtonsFrame, text="Reiniciar", command=reset_all)
resetB.grid(padx=5, pady=5, row=0, column=1)

#Frame de Resultados
resultFrame = LabelFrame(mainframe, text="Resultados")
resultFrame.grid(padx=5, pady=5, row=0, column=1)
pdLabel = Label(resultFrame, text="Daño Físico a Realizar: ")
pdLabel.grid(padx=5, pady=5, row=0, column=0)
mdLabel = Label(resultFrame, text="Daño Mágico a Realizar: ")
mdLabel.grid(padx=5, pady=5, row=1, column=0)
tarLabel = Label(resultFrame, text="A-PR: ")
tarLabel.grid(padx=5, pady=5, row=2, column=0)
tmrLabel = Label(resultFrame, text="RM-PR: ")
tmrLabel.grid(padx=5, pady=5, row=3, column=0)
rseFrame = LabelFrame(resultFrame, text="Red. Daños")
rseFrame.grid(padx=5, pady=5, row=4, column=0, columnspan=2)
pehpLabel = Label(rseFrame, text="Vida Efectiva Física: ")
pehpLabel.grid(padx=5, pady=5, row=0, column=0)
mehpLabel = Label(rseFrame, text="Vida Efectiva Mágica: ")
mehpLabel.grid(padx=5, pady=5, row=1, column=0)
pdrLabel = Label(rseFrame, text="Red. Daño Físico: ")
pdrLabel.grid(padx=5, pady=5, row=2, column=0)
mdrLabel = Label(rseFrame, text="Red. Daño Mágico: ")
mdrLabel.grid(padx=5, pady=5, row=3, column=0)

mainloop()
