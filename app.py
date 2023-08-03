import pyautogui as robot
import pyperclip as clip
import time


def pide_datos():
    importeTotal=input('Ingrese el total de facturación')
    trueofalse=importeTotal.isdigit()
    if not trueofalse:
        importeTotal=robot.prompt(text='Ingrese un número válido', title='Total' , default='')

    fcPesos=robot.prompt(text='Ingrese la cantidad de facturas en pesos que desea hacer', title='facturas en pesos' , default='')
    trueofalse=fcPesos.isdigit()
    if not trueofalse:
        fcPesos=robot.prompt(text='Ingrese un número válido', title='facturas en pesos' , default='')

    importefcpesos=robot.prompt(text='Ingrese el importe de cada fc en pesos', title='Total' , default='')
    trueofalse=importefcpesos.isdigit()
    if not trueofalse:
        importefcpesos=robot.prompt(text='Ingrese un número válido', title='Total' , default='')

    fcDolar=robot.prompt(text='Ingrese la cantidad de facturas en dólares', title='Total' , default='')
    trueofalse=fcDolar.isdigit()
    if not trueofalse:
        fcDolar=robot.prompt(text='Ingrese un número válido', title='Total' , default='')

    importefcdolar=robot.prompt(text='Ingrese el importe de cada factura de dólares', title='Total' , default='')
    trueofalse=importefcdolar.isdigit()
    if not trueofalse:
        importefcdolar=robot.prompt(text='Ingrese un número válido', title='Total' , default='')

    return importeTotal,fcPesos,fcDolar,importefcpesos,importefcdolar

importeTotal,fcPesos,fcDolar,importefcpesos,importefcdolar=pide_datos()
print(importeTotal,fcPesos,fcDolar,importefcdolar,importefcpesos)
