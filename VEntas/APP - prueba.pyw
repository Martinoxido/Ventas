import openpyxl
exel=openpyxl.load_workbook('hist.xlsx')
sheet = exel.active
from openpyxl.styles import Font
from openpyxl.styles import PatternFill
import tkinter as tk
#from ventas import*
import tkinter.font as tkf
from tkinter import*
import time
from gen import*
def confir():
    tk.messagebox.showinfo(title="Estado de venta",message="Venta Registrada\n (revise la info en el excel hist)")
root=tk.Tk()
root.config(bg="white")
root.geometry("1280x720")



#paginas Venta
def iniciarventa():
    def validacion(x, y):
        l=2
        while (l>=2 and l<x):
            val=sheet[f'B{l}']
            comp=val.value
            tecla_rand()
            y=int(y)
            comp=int(comp)
            while (comp==y):
                print ('se repitio un codigo')
                lista_char()
                tecla_rand()
                y = clave[0]+clave[1]+clave[2]+clave[3]+clave[4]+clave[5]+clave[6]+clave[7]
            l+=1    
    def codigo(i):
        n=sheet['E1']
        p=n.value
        p=int(p)
        lista_char()
        tecla_rand()
        cod = clave[0]+clave[1]+clave[2]+clave[3]+clave[4]+clave[5]+clave[6]+clave[7]
        validacion(p,cod)  
        sheet[f'B{i}']=cod
        del clave[:]
    def nombre(i):
        nom=tomanombre.get()
        stnom=str(nom)
        sheet[f'C{i}']=stnom
    def fecha(i):
        fechac = time.strftime('%x')
        sheet[f'A{i}']=fechac


    def main():
        n=sheet['E1']
        p=n.value
        p=int(p)
        p+=1
        sheet['E1']=p
        nombre(p)
        codigo(p)
        fecha(p)
        exel.save('hist.xlsx')

    def prueba():
        main()
        ventas.destroy
        iniciarventa()
        mostrarHist()

    def mostrarHist():
        r=sheet[f"E1"] 
        rango=r.value
        for i in range (2,rango+1):
            q=sheet[f"A{i}"]
            w=sheet[f"B{i}"]
            e=sheet[f"C{i}"]

            
        ###convirtiendo casillas en valores
            fecha=q.value
            code=w.value
            name=e.value
        ###mostrando por lineas
            resultado.insert("1.0",f"{fecha}\n")
            resultado2.insert("1.0",f"{code}\n")
            resultado3.insert("1.0",f"{name}\n")
            
            
    ventas=Frame()
    backG=PhotoImage(file="Bg/ACT.gif")
    fondo=Label(ventas,image=backG).pack()
    #toma=Entry(Tframe,width=30).pack()
    Tframe=Frame().place(x=60,y=160,height=360,width=300)
    #Label(Tframe,image=backG).place(x=0,y=0)
    tomanombre=Entry(Tframe,width=30,font=["arial","10"])
    tomanombre.place(x=100,y=250)
    tomaID=Entry(Tframe,width=3,font=["arial","20"]).place(x=180,y=300)
    #nombre=Frame().place(x=200,y=100,width=150)
    #Label(nombre,image=backG).place(x=0,y=0)
    Label(Tframe,text="Nombre de cliente",font=["arial","12"],fg="black").place(x=140,y=225,width=150)
    Label(Tframe,text="ID PRODUCTO",font=["arial","12"],fg="black").place(x=140,y=274,width=150)
    resultado=Text(ventas,height=20,width=8,fg="blue")
    resultado.place(x=500,y=200)
    resultado2=Text(ventas,height=20,width=8,fg="red",bg="#D8D8D8")
    resultado2.place(x=570,y=200)
    resultado3=Text(ventas,height=20,width=30,fg="green")
    resultado3.place(x=640,y=200)
    resultado4=Text(ventas,height=20,width=2,fg="orange",bg="#D8D8D8")
    resultado4.place(x=886,y=200)
    resultado5=Text(ventas,height=20,width=33,fg="black")
    resultado5.place(x=908,y=200)
    resultado6=Text(ventas,height=20,width=8,fg="dark blue",bg="#D8D8D8")
    resultado6.place(x=1178,y=200)
    Label(ventas,text="Historial",font=["arial","20"],bg="light blue").place(x=500,y=160,width=746)
    Listo=Button(Tframe,text="Listo",font=["arial","18"],command=prueba).place(x=170,y=350)
    def dele():
        ventas.destroy()
    Listo2=Button(Tframe,text="Atras",font=["arial","18"],command=pg2T).place(x=0,y=0)
    ##error para forzar la carga de imagen##
    ventas.place(x=0,y=0)
    mostrarHist()
    
    aa
  
    

 

