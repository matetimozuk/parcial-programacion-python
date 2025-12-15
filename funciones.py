# En una escuela secundaria se evalúa a los alumnos a lo largo de 3 trimestres y, en una 
# planilla, se almacenan las calificaciones promediadas de todos los alumnos de una división.
# En el último año de esta institución hay 5 divisiones, siendo nombradas estas con letras de
# la A a la E.
# En la institución se busca analizar los resultados de las distintas divisiones para verificar el
# estado de los alumnos.
# Realizar un menú de opciones:
# 1. Cargar notas: Para ello se deberá crear una función que cargue cada trimestre de
# cada división.
# 2. Calcular la nota final de cada división, haciendo un promedio de las tres notas
# trimestrales de la misma.
# 3. Mostrar la división o divisiones que haya tenido la menor nota trimestral.
# 4. Mostrar el promedio de notas finales entre todas las divisiones.
# 5. Mostrar la división con más nota final.
# 6. Mostrar el trimestre que más nota haya conseguido entre las 5 divisiones.
# 7. Hacer un informe de cada división, ordenandolas de mayor a menor según su nota
# final.

from parcial1.notas_parciales.datos import divisiones, promedios_finales
from validaciones import get_int, mostrar


def cargar_notas():
    '''
    - ¿Que hace?
        - Carga las notas de los 3 trimestres para cada division.
    '''
    mostrar("--- CARGAR NOTAS ---")
    for division in divisiones:
        mostrar(f"\nIngresar notas para la division {division}")
        notas = [0, 0, 0] 
        i = 0
        while i < 3:
            nota = get_int(f"Ingrese nota del trimestre {i + 1}: ")
            if 0 <= nota <= 10:
                notas[i] = nota
                i += 1
            else:
                mostrar("La nota debe estar entre 0 y 10.")
        divisiones[division] = notas
    mostrar("Notas cargadas correctamente.")

def calcular_promedios_finales():
    '''
    - ¿Que hace?
        - Calcula el promedio final de cada division y lo guarda en un diccionario.
    '''
    mostrar("--- CALCULAR PROMEDIO FINAL ---")
    for division in divisiones:
        notas = divisiones[division]
        if len(notas) == 3:
            promedio = (notas[0] + notas[1] + notas[2]) / 3
            promedios_finales[division] = promedio
    mostrar("Promedios finales calculados.")

def mostrar_menor_nota_trimestral():
    '''
    - ¿Que hace?
        - Busca y muestra la division con la menor nota trimestral.
    '''
    mostrar("--- MENOR NOTA TRIMESTRAL ---")
    menor_nota = 11
    division_menor = ""
    for division in divisiones:
        notas = divisiones[division]
        for nota in notas:
            if nota < menor_nota:
                menor_nota = nota
                division_menor = division
    mostrar(f"La division con la menor nota trimestral es {division_menor} con la nota {menor_nota}")

def mostrar_promedio_general():
    '''
    - ¿Que hace?
        - Calcula y muestra el promedio general de los promedios finales.
    '''
    mostrar("--- PROMEDIO GENERAL DE NOTAS FINALES ---")
    total = 0
    cantidad = 0
    for division in promedios_finales:
        promedio = promedios_finales[division]
        if promedio > 0:
            total += promedio
            cantidad += 1
    if cantidad > 0:
        general = total / cantidad
        mostrar(f"Promedio general: {(general, 2)}")
    else:
        mostrar("Primero debe calcular los promedios finales.")

def mostrar_division_con_mayor_final():
    '''
    - ¿Que hace?
        - Muestra cual es la division con la mayor nota final.
    '''
    mostrar("--- DIVISIÓN CON MAYOR NOTA FINAL ---")
    mayor = -1
    division_mayor = ""
    for division in promedios_finales:
        promedio = promedios_finales[division]
        if promedio > mayor:
            mayor = promedio
            division_mayor = division
    if mayor != -1:
        mostrar(f"La division con mayor nota final es {division_mayor} con {mayor}")
    else:
        mostrar("Primero debe calcular los promedios finales.")

def mostrar_trimestre_mas_nota():
    '''
    - ¿Que hace?
        - Muestra que trimestre tuvo la mayor suma de notas entre todas las divisiones.
    '''
    mostrar("--- TRIMESTRE CON MAYOR SUMA DE NOTAS ---")
    suma_trimestres = [0, 0, 0]
    for division in divisiones:
        notas = divisiones[division]
        if len(notas) == 3:
            suma_trimestres[0] += notas[0]
            suma_trimestres[1] += notas[1]
            suma_trimestres[2] += notas[2]
    mayor_suma = suma_trimestres[0]
    trimestre = 1
    for i in range(1, 3):
        if suma_trimestres[i] > mayor_suma:
            mayor_suma = suma_trimestres[i]
            trimestre = i + 1
    mostrar(f"El trimestre con mayor suma de notas es el {trimestre} con {mayor_suma}")


def informe_ordenado():
    divisiones_orden = []
    promedios_orden = []
    for clave in promedios_finales:
        n = len(promedios_orden)
        i = 0
        while i < n and promedios_finales[clave] < promedios_orden[i]:
            i += 1
        divisiones_orden += [""]
        promedios_orden += [0]
        j = n
        while j > i:
            divisiones_orden[j] = divisiones_orden[j - 1]
            promedios_orden[j] = promedios_orden[j - 1]
            j -= 1
        divisiones_orden[i] = clave
        promedios_orden[i] = promedios_finales[clave]
    for i in range(len(divisiones_orden)):
        get_int(f"{divisiones_orden[i]} - {promedios_orden[i]}")





