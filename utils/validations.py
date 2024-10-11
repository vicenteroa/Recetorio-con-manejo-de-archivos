import os


class Validations:
    def validate(self, ruta, nombre):
        pass


class CategoryValidation(Validations):
    def validate(self, ruta, nombre):
        directorio = os.scandir(ruta)
        for archivo in directorio:
            if nombre == archivo.name:
                return True
        return False


class RecipeValidation(Validations):
    def validate(self, ruta, nombre):
        directorio = os.scandir(ruta)
        for archivo in directorio:
            if (nombre + ".txt") == archivo.name:
                return True
        return False
