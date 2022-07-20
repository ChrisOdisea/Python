"""
Proyecto Básico de Python (El Ahorcado).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
"""
import random   # aqui se importa la herramienta para el numero aleatorio
import string   # es para generar palabras aleatorias
from palabras import palabras  # se importa la libreria
from ahorcado_diagramas import vidas_diccionario_visual # se importa la libreria que se creo con los diccionarios


def obtener_palabra_válida(palabras): # esa clase                                                                            
    palabra = random.choice(palabras) # aqui elige una de las palabras del diccionario aleatoriamente


    while '-' in palabra or ' ' in palabra:  #se arma un ciclo while que mete palabra seleccionada a la lista
        palabra = random.choice(palabras)

    return palabra.upper()  #regresa palabra en mayusculas


def ahorcado(): #la clase de ahorcado que tiene todo el codigo

    print("=======================================")
    print(" ¡Bienvenido(a) al juego del Ahorcado! ") #se imprime el titulo del juego
    print("=======================================")

    palabra = obtener_palabra_válida(palabras)
    letras_por_adivinar = set(palabra)  
    abecedario = set(string.ascii_uppercase)  #se escribe el codigo que es para usar las listas de palabras aleatorias y definir la palabra valida
    letras_adivinadas = set()  

    vidas = 7


    while len(letras_por_adivinar) > 0 and vidas > 0: # se arma el ciclo donde las vidas van bajando 

        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}") #muestra el numero de vidas que te faltan

      
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas]) 
        print(f"Palabra: {' '.join(palabra_lista)}")  #se va agregando a la lista y compara

     
        letra_usuario = input('Escoge una letra: ').upper() #pon una letra y la hace en minusculas

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)  #la agrega y compara
       
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
         
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")  #si no es correcta, niega y pregunta hasta quedarte sin vidas

   
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}") # pierdes el juego
    else:
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!') # ganas el juego


    ahorcado()