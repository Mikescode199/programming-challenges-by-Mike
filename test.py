def saludo(func):
    print("Buenas noches")
    func()


@saludo
def nombre():
    print("mike")
    

