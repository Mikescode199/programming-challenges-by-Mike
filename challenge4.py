#ASYNC FUNCTION 
import asyncio
import time


precio_frutas = {
    'Fresa': 30,
    'Manzana': 40,
    'Plátano': 12,
    'Sandía' : 37
}

async def Frutero(diccionario):
    print('Hola a todos, estas son las frutas: ')
    await asyncio.sleep(3)
    for _ in diccionario:
        print( _ , ":" , diccionario[_])

asyncio.run(Frutero(precio_frutas))
