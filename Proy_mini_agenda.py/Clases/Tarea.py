from datetime import datetime as dt
from datetime import timedelta as td

#Definicion de clase---------------------------------------------------------------------------------------------------------------------------------
class Tarea:

    #Constructor
    def __init__(self, fecha_de_inicio: dt= dt.now(),
                 duracion_horas: int= 0,
                 duracion_minutos: int= 0,
                 detalle: str= '<No se especifico detalle>') -> None:
        
        self.fecha_de_inicio = fecha_de_inicio
        self.duracion_hora = duracion_horas
        self.duracion_minutos = duracion_minutos
        self.se_completo = False
        self.detalle = detalle

    #Metodos de instancia
    
    def esta_vencida(self) -> bool:
        '''Retorna True si el instante actual es mayor que el instante de comienzo de la tarea mas su duracion; False caso contrario.'''
        
        return dt.now() > (self.fecha_de_inicio + td(hours= self.duracion_hora, minutes= self.duracion_minutos))
    
    def comienza_en(self) -> str:
        '''Si esta vencida retorna hace cuanto se vencio en dias, horas y minutos; caso contrario en cuanto comienza.'''   
        
        delta = dt.now() - self.fecha_de_inicio
        return ('Comenzo hace 'if self.esta_vencida() else 'Comienza en ') + f'{delta.days} dias, {delta.seconds // 3600} horas y {(delta.seconds % 3600) // 60} minutos.'
        
    def __str__(self) -> str:
        '''Retorna una cadena con caracteres de escape para su correcto despliegue en pantalla.'''
        return f'Detalle tarea : {self.detalle}\nInicia : {self.fecha_de_inicio.strftime("%d-%m-%Y %H:%M")}\nDura {self.duracion_hora} horas, con {self.duracion_minutos} minutos\nSe encuentra concluida : {self.se_completo}'
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#Pruebas---------------------------------------------------------------------------------------------------------------------------------------------
def main():

    nueva_tarea = Tarea(dt(year=2024,month=8,day=14,hour=0,minute=59))
    print(nueva_tarea)
    print(nueva_tarea.esta_vencida())
    print(nueva_tarea.comienza_en())

    print('\n')

    nueva_tarea = Tarea(dt(year=2024,month=8,day=15,hour=2,minute=59), 4, 32)
    print(nueva_tarea)
    print(nueva_tarea.esta_vencida())
    print(nueva_tarea.comienza_en())
    
if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------------------------------------------------------------------------------