def validacion(x, y):
    l=2
    while (l>=2 and l<x):
        val=sheet[f'B{l}']
        comp=val.value
        tecla_rand()
        y=int(y)
        comp=int(comp)
        while (comp==y):
            print ('se repitio un codigo')
            lista_char()
            tecla_rand()
            y = clave[0]+clave[1]+clave[2]+clave[3]+clave[4]+clave[5]+clave[6]+clave[7]
        l+=1    
def codigo(i):
    n=sheet['E1']
    p=n.value
    p=int(p)
    lista_char()
    tecla_rand()
    cod = clave[0]+clave[1]+clave[2]+clave[3]+clave[4]+clave[5]+clave[6]+clave[7]
    validacion(p,cod)  
    sheet[f'B{i}']=cod
    del clave[:]
def nombre(i):
    nom=tomanombre.get()
    stnom=str(nom)
    sheet[f'C{i}']=stnom
def fecha(i):
    fechac = time.strftime('%x')
    sheet[f'A{i}']=fechac


def main():
    n=sheet['E1']
    p=n.value
    p=int(p)
    while True:
        p+=1
        sheet['E1']=p
        nombre(p)
        codigo(p)
        fecha(p)
        exel.save('hist.xlsx')




    
#DISEÑO DE PAGINAS#######################################################################################################
        #########################################################################################################################
        ###############################################################################
"""Aqui diseño cada frame con sus widgets correspondientes"""
#Pagina 1 LOGIN
login=tk.Frame()

def pg2T():
    def ok():
        print("hola")
    pag2=tk.Frame()
    pag2.config(width=1280,height=720)
    fuente=tkf.Font(family="Arial",size=34)

    fondo=tk.PhotoImage(file="Bg/MENUT.png")
    pag2.pack()
    enun=tk.Label(pag2,image=fondo).place(x=3,y=3)

    def click(event):
        pag2.destroy()
        iniciarventa()
        
        
        
    def onbutton(event):
        botonVentas.config(bd=2)
    def outbutton(event):
        botonVentas.config(bd=0)
    Bv=tk.PhotoImage(file="buttoms/CACHIN.png")
    botonVentas=tk.Label(pag2,image=Bv,font=fuente,bd=0,relief="sunken") 
    botonVentas.place(x=204,y=329)
    botonVentas.bind("<Button-1>",click)
    botonVentas.bind("<Enter>",onbutton)
    botonVentas.bind("<Leave>",outbutton)
    
    def click(event):
        print("hola2")
    def onbutton(event):
        botonBusca.config(bd=2)
    def outbutton(event):
        botonBusca.config(bd=0)
    Bv2=tk.PhotoImage(file="buttoms/buscar.png")
    botonBusca=tk.Label(pag2,image=Bv2,font=fuente,bd=0,relief="sunken")
    botonBusca.place(x=550,y=329)
    botonBusca.bind("<Button-1>",click)
    botonBusca.bind("<Enter>",onbutton)
    botonBusca.bind("<Leave>",outbutton)
    
    def click(event):
        print("hola3")
    def onbutton(event):
        botonDoc.config(bd=2)
    def outbutton(event):
        botonDoc.config(bd=0)
    Bv3=tk.PhotoImage(file="buttoms/boletaycertificado.png")
    botonDoc=tk.Label(pag2,image=Bv3,font=fuente,bd=0,relief="sunken")
    botonDoc.place(x=902,y=329)
    botonDoc.bind("<Button-1>",click)
    botonDoc.bind("<Enter>",onbutton)
    botonDoc.bind("<Leave>",outbutton)
    
    aa
    
    ##este error por alguna razon me permite colocar la imagen y seguir normalmente con el programa
