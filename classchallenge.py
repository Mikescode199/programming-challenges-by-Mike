import random as rd

class Saint():
    def __init__(self, nombre: str, cloth: str):
        self.nombre = nombre
        self.cloth = cloth
        self.habilidades = []
        self.octavosentido = 3
        self.edad = rd.randrange(13,700)

    def agregarHabilidad(self, habilidad):
        self.habilidades.append(habilidad)

    def habilidad(self):
        print(f"Hola soy {self.nombre} de {self.cloth}")
        for _ in self.habilidades:
            print(f"Mi habilidad es {_} ")

    def is_God(self):
        if self.edad >= 500:
            print(f"{self.nombre} de {self.cloth} es un Dios, edad {self.edad}")
        else:
            print(f"No es un Dios, edad {self.edad }")

    def is_OctavoSentido(self):
        if self.octavosentido == True:
            print("Ha superado a la muerte")

        elif self.octavosentido == 3:
            print("Comienza a despertar el Octavo sentido")

        else:
            print(f"NO ha superado a la muerte {self.octavosentido}")

santo = Saint("Mike", "Escorpio")
santo.agregarHabilidad("A")
santo.habilidad
santo.is_God()
santo.is_OctavoSentido()


'''
class Santuario():
    def __init__(self):
        self.santos =  []

    def AgregarSantos(self):
        input_caballeros = int(input("Número de caballeros: "))
        for c in range(input_caballeros):
            input_nombre = input("Ingresa nombre del Caballero: ")
            input_cloth = input("Ingresa Cloth: ")
            nuevo_santo = Saint(input_nombre, input_cloth)
            self.santos.append(nuevo_santo.cloth)
            for s in self.santos:
                print(s)
'''