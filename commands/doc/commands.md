# Command (Recetas)

en esta clase pense en manejar las diferentes opciones que se pueden realizar en el sistema
por ejemplo crear una categoría, eliminar una categoría, crear una receta, eliminar una Recetas
lo que en cierta parte se puede resumir en comandos y centralizarlos en una clase

## Patron de diseño

```mermaid
classDiagram
    class Command{
        +execute(ruta)
    }
    class ShowCategories{
        +execute(ruta)
    }
    class CreateCategory{
        +execute(ruta)
    }
    class DeleteCategory{
        +execute(ruta)
    }
    class ShowRecipes{
        +execute(ruta)
    }
    class CreateRecipe{
        +execute(ruta)
    }
```

el patrón asi como en la clase User es el patrón de diseño Command
al igual que en la clase User, el código se vuelve más modular y fácil de entender y es mucho mas flexible
