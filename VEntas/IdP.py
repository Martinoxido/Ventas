
import openpyxl
from openpyxl.styles import Font
from openpyxl.styles import PatternFill

import time
from tkinter import*
from tkinter import messagebox as mb
exel=openpyxl.load_workbook("ProductosPrecios.xlsx")
hoja1=exel.active
#golabalizando dicts

#creando recursos#
precios={}
nombrexid={}
idpornombre={}
root=Tk()

#crando diccionarios
def iniciarInventario():
    dic()
    def cuadroB():
        def cambio(event):
            tail.config(bg="gray",width=200,height=50)
            lbl1.config(bg="gray")
            tail2.config(bg="light gray",width=200,height=50)
            lbl2.config(bg="light gray")
            enun.place(x=1500,y=1500)
            item.place(x=1500,y=1500)
            enun2.place(x=25,y=50)
            item2.place(x=25,y=100)
            Bbusca.place(x=1500,y=1500)
            Bbusca2.place(x=260,y=100)
        def cambio2(event):
            tail.config(bg="light gray",width=200,height=50)
            lbl1.config(bg="light gray")
            tail2.config(bg="gray",width=200,height=50)
            lbl2.config(bg="gray")
            enun2.place(x=1500,y=1500)
            item2.place(x=1500,y=1500)
            enun.place(x=25,y=50)
            item.place(x=50,y=100)
            Bbusca2.place(x=1500,y=1500)
            Bbusca.place(x=260,y=100)
           
            
        #def search2():
        search=Frame(stock)   
        search.config(bg="light gray",width=400,height=500)
        enun=Label(search,text="ID de Producto",font=["Arial","20"],bg="light gray")
        enun2=Label(search,text="Nombre de Producto",font=["Arial","20"],bg="light gray")
        enun.place(x=25,y=50)
        item=Entry(search,width=4,font=["Arial","40"])
        item2=Text(search,width=30,height=4,font=["Arial","10"])
        item.place(x=50,y=100)
        search.place(x=50,y=100)
        
        #detalles
        tail=Frame(stock)
        tail.config(bg="light gray",width=200,height=50)
        lbl1=Label(tail,text="Buscar por ID",bg="light gray",font=["Arial","12"])
        lbl1.place(x=50,y=12)
        tail.place(x=50,y=50)
        tail2=Frame(stock)
        tail2.config(bg="gray",width=200,height=50)
        lbl2=Label(tail2,text="Buscar por NOMBRE",bg="gray",font=["Arial","12"])

        lbl2.place(x=25,y=12)
        tail2.place(x=250,y=50)
        tail.bind("<Button 1>",cambio2)
        tail2.bind("<Button 1>",cambio)
        lbl1.bind("<Button 1>",cambio2)
        lbl2.bind("<Button 1>",cambio)
        ####AAAAAAAAAAAAAAAQUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII QUEDEEEEEEEEEEEEEEEEEEEEEEEEEEEE#
        def ok2():
                BusquedaxNOM()
        def BusquedaxID():
            busca=item.get()
            z=busca
            x=nombrexid.get(busca,"NO ENCONTRADO")
            c=precios.get(busca,"NO ENCONTRADO")
            mb.showinfo("Busqueda",f"""
            ID: {z}
        Nombre: {x}
        Precio: {c}""")
        def BusquedaxNOM():
            busca=item2.get("1.0","1.120")
            z=busca
            x=idpornombre.get(busca,"NO ENCONTRADO")
            nid=x
            c=precios.get(nid,"NO ENCONTRADO")
            mb.showinfo("Busqueda",f"""
            ID: {z}
        Nombre: {x}
        Precio: {c}""")
        def ok():
            BusquedaxID()
        Bbusca=Button(search,text="Buscar",font=["Arial","25"],command=ok)
        Bbusca2=Button(search,text="Buscar",font=["Arial","25"],command=ok2)
        Bbusca.place(x=260,y=100)
        
        ######
        
        
    
        
    stock=Frame()
    x=PhotoImage(file="Bg/ACT.gif")
    stock.config(bg="red",width=1280,height=720)
    Label(stock,image=x).pack()
    stock.place(x=0,y=0)
    cuadroB()
    
    
    #creando recursos#
   
    
    ####
    aa
    
    
    
def dic():
    x=hoja1["F2"].value
    print(x)
    
    for i in range (1,x):
        q=hoja1[f"A{i}"]
        w=hoja1[f"C{i}"]
        e=hoja1[f"B{i}"]
        ID=q.value
        PRE=w.value
        NOM=e.value
        precios[ID] = PRE
        nombrexid[ID] = NOM
        idpornombre[NOM] = ID
        
def BusquedaxID():
    busca=item.get()
    z=busca
    x=nombrexid.get(busca,"NO ENCONTRADO")
    c=precios.get(busca,"NO ENCONTRADO")
    print(f"""
    ID: {z}
Nombre: {x}
Precio: {c}""")
def BusquedaxNOM():
    busca=item2.get()
    z=busca
    x=idpornombre.get(busca,"NO ENCONTRADO")
    nid=x
    c=precios.get(nid,"NO ENCONTRADO")
    print(f"""
    ID: {z}
Nombre: {x}
Precio: {c}""")




iniciarInventario()

