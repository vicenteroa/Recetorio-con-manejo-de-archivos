from entities.user import User
from commands.category import ShowCategories, CreateCategory, DeleteCategory
from commands.recipes import ShowRecipes, CreateRecipe


def menu():
    # Cambia esto a la ruta adecuada
    ruta_recetas = "./Recetas/"
    user = User(None, ruta_recetas)

    while True:
        print("")
        print("RECETORIO.PY")
        print("------")
        print("1. Mostrar categorías")
        print("2. Crear categoría")
        print("3. Eliminar categoría")
        print("4. Mostrar recetas")
        print("5. Crear receta")
        print("6. Salir")
        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            user.execute_command(ShowCategories())
        elif opcion == 2:
            user.execute_command(CreateCategory())
        elif opcion == 3:
            user.execute_command(DeleteCategory())
        elif opcion == 4:
            user.execute_command(ShowRecipes())
        elif opcion == 5:
            user.execute_command(CreateRecipe())
        elif opcion == 6:
            print("Adiós")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu()
