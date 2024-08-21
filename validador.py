
def validate(opciones, eleccion):
    """Confirma si un valor se encuentra dentro de un conjunto de opciones

    Args: 
        opciones(arr): Opciones disponibles para elegir
        elección(str): Opción elegida
    Returns:
        eleccion(str): Opción elegida y validada

    Esta función provee un mensaje de opción inválida al usuario y se ejecuta hasta que el usuario ingrese una opción valida.
    """

    while eleccion not in opciones: #exluye las opciones que no sean 0 o 1
            print("Opción no válida, ingrese una de las opciones válidas:")
            eleccion = input("Ingresa una Opción: ").lower() #pide input nuevamente luego del mensaje de error
    
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
