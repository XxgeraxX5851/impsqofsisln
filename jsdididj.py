from datetime import datetime

ahora = datetime.now ()
print(ahora.year)
print(ahora.strftime('%A')) 
fecha = datetime(2025,4,11) 
print(fecha.strftime('%B'))  
str_fecha = '19/04/08 12:35:00'
fecha_obj = datetime.strptime(str_fecha,'%d/%m/%y %H:%M:%S')
dias_vivido = (ahora - fecha_obj)
print(dias_vivido)
