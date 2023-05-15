from tkinter import*
from gen import*
import openpyxl
exel=openpyxl.load_workbook('hist.xlsx')
sheet = exel.active
from openpyxl.styles import Font
from openpyxl.styles import PatternFill
import time


#root=Tk()
#root.geometry("1280x720")
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



   

    
