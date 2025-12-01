#Para que los datos se queden guardados
import json
import os

                            #-ESTRUCTURA DE DATOS Y REGISTRO DE LIBROS- (PARTE DE YOMAR) -
#Catalogos de Libros
catalogo_principal = {
    "Clasicos": [
        {"titulo": "Don Quijote de la Mancha",
         "autor": "Miguel de Cervantes",
         "año": "1605",
         "disponible": True
         },
         {"titulo": "Cien años de soledad",
         "autor": "Gabriel García Márquez",
         "año": "1967",
         "disponible": True
         },
         {"titulo": "El Principito",
          "autor": "Antoine de Saint-Exupéry",
          "año": "1943",
          "disponible": True
         },
         {"titulo": "La Odisea",
          "autor": "Homero",
          "año": "Siglo VIII a.C.",
          "disponible": True
         },
         {"titulo": "Moby Dick",
         "autor": "Herman Melville",
         "año": "1851",
         "disponible": True
         }
    ],
    "Ciencia Ficción": [
        {"titulo": "Dune",
         "autor": "Frank Herbert",
         "año": "1965",
         "disponible": True
         },
         {"titulo": "Neuromante",
          "autor": "William Gibson",
          "año": "1984",
          "disponible": True
         },
         {"titulo": "Fundación",
          "autor": "Isaac Asimov",
          "año": "1951",
          "disponible": True
         },
         {"titulo": "Metro",
          "autor": "Dmitry Glukhovsky",
          "año": "2005",
          "disponible": True
         },
         {"titulo": "Frankenstein",
          "autor": "Mary Shelley",
          "año": "1818",
          "disponible": True
         }
    ],
    "Terror/Thriller": [
        {"titulo": "El resplandor",
         "autor": "Stephen King",
         "año": "1977",
         "disponible": True
         },
        {"titulo": "Dexter",
         "autor": "Jeff Lindsay",
         "año": "2004",
         "disponible": True
         },
        {"titulo": "El necrófilo",
         "autor": "Gabrielle Wittkop",
         "año": "1972",
         "disponible": True
         },
         
        {"titulo": "Cementerio de animales",
         "autor": "Stephen King",
         "año": "1983",
         "disponible": True
         },
        {"titulo": "El exorcista",
         "autor": "William Peter Blatty",
         "año": "1977",
         "disponible": True
         }
    ],
    "Comics/Manga": [
        {"titulo": "Cowbow Bebop",
         "autor": "Yutaka Nanten",
         "año": "2006",
         "disponible": True
         },
        {"titulo": "Jojo's Bizarre Adventure",
         "autor": "Hirohiko Araki",
         "año": "1987",
         "disponible": True
         },
        {"titulo": "Invensible",
         "autor": "Robert Kirkman",
         "año": "2007",
         "disponible": True
         },
        {"titulo": "All star superman",
         "autor": "Grant Morrison",
         "año": "2008",
         "disponible": True
         },
        {"titulo": "Akira",
         "autor": "Katsuhiro Otomo",
         "año": "1988",
         "disponible": True
         }
    ],
    "Fantasia": [
         {"titulo": "The Sandman",
         "autor": "Neil Gaiman",
         "año": "1987",
         "disponible": True
         },
        {"titulo": "The Witcher",
         "autor": "Andrzej Sapkowski",
         "año": "1993",
         "disponible": True
         },
        {"titulo": "El nseñor de los anillos",
         "autor": "J.R.R. Tolkien",
         "año": "1954",
         "disponible": True
         },
        {"titulo": "La rueda del tiempo",
         "autor": "Robert Jordan",
         "año": "1982",
         "disponible": True
         },
        {"titulo": "El hobbit",
         "autor": "J.R.R. Tolkien",
         "año": "1937",
         "disponible": True
         }
    ],
}
#Funcion para agregar libros y crear catalogos, para el usuario
def agregar_libro(catalogo):
    print ("Agregar un nuevo libro al catálogo")
    categoria = input("Ingrese la categoría del libro. Si la categoría no existe, se creará una nueva categoría👀: ").strip().capitalize()
    titulo = input("Ingrese el título del libro: ").strip()
    autor = input("Ingrese el autor del libro: ").strip()
    año = input("Ingrese el año del libro: ").strip()
    if not titulo or not autor or not año or not categoria:
        print("Error: Todos los campos solicitados son obligatorios.")
        return

#Crear el nuevo libro
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "disponible": True
    }

    #Si la categoria no existe, para crearla
    if categoria not in catalogo:
        catalogo[categoria] = []
        print(f"La categoria {categoria} no existia, se ha creado una nueva categoria.")
    #Agrega el diccionario del libro a la categoria correspondiente
    catalogo[categoria].append(nuevo_libro)
    print(f"El libro '{titulo}' ha sido agregado a la categoría '{categoria}' exitosamente👍.")

