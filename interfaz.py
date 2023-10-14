# Python Inicial [Python]
# Ejercicio integrador

# Autor: Inove Coding School
# Version: 2.0

imagenes = [
    '''    
    |   |
        |
        |
        |
        |
        =''',
    '''
    
    |   |
    O   |
        |
        |
        |
        =''',
    '''
    
    |   |
    O   |
    |   |
        |
        |
        =''',
    '''
    
    |   |
    O   |
   /|   |
        |
        |
        =''',
    '''
    
    |   |
    O   |
   /|\  |
        |
        |
        =''',
    '''
   
    |   |
    O   |
   /|\  |
    |   |
        |
        =''',
    '''
    
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =''',
    '''
    
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        ='''
]

def dibujar(palabra_secreta, lista_letras_usadas, intentos_invalidos):

    palabra_oculta = ['_.'] * len(palabra_secreta)

    for letra in lista_letras_usadas:

        if letra in palabra_secreta:
            for i in range(len(palabra_secreta)):

                if palabra_secreta[i] == letra:
                    palabra_oculta[i] = letra + "."


    print(imagenes[min(intentos_invalidos, len(imagenes)-1)])
    print("Palabra secreta:")
    print("".join(palabra_oculta))
    print("Letras utilizadas:")
    print(lista_letras_usadas)
    return palabra_oculta

if __name__ == "__main__":

    palabra_secreta = "palabra"
    lista_letras_usadas = ["a", "p", "l", "b", "r"]
    dibujar(palabra_secreta, lista_letras_usadas, 3)

