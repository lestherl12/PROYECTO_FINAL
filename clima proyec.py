
print("Elige una opcion"
      """
    1) Consultar clima por ciudad
    2) Salir
    """)
# Leemos lo que ingresa el usuario
eligio=input("-Selecciona una opcion :")

 # Leemos lo que ingresa el usuario   
eligio=input
if eligio=="1":
    print #importamos la libreria request 
import requests          #importamos la libreria
city = input("ingrese una ciudad: ")
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=27aaf6857613a541e5d5c27f9ee32673&units=metric".format(city)    #link de la api

res = requests.get(url)      #  se obtienen los resultados de api
data = res.json()  
#almacenamos los parametros en las variables
temp = data["main"]["temp"]
wind_speed = data ["wind"]["speed"]
latitude = data["coord"]["lat"]
longitud = data ["coord"]["lon"]
descripcion = data ["weather"][0]["description"]
#mostramos los resultados
print("temperatura: ", temp)
print("velocidad del viento: ", wind_speed)
print("latitud: ", latitude)
print("longitud: ", longitud)
print("descripcion: ", descripcion)
if eligio=="2":
    exit
