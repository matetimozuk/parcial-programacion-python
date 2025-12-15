import funciones
from validaciones import get_int, mostrar

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Cargar notas")
        print("2. Calcular nota final de cada division")
        print("3. Mostrar division(es) con menor nota trimestral")
        print("4. Mostrar promedio de notas finales")
        print("5. Mostrar division con mayor nota final")
        print("6. Mostrar trimestre con mas nota total")
        print("7. Informe ordenado por nota final")
        print("8. Salir")

        opcion = input("Selecciona una opcion: ")


        if opcion == "1":
            funciones.cargar_notas()
        elif opcion == "2":
            funciones.calcular_promedios_finales()
        elif opcion == "3":
            funciones.mostrar_menor_nota_trimestral()
        elif opcion == "4":
            funciones.mostrar_promedio_general()
        elif opcion == "5":
            funciones.mostrar_division_con_mayor_final()
        elif opcion == "6":
            funciones.mostrar_trimestre_mas_nota()
        elif opcion == "7":
            funciones.informe_ordenado()
        elif opcion == "8":
            print("Fin del programa.")
            break
        else:
            print("Opcion invalida. Intenta de nuevo.")


menu()