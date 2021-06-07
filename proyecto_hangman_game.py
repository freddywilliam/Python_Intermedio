import os, random
from collections import Counter

def importar_palabra():
    numerado = {}
    palabra = {}
    palabra_cortada = []
    contador = 0
    palabra_cortada_enumerada = {}

    with open("./archivos/DATA.txt", "r", encoding="utf-8") as f:
        numerado = dict(enumerate(f, 1))

    palabra = str(numerado.get(random.randint(1,171), "No hay"))

    for i in range(len(palabra)):
        palabra_cortada.append(palabra[i])
        palabra_cortada_enumerada[i] = palabra[i]
        contador += 1

    contador = contador - 1
    del palabra_cortada_enumerada[contador]
    dic_palabra = palabra_cortada_enumerada
    dic_palabra =list(dic_palabra.values())

    return dic_palabra

def palabra_usuario():
    print(""" 
        -------------
        AHORCADO ALPHA
        -------------

    REGLAS
    _______

    -Cada vez que repitas una palabra pierdes 1 punto.

    
            QUE EMPIEZE EL JUEGO
            _____________________

    Ingresa tu primera letra para empezar
    
    """)
    letra_ingresada = str(input("Escribe tu letra: ")).lower()
    dic_letras_ingrsadas_numeradas = dict(enumerate(letra_ingresada))
    dic_letras_ingrsadas_numeradas = list(dic_letras_ingrsadas_numeradas.values())

    return dic_letras_ingrsadas_numeradas

def comparacion_listas_cierre(a, b):
    return Counter(a) == Counter(b)
 
def comparacion(letra_usuario, palabra_importada, letra_adivinada, palabra_rayada, puntaje):
    
    creacion_rayas =[palabra_rayada.append(' _ ') for i in range(len(palabra_importada)) if len(palabra_rayada) < len(palabra_importada)]
  
    for i in range(len(palabra_importada)):
       
        if palabra_importada[i]== letra_usuario[0]:
            
            letra_adivinada.append(palabra_importada[i])
            palabra_rayada[i]= letra_usuario
                        
    return letra_adivinada, palabra_rayada, puntaje

def letras_repetidas(lista_letra_usuario, mensaje):
    
    letras_repetidas = []
    mensaje = 0

    for n in lista_letra_usuario:
        if n not in letras_repetidas:
            letras_repetidas.append(n)
            mensaje = 0
            
        else:
            mensaje = 1
            
    return mensaje

def run():
    os.system("cls")
    palabra_importada = importar_palabra()
    palabra_rayada = []
    lista_letra_usuario = []
    letra_adivinada = []
    comparacion_listas_cierre_valor = 0
    mensaje = 0
    puntaje = 20

    for i in range(21):
        if i == 20:
            print("""
            
            PERDISTE!!
            
            """)
        
        print("Tienes", puntaje, "Intentos.")
        print("""
        
        
         """)

        print(palabra_rayada)
        letra_usuario = palabra_usuario()
        lista_letra_usuario.append(letra_usuario)
        letras_repetidas(lista_letra_usuario, mensaje)

        if letras_repetidas(lista_letra_usuario, mensaje) == 1:
            print("REPETIDA")
            letras_repetidas(lista_letra_usuario, mensaje)
            mensaje = 0 
            puntaje -= 1
            os.system("cls")
        
        if letras_repetidas(lista_letra_usuario, mensaje) == 0: 
            comparacion(letra_usuario, palabra_importada, letra_adivinada, palabra_rayada, puntaje)
            comparacion_listas_cierre_valor = comparacion_listas_cierre(palabra_importada, letra_adivinada)
            mensaje = 0
            os.system("cls")
            if comparacion_listas_cierre_valor == True:
                print("GANASTE")
                break
            else:
                continue
    os.system("cls")
        
     
if __name__ == '__main__':
    run()