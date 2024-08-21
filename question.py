import preguntas as p
import random
from shuffle import shuffle_alt


opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}


def choose_q(dificultad):
    """Permite escoger las preguntas de preguntas.py de acuerdo al nivel de dificultad escogida,
    luego elimina la opción escogida del ambiente global
    y entrega el enunciado de la pregunta con sus alternativas mezcladas
    
    Args:
        dificultad(str): nivel de dificultad escogido para la pregunta (basico, intermedio o avanzado)
    Returns:
        pregunta(str): enunciado de la pregunta
        alternativas(arr): alternativas aleatorizadas de la pregunta
        """
    #escoger preguntas por dificultad
    preguntas = list(p.pool_preguntas[dificultad].keys())
    # usar opciones desde ambiente global
    global opciones
    # escoger una pregunta
    n_elegido = random.choice(opciones[dificultad])
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)
    # escoger enunciado y alternativas mezcladas
    pregunta = p.pool_preguntas[dificultad][f'pregunta_{n_elegido}']
    alternativas = shuffle_alt(pregunta)
        
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')