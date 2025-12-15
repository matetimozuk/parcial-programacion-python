def get_int(mensaje):
    '''
    Solicita un numero entero al usuario con validacion.
    '''
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: tenes que ingresar un numero entero.")

def mostrar(mensaje):
    '''
    Muestra un mensaje al usuario.
    reemplazo del print.
    '''
    input(mensaje)