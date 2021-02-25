#Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer

def elemento(n):
    numero = str(n)
    lista_numeros = list(numero)
    print(lista_numeros[:])
    lista = []
    for i in lista_numeros:
        lista.append(int(i))
    print(lista[:])
    resultado = []
    for l in lista:
        r = l **2
        resultado.append(str(r))
    numero = ""
    for i in resultado:
        numero += i
    print(numero)


       
   

elemento(9119)
