import os
from utils.validations import CategoryValidation
from commands.command import Command


class ShowCategories(Command):
    def execute(self, ruta):
        directorio = list(os.scandir(ruta))
        if not directorio:
            print("No tienes recetas en el archivo")
            return False
        else:
            print("Tienes estas categorías: ")
            for categoria in directorio:
                if categoria.is_dir():
                    print(f"- {categoria.name}")
            return True


class CreateCategory(Command):
    def execute(self, ruta):
        opcion = input("Ingrese el nombre de la nueva categoría: ")
        nuevaCategoria = os.path.join(ruta, opcion)
        if not CategoryValidation().validate(ruta, opcion):
            os.makedirs(nuevaCategoria)
            print("Nueva categoría creada")
        else:
            print("La categoría ya existe")


class DeleteCategory(Command):
    def execute(self, ruta):
        opcion = input("Ingrese el nombre de la categoría a eliminar: ")
        nuevaCategoria = os.path.join(ruta, opcion)
        if CategoryValidation().validate(ruta, opcion):
            os.rmdir(nuevaCategoria)
            print(f"Categoría {opcion} eliminada.")
        else:
            print("No existe esa categoría o ya fue eliminada")
