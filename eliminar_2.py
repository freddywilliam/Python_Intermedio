from collections import Counter

# def comparacion(a,b):
#     return Counter(a) == Counter(b)    
def repetidos(lista_letra_usuario):
    mensaje = 0
    letras_repetidas = []

    for n in lista_letra_usuario:
        if n not in letras_repetidas:
            letras_repetidas.append(n)
            print(letras_repetidas)
        else:
            mensaje = print("LETRA REPETIDA")
    return mensaje

def run():

    lista_letra_usuario = []

    for i in range(5):
        
        letra_usuario = str(input("Letra: "))
        lista_letra_usuario.append(letra_usuario)
        repetidos(lista_letra_usuario)
        






    # a = [ "A", "B", "C"]
    # b = [ "A", "B", "C"]
    # print(comparacion(a, b))
    # if comparacion(a,b) == True:
    #     print("SII")


if __name__ == '__main__':
    run()