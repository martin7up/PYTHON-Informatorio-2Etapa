
from datetime import datetime as dt
from typing import Dict
import tkinter as tk
from tkinter import messagebox as ms
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
def crear_ventana(titulo: str= '<sin titulo>', largo: int= 100, ancho: int= 100) -> tk:
    '''Crea una ventana con los datos requeridos o por defecto y muestra el año actual'''
    
    ventana_principal = tk.Tk()#Creacion de ventana

    ventana_principal.title(f'{titulo} {dt.now().year}')#Configuracion de ventana
    ventana_principal.geometry(f'{largo}x{ancho}')

    return ventana_principal

def crear_barra_menu(ventana : tk.Tk, **kwargs: Dict[str, callable]) -> None:
    '''Esta funcion recibe: una ventana a la cual se le agregara una barra de menu, nombres de cada menu y su funcion respectiva'''
    
    #Creacion de barra y asignacion
    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu)

    for nombre, metodo in kwargs.items() :
        barra_menu.add_cascade(label= nombre, command= metodo)
    
def limpiar_marco(marco: tk.Frame) -> None:
    '''Este metodo simplemente limpia todo lo que se encuentre en un marco pasado como argumento'''

    for elemento in marco.winfo_children():
        elemento.destroy()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------        

#Prueba de codigo--------------------------------------------------------------------------------------------------------------------------------------
def main():
    
    def ups() -> None:
        '''Desplega una ventana de informacion.'''
        ms.showinfo('Info!!!', 'Ups! Falta codificar...')

    def aps() -> None:
        '''Desplega una ventana de informacion.'''
        ms.showinfo('Info!!!', 'Aps! Falta codificar...')

    def eps() -> None:
        '''Desplega una ventana de informacion.'''
        ms.showinfo('Info!!!', 'Eps! Falta codificar...')

    window = crear_ventana('Estamos en el año', 500, 350)

    crear_barra_menu(window, ups= ups, aps= aps, eps= eps, none= None)

    window.mainloop()

if __name__ == '__main__':
    main()
#------------------------------------------------------------------------------------------------------------------------------------------------------        