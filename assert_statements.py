def divisors(num):

    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors
    
def run():
    #          assert condicion, mensaje de error
    
        # num = input("Ingresa un numero: ")
        # assert num.isnumeric(), "Debes ingresar un numero"
        # print(divisors(int(num)))
        # print("END PROGRAM")
    
    #           RETO
    # PUEDES COMBINAR SEGUN TU CRITERIO LOS ASSERT Y TRY,EXCEPT
    

    try:
        num = int(input("Ingresa un numero: "))
        assert int(num) > 0, "Debes ingresar un numero positivo"
        print(divisors(num))
        print("END PROGRAM")
    except ValueError:
        print("Ingresa un numero entero.")
   

 
if __name__ == '__main__':
    run()