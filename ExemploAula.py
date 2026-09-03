def main():
    val1 = int(input("informe o valor 1: "))
    val2 = int(input("informe o valor 2: "))

    n = somar(val1, val2)
    print(n)
    
    
def somar(valor1, valor2):
    resultado = valor1 + valor2
    return resultado


main()