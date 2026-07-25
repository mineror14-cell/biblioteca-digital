import streamlit as st
from biblioteca import Libro, LibroDigital, Biblioteca

# Configuración de página
st.set_page_config(page_title="Biblioteca Digital", page_icon="📚", layout="wide")

# Inicializar la biblioteca en la sesión
if 'biblio' not in st.session_state:
    st.session_state.biblio = Biblioteca()
    # Libros iniciales de ejemplo
    st.session_state.biblio.agregar(Libro("Cien años de soledad", "Gabriel García Márquez", "101"))
    st.session_state.biblio.agregar(Libro("El Principito", "Antoine de Saint-Exupéry", "102"))
    st.session_state.biblio.agregar(LibroDigital("Python Avanzado", "Guido van Rossum", "201", "PDF"))

# Título y encabezado principal
st.title(" Panel de Control - Biblioteca Digital")
st.caption("Gestión inteligente, moderna e interactiva de tu catálogo")

# Sidebar (Menú Lateral)
st.sidebar.header(" Navegación")
opcion = st.sidebar.radio("Selecciona una sección:", [" Catálogo de Libros", " Registrar Libro", " Buscar & Prestar"])

# Métricas superiores sencillas
col_m1, col_m2, col_m3 = st.columns(3)
total_libros = len(st.session_state.biblio.libros)
disponibles = sum(1 for l in st.session_state.biblio.libros if l.disponible)
prestados = total_libros - disponibles

col_m1.metric("Total Registrados", total_libros)
col_m2.metric("Disponibles", disponibles)
col_m3.metric("En Préstamo", prestados)

st.divider()

# --- SECCIÓN 1: CATÁLOGO ---
if opcion == " Catálogo de Libros":
    st.subheader(" Catálogo Actual")
    libros = st.session_state.biblio.libros
    
    if not libros:
        st.info("No hay libros registrados en la biblioteca.")
    else:
        # Mostramos los libros organizados en tarjetas limpia de 2 columnas
        cols = st.columns(2)
        for i, libro in enumerate(libros):
            with cols[i % 2]:
                with st.container(border=True):
                    st.markdown(f"### {libro.titulo}")
                    st.write(f"**Autor:** {libro.autor}")
                    st.write(f"**Código ID:** `{libro.codigo}`")
                    
                    if hasattr(libro, 'formato'):
                        st.write(f"**Formato:** {libro.formato}")
                    
                    if libro.disponible:
                        st.success(" Disponible")
                    else:
                        st.error("Prestado")

# --- SECCIÓN 2: REGISTRAR LIBRO ---
elif opcion == " Registrar Libro":
    st.subheader("Añadir un Nuevo Libro")
    
    tipo = st.selectbox("Tipo de Libro:", ["Libro Físico", "Libro Digital"])
    
    with st.form("form_nuevo"):
        col1, col2 = st.columns(2)
        with col1:
            titulo = st.text_input("Título")
            autor = st.text_input("Autor")
        with col2:
            codigo = st.text_input("Código / ISBN")
            formato = st.text_input("Formato (ej. PDF, EPUB)") if tipo == "Libro Digital" else None
            
        btn_guardar = st.form_submit_button(" Guardar en la Biblioteca", type="primary")
        
        if btn_guardar:
            if titulo and autor and codigo:
                if tipo == "Libro Digital":
                    nuevo = LibroDigital(titulo, autor, codigo, formato or "PDF")
                else:
                    nuevo = Libro(titulo, autor, codigo)
                
                st.session_state.biblio.agregar(nuevo)
                st.success(f"¡El libro '{titulo}' fue registrado con éxito!")
                st.rerun()
            else:
                st.warning("Por favor completa los campos requeridos.")

# --- SECCIÓN 3: BUSCAR Y PRESTAR ---
elif opcion == "🔍 Buscar & Prestar":
    st.subheader("Gestión de Préstamos")
    
    codigo_buscar = st.text_input("Ingrese el Código del Libro a Buscar:")
    
    if codigo_buscar:
        encontrado = st.session_state.biblio.buscar(codigo_buscar)
        if encontrado:
            st.success(f"¡Libro Encontrado: **{encontrado.titulo}**!")
            
            with st.container(border=True):
                st.write(f"**Autor:** {encontrado.autor}")
                st.write(f"**Estado:** {' Disponible' if encontrado.disponible else ' Prestado'}")
                
                col_b1, col_b2 = st.columns(2)
                with col_b1:
                    if st.button(" Solicitar Préstamo", use_container_width=True):
                        if encontrado.prestar():
                            st.success("¡Préstamo realizado exitosamente!")
                            st.rerun()
                        else:
                            st.warning("Este libro ya está prestado.")
                with col_b2:
                    if st.button("↩Devolver Libro", use_container_width=True):
                        encontrado.devolver()
                        st.success("¡El libro ha sido devuelto!")
                        st.rerun()
        else:
            st.error("No se encontró ningún libro con ese código.")