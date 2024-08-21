import preguntas as p


def verificar(alternativas, eleccion):
    """Permite verificar si la elección ingresada por el usuario es la correcta
    
    Args:
        alternativas(arr): alternativas aleatorizadas
        elección (str): alternativa escogida por el usuario
    Returns: 
        correcto (int):"""
    
    eleccion_index = ['a', 'b', 'c','d'].index(eleccion)

    #verificar si la eleccion es correcta
    correcto = alternativas[eleccion_index][1] == 1
    
    return correcto



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






