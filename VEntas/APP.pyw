import tkinter as tk
from ventas import*
import tkinter.font as tkf
from tkinter import*
import time
def confir():
    tk.messagebox.showinfo(title="Estado de venta",message="Venta Registrada\n (revise la info en el excel hist)")
root=tk.Tk()
root.config(bg="white")
root.geometry("1280x720")



#paginas

    
#DISEÑO DE PAGINAS
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




