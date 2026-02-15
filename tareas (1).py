
# Lista inicial de tareas
tareas = []

# Función para guardar las tareas en un archivo
def guardar_tareas():
    with open("tareas.txt", "w") as archivo:
        for texto, hecho in tareas:  # cada sublista tiene exactamente 2 elementos
            archivo.write(f"{texto}|{hecho}\n")

# Intentar cargar tareas previas si existe el archivo
try:
    with open("tareas.txt", "r") as archivo:
        tareas = []
        for linea in archivo:
            partes = linea.strip().split("|")
            if len(partes) == 2:  # solo agregamos si hay exactamente 2 elementos
                texto, hecho = partes
                tareas.append([texto, hecho == "True"])
except FileNotFoundError:
    pass  # Si no existe el archivo, seguimos con la lista inicial

# Menú principal
while True:
    print("\n--- LISTA DE TAREAS ---")
    print("1 - Agregar tarea")
    print("2 - Ver tareas")
    print("3 - Borrar tarea")
    print("4 - Marcar tarea como hecha")
    print("5 - Salir")
    
    opcion = input("Elija una opción: ")

    # Opción 1: Agregar tarea
    if opcion == "1":
        nueva_tarea = input("Ingrese la tarea que desea agregar: ")
        tareas.append([nueva_tarea, False])  # siempre 2 elementos
        guardar_tareas()
        print("Tarea agregada.")

    # Opción 2: Ver tareas
    elif opcion == "2":
        print("\n--- TAREAS ---")
        for i, (texto, hecho) in enumerate(tareas, 1):
            estado = "✔" if hecho else " "
            print(f"{i}. [{estado}] {texto}")

# Opción 3: Borrar tarea
    elif opcion == "3":
        print("\n--- BORRAR TAREA ---")
        for i, (texto, hecho) in enumerate(tareas, 1):
            estado = "✔" if hecho else " "
            print(f"{i}. [{estado}] {texto}")
        try:
            numero = int(input("Ingrese el número de la tarea que desea borrar: "))
            tareas.pop(numero - 1)
            guardar_tareas()
            print("Tarea eliminada.")
        except (ValueError, IndexError):
              print("Número inválido.")

    # Opción 4: Marcar tarea como hecha
    elif opcion == "4":
        print("\n--- MARCAR TAREA COMO HECHA ---")
        for i, (texto, hecho) in enumerate(tareas, 1):
            estado = "✔" if hecho else " "
            print(f"{i}. [{estado}] {texto}")
        try:
            numero = int(input("Ingrese el número de la tarea que desea marcar como hecha: "))
            tareas[numero - 1][1] = True
            guardar_tareas()
            print("Tarea marcada como hecha.")
        except (ValueError, IndexError):
            print("Número inválido.")

    # Opción 5: Salir
    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción inválida. Intente nuevamente.")  print("Opción inválida. Intente nuevamente.")