def listar_catalogo(catalogo): #Imprime el catálogo completo de libros, organizado por categorías.
    #Muestra título, autor, año y estado de disponibilidad.
    print("\n=======================================================")
    print("           📚 CATÁLOGO GENERAL DE LIBROS 📚            ")
    print("=======================================================")
    
    # Si el catálogo principal está vacío, se sale.
    if not catalogo:
        print("El catálogo está vacio :(")
        return

    total_libros_general = 0
    
    # 1. Itera sobre las categorías (las claves del diccionario)
    for categoria, lista_libros in catalogo.items():
        
        num_libros_categoria = len(lista_libros)
        total_libros_general += num_libros_categoria
        
        # Imprime el encabezado de la categoría
        print(f"\n--- 📖 CATEGORÍA: {categoria} ({num_libros_categoria} Títulos) ---")
        
        if not lista_libros:
            print("No hay libros registrados en esta categoría.")
            continue
            
        # 2. Itera sobre los libros (la lista de diccionarios) dentro de la categoría
        for i, libro in enumerate(lista_libros, 1):
            # Define el estado para mostrarlo
            estado = "✅ DISPONIBLE" if libro.get("disponible", False) else "❌ PRESTADO"
            # 3. Imprime los detalles del libro
            print(f"  {i}. Título: {libro['titulo']}")
            print(f"     Autor: {libro['autor']} | Año: {libro['año']} | Estado: {estado}")
    print("\n=======================================================")
    print(f"RESUMEN: Total de libros en el catálogo: {total_libros_general}")
    print("=======================================================")
    

                        # — PRÉSTAMOS, DEVOLUCIONES Y DISPONIBILIDAD - (PARTE DE SIGNY) -
def _buscar_libro(catalogo, titulo_buscado): #Función para buscar un libro por título, retorna al diccionario si existe, o None si no.
    for lista_libros in catalogo.values(): # Recorre el diccionario
        for libro in lista_libros:
            if libro["titulo"].strip().lower() == titulo_buscado.strip().lower():
                return libro
    return None

def prestar_libro(catalogo): #Solicita un título al usuario y gestiona el préstamo cambiando la disponibilidad.
    print("\n--- 📖 SOLICITAR PRÉSTAMO DE LIBROS ---")
    titulo = input("Ingrese el título del libro que desea usar: ").strip()
    if not titulo:
        print("❌ Error: Debe de ingresar el nombre del título.")
        return
    #Para buscar
    libro = _buscar_libro(catalogo, titulo)
    if libro: # Verifica si está disponible
        if libro["disponible"]:
            libro["disponible"] = False
            print(f"✅Has pedido prestado el libro: '{libro['titulo']}'.")
        else:
            print(f"⚠️ El libro '{libro['titulo']}' ya se encuentra prestado actualmente.")
    else:
        print(f"❌ Error: No encontramos el libro '{titulo}' en el catálogo.")

def devolver_libro(catalogo): #Solicita un título al usuario y lo devuelve.
    print("\n--- ↩️ DEVOLUCION DE LIBROS ---")
    titulo = input("Ingrese el título del libro que desea devolver: ").strip()
    if not titulo:
        print("❌ Error: Debe de ingresar el nombre del título.")
        return
    #Buscar el libro (de nuevo xd)
    libro = _buscar_libro(catalogo, titulo)
    if libro:
        if not libro["disponible"]: # Verifica si no está disponible
            libro["disponible"] = True
            print(f"✅ ¡Gracias! Has devuelto el libro: '{libro['titulo']}'.")
        else:
            print(f"⚠️ El libro '{libro['titulo']}' ya está disponible.")
    else:
        print(f"❌ Error: No encontramos el libro '{titulo}' en el catálogo para devolverlo.")

                               #-REPORTES Y ESTADISTICAS- (PARTE DE ANGEL) -
def mostrar_libros_disponibles(catalogo): #Genera un reporte de todos los libros que están disponibles.
    print("\n=======================================")
    print("   📊 REPORTE DE LIBROS DISPONIBLES    ")
    print("=======================================")
    
    hay_disponibles = False
    
    # Recorre las categorías y listas de libros
    for categoria, lista_libros in catalogo.items(): #Filtra solo los libros disponibles en esta categoría
        libros_cat_disponibles = [libro for libro in lista_libros if libro.get("disponible", True)]
        if libros_cat_disponibles:
            hay_disponibles = True
            print(f"\n📂 Categoría: {categoria}")
            for libro in libros_cat_disponibles:
                print(f"   - {libro['titulo']} (Autor: {libro['autor']})")

    if not hay_disponibles:
        print("\n⚠️ No hay libros disponibles en este momento. Todos están prestados")
    print("\n---------------------------------------")


def mostrar_libros_prestados(catalogo): #Genera un reporte de todos los libros que están prestados.
    print("\n=======================================")
    print("    📊 REPORTE DE LIBROS PRESTADOS     ")
    print("=======================================")
    
    hay_prestados = False
    
    for categoria, lista_libros in catalogo.items(): #Filtra solo los libros que no están disponibles (prestados)
        libros_cat_prestados = [libro for libro in lista_libros if not libro.get("disponible", True)]
        if libros_cat_prestados:
            hay_prestados = True
            print(f"\n📂 Categoría: {categoria}")
            for libro in libros_cat_prestados:
                print(f" - {libro['titulo']} (Año: {libro['año']})")
    if not hay_prestados:
        print("\n🎉 No se encuentran libros prestados. Todo el catalogo está en la biblioteca.")
    print("\n---------------------------------------")

