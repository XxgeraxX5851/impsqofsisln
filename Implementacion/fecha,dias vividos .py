from datetime import datetime 

ahora = datetime.now()
print(ahora.year) #año de hoy 
print(ahora.strftime('%A')) #dia de hoy
fecha = datetime(2025,9,5)
print(fecha.strftime('%B')) #mes de una fecha
str_fecha ='19/04/2008 12:30:00'
fecha_obj = datetime.strptime(str_fecha,'%d/%m/%Y %H:%M:%S')

print(ahora - fecha_obj)