def choose_level(n_pregunta, p_level):
    """
    Permite escoger el nivel de dificultad de la pregunta a realizar
    
    Args: 
        n_pregunta(int): Número de la pregunta
        p_level(int): Nivel de preguntas por dificultad del cuestionario(1, 2 o 3)
    Returns:
        level(str): Nivel de dificultad de la pregunta (basica, intermedia o avanzada)

    >p_level = 1:
        >primera pregunta: basica
        >segunda pregunta: intermedia
        >tercera pregunta: avanzada
    >p_level = 2:
        >pregunta 1 y 2: basica
        >pregunta 3 y 4: intermedia
        >pregunta 5 y 6: avanzada
    >p_level = 3:
        >pregunta 1, 2 y 3: basica
        >pregunta 4, 5 y 6: intermedia
        >pregunta 7, 8 y 9: avanzada
    """
    
    if p_level == 1:
        if n_pregunta in [1]:
            level='basicas'
        elif n_pregunta in [2]:
            level='intermedias'
        else:
            level='avanzadas'
    if p_level == 2:
        if n_pregunta in [1,2]:
            level='basicas'
        elif n_pregunta in [3,4]:
            level='intermedias'
        else:
            level='avanzadas'
    if p_level == 3:
        if n_pregunta in [1,2,3]:
            level='basicas'
        if n_pregunta in [4,5,6]:
            level='intermedias'
        else:
            level='avanzadas'
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias