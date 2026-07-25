class Libro:
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        self.disponible = True

    def informacion(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"""  Título: {self.titulo}
     Autor: {self.autor}
     Código: {self.codigo}
     Estado: {estado}"""


class LibroDigital(Libro):
    def __init__(self, titulo, autor, codigo, formato):
        super().__init__(titulo, autor, codigo)
        self.formato = formato

    def informacion(self):
        return super().informacion() + f"\n     Formato: {self.formato}"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        self.libros.append(libro)
        print(f"Agregado correctamente: {libro.titulo}")

    def mostrar_todo(self):
        if not self.libros:
            print("\nNo hay libros registrados en la biblioteca")
            return
        print("\n" + "="*50)
        print("           CATÁLOGO COMPLETO")
        print("="*50)
        for numero, libro in enumerate(self.libros, 1):
            print(f"\nLIBRO {numero}")
            print(libro.informacion())
            print("-"*40)

    def buscar(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                return libro
        return None


def menu():
    mi_biblio = Biblioteca()

    mi_biblio.agregar(Libro("El Principito", "Antoine de Saint-Exupéry", "9780"))
    mi_biblio.agregar(LibroDigital("Python para todos", "Autor desconocido", "9781", "PDF"))

    while True:
        print("\n==== MENÚ BIBLIOTECA ====")
        print("1. Ver todos los libros")
        print("2. Agregar libro físico")
        print("3. Agregar libro digital")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Salir")

        opcion = input("\nElige una opción: ")

        if opcion == "1":
            mi_biblio.mostrar_todo()

        elif opcion == "2":
            t = input("Título: ")
            a = input("Autor: ")
            i = input("Código: ")
            mi_biblio.agregar(Libro(t,a,i))

        elif opcion == "3":
            t = input("Título: ")
            a = input("Autor: ")
            i = input("Código: ")
            f = input("Formato (PDF/EPUB): ")
            mi_biblio.agregar(LibroDigital(t,a,i,f))

        elif opcion == "4":
            buscar_codigo = input("Escribe el Código del libro: ")
            libro = mi_biblio.buscar(buscar_codigo)
            if libro:
                if libro.prestar():
                    print("Libro prestado correctamente")
                else:
                    print("Ese libro ya está prestado")
            else:
                print("No se encontró el libro")

        elif opcion == "5":
            buscar_codigo = input("Escribe el Código del libro: ")
            libro = mi_biblio.buscar(buscar_codigo)
            if libro:
                libro.devolver()
                print("Libro devuelto, ya está disponible")
            else:
                print("No se encontró el libro")

        elif opcion == "6":
            print("Gracias por usar nuestro sistema")
            break

        else:
            print("Opción no válida, intenta otra vez")

if __name__ == "__main__":
    menu()