def pg2N():
    def ok():
        print("hola")
    pag2=tk.Frame()
    pag2.config(width=1280,height=720)
    fuente=tkf.Font(family="Arial",size=34)
    fondo=tk.PhotoImage(file="Bg/MENUI.png")
    pag2.pack()
    enun=tk.Label(pag2,image=fondo).place(x=3,y=3)

    def click(event):
        print("hola")
    def onbutton(event):
        botonVentas.config(bd=2)
    def outbutton(event):
        botonVentas.config(bd=0)
    Bv=tk.PhotoImage(file="buttoms/CACHIN.png")
    botonVentas=tk.Label(pag2,image=Bv,font=fuente,bd=0,relief="sunken")
    botonVentas.place(x=204,y=329)
    botonVentas.bind("<Button-1>",click)
    botonVentas.bind("<Enter>",onbutton)
    botonVentas.bind("<Leave>",outbutton)
    
    def click(event):
        print("hola2")
    def onbutton(event):
        botonBusca.config(bd=2)
    def outbutton(event):
        botonBusca.config(bd=0)
    Bv2=tk.PhotoImage(file="buttoms/buscar.png")
    botonBusca=tk.Label(pag2,image=Bv2,font=fuente,bd=0,relief="sunken")
    botonBusca.place(x=550,y=329)
    botonBusca.bind("<Button-1>",click)
    botonBusca.bind("<Enter>",onbutton)
    botonBusca.bind("<Leave>",outbutton)
    
    def click(event):
        print("hola3")
    def onbutton(event):
        botonDoc.config(bd=2)
    def outbutton(event):
        botonDoc.config(bd=0)
    Bv3=tk.PhotoImage(file="buttoms/boletaycertificado.png")
    botonDoc=tk.Label(pag2,image=Bv3,font=fuente,bd=0,relief="sunken")
    botonDoc.place(x=902,y=329)
    botonDoc.bind("<Button-1>",click)
    botonDoc.bind("<Enter>",onbutton)
    botonDoc.bind("<Leave>",outbutton)
    
    aa
    
    ##este error por alguna razon me permite colocar la imagen y seguir normalmente con el programa
    
    
    
    
    

def logining():
    def ok():
        code=cod.get()
        if code=="1":
            marco.destroy()
            pg2T()
            login.destroy()
        elif code=="2":
            print("Hola Nacho")
            marco.destroy()
            pg2N()
            login.destroy()
        else:
            fuente=tkf.Font(family="Arial",size=24)
            tk.Label(entrar,text="*USUARIO NO RECONOCIDO*",font=fuente,fg="red").place(x=160,y=500)
        
    marco=tk.Frame(login, bg="gray")
    marco.config(width=800,height=600)
    marco.place(x=250,y=100)
    entrar=tk.Frame(marco)
    entrar.config(width=790,height=590)
    entrar.place(x=5,y=5)
    fuente=tkf.Font(family="Arial",size=34)
    enun=tk.Label(entrar,text="Codigo de Usuario",font=fuente)
    cod=tk.Entry(entrar,font=fuente)
    acept=tk.Button(entrar,text="OK",font=fuente,command=ok)
    d=80
    enun.place(x=200,y=d)
    cod.place(x=125,y=d*2)
    acept.place(x=325,y=d*3)
    
def click_frame(event):
    logining()
def onbutton(event):
    Blogin.config(image=onPICblogin)
def outbutton(event):
    Blogin.config(image=PICblogin)
    
    
fondo=tk.PhotoImage(file="Bg/LOGIN2.gif")
lbl=tk.Label(login, image=fondo).pack()
login.place(x=0,y=0)
PICblogin=tk.PhotoImage(file="buttoms/Blogin.png")
onPICblogin=tk.PhotoImage(file="buttoms/logiOnPress.png")
bblogin=Frame(login)
Blogin=tk.Label(bblogin,image=PICblogin,bd=0)
Blogin.pack()
bblogin.place(x=462,y=363,width=360,height=80)

Blogin.bind("<Button-1>",click_frame)
Blogin.bind("<Enter>",onbutton)
Blogin.bind("<Leave>",outbutton)
bblogin.place(x=462,y=363)
bblogin.config(width=360,height=80)




root.mainloop()




