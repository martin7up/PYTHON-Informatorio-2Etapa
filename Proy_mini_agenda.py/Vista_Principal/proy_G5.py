import tkinter as tk
import random as rnd
from tkinter import messagebox
from datetime import datetime as dt

def ups() -> None:
    '''Desplega una ventana de informacion.'''
    messagebox.showinfo('Info!!!', 'ups! Falta codificar...')

def mostar_mensaje() -> None:  
    # Remove all widgets from the frame
    for elemento in marco.winfo_children():
        elemento.destroy()
    
    # Create a label and add it to the frame
    label = tk.Label(marco, text=rnd.randint(3,25))
    label.pack(padx=1, pady=1)
    
ventana_raiz = tk.Tk()
ventana_raiz.title(f'Agenda - Planificador InfoG5 {dt.now().year}')
ventana_raiz.geometry('400x150')
ventana_raiz.minsize(width=400,height=150)
ventana_raiz.maxsize(width=750,height=300)

marco = tk.Frame(ventana_raiz, borderwidth=2, relief="sunken")
marco.pack(padx=20, pady=20, fill="both", expand=True)

barra_menu = tk.Menu(ventana_raiz)
ventana_raiz.config(menu=barra_menu)

barra_menu.add_cascade(label = 'Nueva actividad.',command=mostar_mensaje)
barra_menu.add_cascade(label = 'Ver todas.',command=mostar_mensaje)
barra_menu.add_cascade(label = 'Ver completadas.',command=mostar_mensaje)
barra_menu.add_cascade(label = 'Ver pendientes.',command=ups)

ventana_raiz.mainloop()