def generar_estadisticas_uso(catalogo): #Calcula las estadísticas (total de libros, prestados y % de ocupación)
    print("\n=======================================")
    print("      📈 ESTADÍSTICAS DE LA BIBLIOTECA  ")
    print("=======================================")
    
    total_libros = 0
    total_prestados = 0
    
    # Recorrido para conteo
    for lista_libros in catalogo.values():
        total_libros += len(lista_libros)
        for libro in lista_libros:
            if not libro.get("disponible", True):
                total_prestados += 1
    
    # Para calcular
    total_disponibles = total_libros - total_prestados
    
    if total_libros > 0:
        porcentaje_ocupacion = (total_prestados / total_libros) * 100
        porcentaje_disponibilidad = (total_disponibles / total_libros) * 100
    else:
        porcentaje_ocupacion = 0.0
        porcentaje_disponibilidad = 0.0

    # Imprime los resultados
    print(f"📚 Total de Libros en Catálogo:  {total_libros}")
    print(f"❌ Libros Prestados:             {total_prestados}")
    print(f"✅ Libros Disponibles:           {total_disponibles}")
    print("---------------------------------------")
    print(f"📊 Porcentaje de Préstamos:      {porcentaje_ocupacion:.2f}%")
    print(f"📊 Porcentaje de Disponibilidad: {porcentaje_disponibilidad:.2f}%")
    print("=======================================")

                             #-EXTRAS Y PERSISTENCIA DE DATOS- (PARTE DE GABRIELA) -
NOMBRE_ARCHIVO = "datos_biblioteca.json"

def guardar_catalogo_archivo(catalogo): #guarda el diccionario del catálogo en un archivo JSON.
    try:
        with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as archivo:
            json.dump(catalogo, archivo, indent=4, ensure_ascii=False)
        print(f"\n💾 ¡Datos guardados exitosamente en '{NOMBRE_ARCHIVO}'!")
    except Exception as e:
        print(f"\n❌ Error al guardar el archivo: {e}")


def cargar_catalogo_archivo(catalogo_por_defecto): #Intenta cargar el catálogo desde el archivo JSON.
    #Si el archivo no existe, retorna el catálogo por defecto (el que está en el código.

    if os.path.exists(NOMBRE_ARCHIVO):
        try:
            with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as archivo:
                datos_cargados = json.load(archivo)
            print(f"\n📂 Se han cargado los datos previos desde '{NOMBRE_ARCHIVO}'.")
            return datos_cargados
        except Exception as e:
            print(f"⚠️ Error al leer el archivo (se usará el catálogo por defecto): {e}")
            return catalogo_por_defecto
    else:
        print("\n🆕 No se encontró archivo previo. Se inicia con el catálogo por defecto.")
        return catalogo_por_defecto


def menu_principal(): #controla el flujo del programa y conecta las funciones de las Personas 1, 2 y 3.
    #Cargar datos al iniciar
    mi_catalogo = cargar_catalogo_archivo(catalogo_principal)

    while True:
        print("\n=============================================")
        print("      🏛️  SISTEMA DE GESTIÓN DE BIBLIOTECA    ")
        print("=============================================")
        print("1.  📜  Listar Catálogo Completo")
        print("2.  ➕  Agregar Nuevo Libro")
        print("3.  🤝  Solicitar un Libro")
        print("4.  ↩️  Devolver Libro")
        print("5.  📊  Reporte: Libros Disponibles")
        print("6.  📊  Reporte: Libros Prestados")
        print("7.  📈  Estadísticas Generales")
        print("8.  💾  Guardar y Salir")
        print("---------------------------------------------")
        
        opcion = input("👉 Seleccione una opción (1-8): ").strip()

        if opcion == '1':
            listar_catalogo(mi_catalogo)
            
        #guardar_catalogo_archivo(mi_catalogo) 
        elif opcion == '2':
            agregar_libro(mi_catalogo) #guarda automáticamente después de agregar
        
        elif opcion == '3':
            prestar_libro(mi_catalogo)
        
        elif opcion == '4':
            devolver_libro(mi_catalogo)
        
        elif opcion == '5':
            mostrar_libros_disponibles(mi_catalogo)
        
        elif opcion == '6':
            mostrar_libros_prestados(mi_catalogo)
            
        elif opcion == '7':
            generar_estadisticas_uso(mi_catalogo)
            
        elif opcion == '8':
            print("\nGuardando cambios...")
            guardar_catalogo_archivo(mi_catalogo)
            print("👋 ¡Gracias por usar el papusistemas biblioteca! Hasta pronto.")
            break
        else:
            print("❌ Opción no válida. Por favor ingrese del 1 hasta el 8.")

if __name__ == "__main__":
    menu_principal()