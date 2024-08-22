import os

#Cantidad de carpetas en dicha carpeta de Recetas
def cantidadRecetas(ruta):
    directorio = os.scandir(ruta)
    cantidad = 0
    for carpeta in directorio:
        cantidad += 1
    return cantidad

# Mostrar categorias
def showCate(ruta):
    directorio = list(os.scandir(ruta))
    if not directorio:
        print("No tienes recetas en el archivo")
        return False
    else:
        print("Tienes estas categorias: ")
        for categoria in directorio:
            if categoria.is_dir():
                print(f"- {categoria.name}")
        print("¿Qué categoría eliges?")
        return True

# Mostrar recetas
def showRecet(ruta):
    directorio = list(os.scandir(ruta))
    if not directorio:
        print("No tienes recetas en el archivo")
        return False
    else:
        print("Tienes estas recetas: ")
        for receta in directorio:
            if receta.is_file() and receta.name.endswith(".txt"):
                print(f"- {receta.name[:-4]}")
        print("¿Qué receta eliges?")
        return True


#Validar ¿Existe esa categoria?
def validCate(direct, categoria):
    directorio = os.scandir(direct)
    for archivo in directorio:
        if categoria == archivo.name:
            return True
    return False

#Validar ¿Existe esa receta?
def validRecet(direct,receta,eleccion):
    directorio = os.scandir(direct)
    if eleccion == 1:
        for archivo in directorio:
            if (receta + ".txt" == archivo.name):
                abrir_leer(os.path.join(direct, archivo.name))  # Pasar la ruta completa a abrir_leer
                return True
        return False
    else:
        for archivo in directorio:
            if (receta + ".txt" == archivo.name):
                os.remove(os.path.join(direct, archivo.name))
                return True
        return False


#Leer archivos
def abrir_leer(archivo):
    with open(archivo, "r") as contenido: #Garantiza que se cierre el archivo
        print(contenido.read())

#Crear archivo para la receta
def crearRecet(archivo):
    with open(archivo, "x") as contenido: #Garantiza que se cierre el archivo
        print(contenido.read())

#Escribir en el documento
def escribirDoc(archivo):
    with open(archivo,"a") as contenido:
        print("Ingrese las indicaciones de dicha receta")
        texto = input()
        contenido.write(texto)
        return contenido

#Leer recetas
def showElement(ruta):
    opcion = input("Ingrese el nombre de la categoria: ")
    nuevoDirectorio = os.path.join(ruta, opcion)
    if validCate(ruta, opcion):
        if not showRecet(nuevoDirectorio):
            return  # Volvemos al menú si no hay recetas
        ver = input("Ingrese el nombre de la receta que desea leer: ")
        if not validRecet(nuevoDirectorio, ver, 1):
            print("No se encontró dicha receta.")
            return showElement(ruta)
    else:
        print("No se encontro dicha categoria.")
        return showElement(ruta)

#Desarrollando la opcion 2
#Crear receta
def crearReceta(ruta):
    opcion = input("Ingrese el nombre de la categoria: ")
    nuevoDirectorio = os.path.join(ruta, opcion)
    if validCate(ruta, opcion):
        nombreReceta = input(f"Ingrese el nombre de la nueva receta para la categoria {opcion}: ")
        recetaNuevaArch = os.path.join(nuevoDirectorio, nombreReceta + ".txt")
        escribirDoc(recetaNuevaArch)
        abrir_leer(recetaNuevaArch)
        return
    else:
        print("Ingrese una categoria correcta")
        return

#Desarrollando la opcion 3
#Crear categoria
def crearCategoria(ruta):
    opcion = input("Ingrese el nombre de la categoria: ")
    nuevaCategoria = os.path.join(ruta, opcion)
    if not validCate(ruta,opcion):
        os.makedirs(nuevaCategoria)
        print("Nueva categoria creada")
    else:
        print("Ya existe dicha categoria")
        return

#Eliminar receta
def deletRecet(ruta):
    opcion = input("Ingrese el nombre de la categoria: ")
    categoriaSelec = os.path.join(ruta, opcion)
    if validCate(ruta, opcion):
        showRecet(categoriaSelec)
        ver = input("Ingrese el nombre de la receta que desea eliminar: ")
        if validRecet(categoriaSelec, ver, 0):
            print("Receta eliminada: " + ver)
            return
        else:
            print("No se encontro dicha receta.")
            return showElement(ruta)
    else:
        print("No se encontro dicha categoria.")
        return showElement(ruta)
#Eliminar categoria
def deletCate(ruta):
    opcion = input("Ingresa la categoria que desea eliminar: ")
    nuevoDirectorio = os.path.join(ruta, opcion)
    if validCate(ruta, opcion):
        os.rmdir(nuevoDirectorio)
        print(f"Categoria eliminada: {opcion}")
    else:
        print("No existe esa categoria o fue eliminada con anterioridad")
        return
#Menu para acceder a las recetas
def menuRecetas(opcion, ruta):
    match opcion:
        case 1:
            os.system('cls')
            showCate(ruta)
            showElement(ruta)
        case 2:
            os.system('cls')
            showCate(ruta)
            crearReceta(ruta)
        case 3:
            os.system('cls')
            crearCategoria(ruta)
        case 4:
            os.system('cls')
            showCate(ruta)
            deletRecet(ruta)
        case 5:
            os.system('cls')
            showCate(ruta)
            deletCate(ruta)
        case 6:
            os.system('cls')
            print("Hasta luego ten un buen día")
            return True
        case _:
            print("Seleccione una opcion valida!")

#Eleccion usuario
def interactUser(ruta):
    while True:
        try:
            eleccion = int(input("Elige una opción: \n1. Elegir categoria de alimentos que desee leer.\n2. Elegir categia y crear receta.\n3. Crear nueva categoria. \n4. Eliminar receta.\n5. Eliminar categoria.\n6. Salir.\nTu opción es: "))
            os.system('cls')
            if menuRecetas(eleccion, ruta):
                break

        except ValueError:
            print("Por favor ingrese un numero valido")


print("Bienvenido usuario")
#Informar la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas
rutaRecetas = "M:\\Programas en Python\\Python\\Día 6\\Recetas"

print(f"Te comento que la carpeta de recetas se encuentra en: {rutaRecetas}")

numReceta = cantidadRecetas(rutaRecetas)
print(f"La cantidad de recetas: {numReceta}")

#Para interactuar con el usuario
interactUser(rutaRecetas)


