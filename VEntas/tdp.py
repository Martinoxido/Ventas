import openpyxl as o
excel=o.load_workbook('tomaDeProductos.xlsx')
sheet1=excel.active
ID_precios={}
ID_nombres={}
def TDP():
    x=sheet1['E1'].value
    for i in range (2,x+1):
        jet=sheet1[f'A{i}'].value
        ID_precios[jet]=sheet1[f'C{i}'].value
        ID_nombres[jet]=sheet1[f'B{i}'].value
def inventarioTotal():
    x=sheet1['E1'].value
    for i in range (2,x+1):
        ID=sheet1[f'A{i}'].value
        print (ID,'$',ID_precios.get(ID),ID_nombres.get(ID))
def BuscarPorID():
    
    busca=input('Ingrese ID del producto: ')
    print(busca,'$',ID_precios.get(busca,'Producto no'),ID_nombres.get(busca,'encontrado'))
    
    
        

TDP()
inventarioTotal()
BuscarPorID()





