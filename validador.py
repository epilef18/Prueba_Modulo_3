
def validate(opciones, eleccion):

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
    
    
