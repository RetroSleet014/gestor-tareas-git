
def main():
    print("¡Bienvenido al Gestor de Tareas!")

def guardar_tarea():
    with open("tareas.txt", "a") as archivo:
        tarea = input("Escribe una nueva tarea: ")
        archivo.write(tarea + "\n")
        print("Tarea guardada.\n")

if __name__ == "__main__":
    main()

