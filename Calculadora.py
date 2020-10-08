def boasVindas():
    print("Calculadora de Operações Básicas\n")
    print("(1) SOMA\n(2) SUBTRAÇÃO\n(3) MULTIPLICAÇÃO\n(4) DIVISÃO\n")

def calculadora():    
    operacao = int(input("Qual tipo de operação? \n"))
    while operacao == 1 or 2 or 3 or 4:
        if operacao == 1:
            return soma()
        elif operacao == 2:
            return subtracao()
        elif operacao == 3:
            return multiplicacao()
        elif operacao == 4:
            return divisao()
        else:
            return mensagemDeErro()    
                  
def soma():
    numero1 = float(input("Qual o primeiro número? \n"))
    numero2 = float(input("Qual o segundo número? \n"))
    resultado = numero1 + numero2
    print("{} + {} = {}\n".format(numero1, numero2, resultado))
    novaOperacao()

def subtracao():
    numero1 = float(input("Qual o primeiro número? \n"))
    numero2 = float(input("Qual o segundo número? \n"))
    resultado = numero1 - numero2
    print("{} - {} = {}\n".format(numero1, numero2, resultado))
    novaOperacao()

def multiplicacao():
    numero1 = float(input("Qual o primeiro número? \n"))
    numero2 = float(input("Qual o segundo número? \n"))
    resultado = numero1 * numero2
    print("{} * {} = {}\n".format(numero1, numero2, resultado))
    novaOperacao()

def divisao():
    numero1 = float(input("Qual o primeiro número? \n"))
    numero2 = float(input("Qual o segundo número? \n"))
    resultado = numero1 / numero2
    print("{} / {} = {}\n".format(numero1, numero2, resultado))
    novaOperacao()

def novaOperacao():
    novoCalculo = int(input("Quer fazer outra operação? (1) SIM ; (2) NÃO\n"))
    print("(1) SOMA\n(2) SUBTRAÇÃO\n(3) MULTIPLICAÇÃO\n(4) DIVISÃO\n")
    while novoCalculo == 1:
        return calculadora()       
    else:
        print("\nObrigado por utilizar meu programa\n")

def mensagemDeErro():
    print("\nEscolha uma opção válida\n")  
    return calculadora()

boasVindas()
calculadora()