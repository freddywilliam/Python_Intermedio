from collections import Counter
def comparar_listas(a,b):
    return Counter(a) == (b)

def run():
    palabra_importada = ["1", "2", "3", "4", "1"]
    

    palabra_importada_raya = list(palabra_importada)
    

    for i in range(len(palabra_importada)):
        palabra_importada_raya[i] = " - "
    print(palabra_importada_raya)

    
    letra_usuario = str(input("Letras: "))
    filter_condicion = list(filter(lambda x: x == letra_usuario , palabra_importada)) 
    palabra_adivinada.append(filter_condicion)


   
 
    if letra_usuario[0] == palabra_importada[i]:
        print("SI")
        palabra_importada_raya[i]= letra_usuario[0]
        print(palabra_importada_raya)


   

































if __name__ == '__main__':
    run()