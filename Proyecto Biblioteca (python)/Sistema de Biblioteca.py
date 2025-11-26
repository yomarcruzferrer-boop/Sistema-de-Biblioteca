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
    categoria = input("Ingrese la categoría del libro: ").strip().capitalize()
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
    print(f"El libro '{titulo}' ha sido agregado a la categoría '{categoria}' exitosamente.")

def listar_catalogo(catalogo):
    """
    Imprime el catálogo completo de libros, organizado por categorías.
    Muestra título, autor, año y estado de disponibilidad.
    """
    print("\n=======================================================")
    print("           📚 CATÁLOGO GENERAL DE LIBROS 📚            ")
    print("=======================================================")
    
    # Si el catálogo principal está vacío, salimos.
    if not catalogo:
        print("El catálogo está completamente vacío.")
        return

    total_libros_general = 0
    
    # 1. Iterar sobre las categorías (las claves del diccionario)
    for categoria, lista_libros in catalogo.items():
        
        num_libros_categoria = len(lista_libros)
        total_libros_general += num_libros_categoria
        
        # Imprimir el encabezado de la categoría
        print(f"\n--- 📖 CATEGORÍA: {categoria} ({num_libros_categoria} Títulos) ---")
        
        if not lista_libros:
            print("  (No hay libros registrados en esta categoría.)")
            continue
            
        # 2. Iterar sobre los libros (la lista de diccionarios) dentro de la categoría
        for i, libro in enumerate(lista_libros, 1):
            
            # Definir el estado para mostrarlo con claridad
            estado = "✅ DISPONIBLE" if libro.get("disponible", False) else "❌ PRESTADO"
            
            # 3. Imprimir los detalles del libro
            print(f"  {i}. Título: {libro['titulo']}")
            print(f"     Autor: {libro['autor']} | Año: {libro['año']} | Estado: {estado}")
            
    print("\n=======================================================")
    print(f"RESUMEN: Total de libros en el catálogo: {total_libros_general}")
    print("=======================================================")