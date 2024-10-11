import os
from utils.validations import CategoryValidation
from commands.command import Command


class ShowRecipes(Command):
    def execute(self, ruta):
        opcion = input("Ingrese el nombre de la categoría: ")
        nuevoDirectorio = os.path.join(ruta, opcion)

        if not CategoryValidation().validate(ruta, opcion):
            print("Categoría no encontrada. Ingrese una categoría válida.")
            return

        recetas = [receta.name for receta in os.scandir(
            nuevoDirectorio) if receta.is_file()]
        if not recetas:
            print("No hay recetas en esta categoría.")
            return

        print("Recetas en la categoría:")
        for receta in recetas:
            print(f"- {receta}")

        ver_receta = input(
            "¿Desea leer alguna receta? (sí/no o s/n): ").strip().lower()
        if ver_receta in ['sí', 's', 'si', 'yes']:
            nombre_receta = input(
                "Ingrese el nombre de la receta (sin .txt): ") + ".txt"
            receta_path = os.path.join(nuevoDirectorio, nombre_receta)

            if os.path.exists(receta_path):
                with open(receta_path, 'r') as file:
                    contenido = file.read()
                    print(f"Contenido de la receta '{nombre_receta}':")
                    print(contenido)
            else:
                print("No se encontró la receta especificada.")
        elif ver_receta in ['no', 'n']:
            print("Regresando al menú principal...")
        else:
            print("Opción no válida. Regresando al menú principal...")


class CreateRecipe(Command):
    def execute(self, ruta):
        opcion = input("Ingrese el nombre de la categoría: ")
        nuevoDirectorio = os.path.join(ruta, opcion)

        if not CategoryValidation().validate(ruta, opcion):
            print("Categoría no encontrada. Ingrese una categoría válida.")
            return

        nombreReceta = input(
            f"Ingrese el nombre de la nueva receta para la categoría '{opcion}': ")
        recetaNuevaArch = os.path.join(nuevoDirectorio, nombreReceta + ".txt")

        if os.path.exists(recetaNuevaArch):
            print("La receta ya existe. Por favor, elige otro nombre.")
            return

        with open(recetaNuevaArch, 'w') as file:
            contenido = input("Ingrese el contenido de la receta: ")
            file.write(contenido)

        print(
            f"Receta '{nombreReceta}' creada exitosamente en la categoría '{opcion}'.")
