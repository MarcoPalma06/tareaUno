#Marco Antonio Palma Rivera
#20192000607

class Libro:
    def __init__(self, titulo: str, autor: str, aPublicado: int, numPaginas: int):
        self.titulo = titulo
        self.autor = autor
        self.aPublicado = aPublicado
        self.numPaginas = numPaginas

    def mostrarInformacion(self):
        print(f'Título: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Año de publicacion: {self.aPublicado}')
        print(f'Numero de páginas: {self.numPaginas}')

DonQuijoteDeLaMancha = Libro('Don Quijote de la mancha', 'Miguel de Cervantes Saavedra', 1605, 863)

# print(DonQuijoteDeLaMancha)

DonQuijoteDeLaMancha.mostrarInformacion()