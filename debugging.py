def divisors(num):

    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

def run():
    
    try:
        num = int(input("Ingresa un numero: "))
        if num <= 0:
            raise Exception("Numero negativo o diferente a cero")
        print(divisors(num))
        print("END PROGRAM")
    except ValueError:
        print("Ingresa un numero entero.")
    except Exception:
        print("Debes Ingresar Un Numero Positivo")

if __name__ == '__main__':
    run()