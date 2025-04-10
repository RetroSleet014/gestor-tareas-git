

def guardar_tarea():
    with open("tareas.txt", "a") as archivo:
        tarea = input("Escribe una nueva tarea: ")
        archivo.write(tarea + "\n")
        print("Tarea guardada.\n")

def ver_tareas():
    print("\nTus tareas:")
    try:
        with open("tareas.txt", "r") as archivo:
            contenido = archivo.read()
            if contenido.strip():
                print(contenido)
            else:
                print("No hay tareas registradas.")
    except FileNotFoundError:
        print("No hay tareas registradas (archivo no encontrado).")

def main():
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            guardar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()

