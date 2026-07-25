#import pytest
from biblioteca import Libro, LibroDigital, Biblioteca

#1

def test_creacion_libro():
    libro = Libro("Cien años de soledad", "Gabriel García Márquez", "101")
    assert libro.titulo == "Cien años de soledad"
    assert libro.autor == "Gabriel García Márquez"
    assert libro.codigo == "101"
    assert libro.disponible is True

def test_prestar_y_devolver_libro():
    libro = Libro("El Principito", "Antoine de Saint-Exupéry", "102")
    
    assert libro.prestar() is True
    assert libro.disponible is False
    assert libro.prestar() is False  # Ya prestado
    
    libro.devolver()
    assert libro.disponible is True

def test_informacion_libro():
    libro = Libro("Rayuela", "Julio Cortázar", "103")
    info = libro.informacion()
    assert "Rayuela" in info
    assert "Disponible" in info
    
    libro.prestar()
    info_prestado = libro.informacion()
    assert "Prestado" in info_prestado


#2

def test_libro_digital_informacion():
    libro_d = LibroDigital("Python Avanzado", "Guido van Rossum", "201", "PDF")
    info = libro_d.informacion()
    assert "Formato: PDF" in info
    assert libro_d.formato == "PDF"


#3cls

def test_agregar_y_buscar_libro():
    biblio = Biblioteca()
    libro1 = Libro("Fahrenheit 451", "Ray Bradbury", "301")
    
    biblio.agregar(libro1)
    
    encontrado = biblio.buscar("301")
    assert encontrado is not None
    assert encontrado.titulo == "Fahrenheit 451"
    
    no_encontrado = biblio.buscar("999")
    assert no_encontrado is None

def test_mostrar_todo(capsys):
    biblio = Biblioteca()
    
    biblio.mostrar_todo()
    captured = capsys.readouterr()
    assert "No hay libros registrados" in captured.out
    
    biblio.agregar(Libro("1984", "George Orwell", "302"))
    biblio.mostrar_todo()
    captured_con_libros = capsys.readouterr()
    assert "CATÁLOGO COMPLETO" in captured_con_libros.out

 
# PARA PRUEBAS Y VERIFICACIÓN DE FALLOS:
# Si deseas comprobar que pytest detecta errores correctamente, puedes cambiar 
# un valor esperado dentro de las pruebas superiores.
#
# Ejemplo:
# En 'test_creacion_libro', si cambias:
#     assert libro.codigo == "101"
# Por un código distinto como:
#     assert libro.codigo == "102"
#
# Al ejecutar 'python -m pytest' en la terminal, la prueba fallará (FAILED) 
# y mostrará un AssertionError indicando la diferencia entre "101" y "102".
# ==============================================================================