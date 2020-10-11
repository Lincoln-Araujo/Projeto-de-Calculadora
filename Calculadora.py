def boasVindas():
    print("\n+ - * / Calculadora de Operações Básicas + - * /\n")
    print("(1) SOMA\n(2) SUBTRAÇÃO\n(3) MULTIPLICAÇÃO\n(4) DIVISÃO\n") 
         
def calculadora():
    operacao = input(" Qual tipo de operação? \n")

    listaDeStringsValidas = ["1", "2", "3", "4"]

    if operacao in listaDeStringsValidas:

        somar = "1"
        subtrair = "2"
        multiplicar = "3"
        dividir = "4"

        numero1 = entradaDeNumero(" Qual o primeiro número? \n", "\nDigite um número válido\n")
        numero2 = entradaDeNumero(" Qual o segundo número? \n", "\nDigite um número válido\n")
    
        if operacao == somar:
            soma(numero1, numero2)
        elif operacao == subtrair:
            subtracao(numero1, numero2)
        elif operacao == multiplicar:
            multiplicacao(numero1, numero2)
        elif operacao == dividir:
            divisao(numero1, numero2)
        else:
            return mensagemDeErro() 
    else:
        return mensagemDeErro()

def entradaDeNumero(perguntaPeloNumero, alertaDeNumeroInvalido):
    x = None
   
    while True:
        try:
            x = float(input(perguntaPeloNumero))
            break
        except ValueError:
            print(alertaDeNumeroInvalido)
           
    return x
                  
def soma(numero1, numero2):    
    resultado = numero1 + numero2
    print("{} + {} = {}".format(numero1, numero2, resultado))

def subtracao(numero1, numero2):
    resultado = numero1 - numero2
    print("{} - {} = {}\n".format(numero1, numero2, resultado))   

def multiplicacao(numero1, numero2):
    resultado = numero1 * numero2
    print("{} * {} = {}\n".format(numero1, numero2, resultado))   

def divisao(numero1, numero2):
    if numero2 == float(0):
        print("\n!!! Não é possivel dividir {} por 0 !!!\n".format(numero1))
        boasVindas()
        calculadora()
    else:
        resultado = numero1 / numero2
        print("{} / {} = {}\n".format(numero1, numero2, resultado))    

def novaOperacao():
    novoCalculo = input("\nQuer fazer outra operação? (1) SIM ; (2) NÃO\n")
    if novoCalculo == "1":
        boasVindas()
        calculadora() 
        novaOperacao() 
    elif novoCalculo == "2":
        print("\nObrigado por utilizar meu programa\n")    
    else:
        mensagemDeErro2()

def mensagemDeErro():
    print("\n!!! Escolha uma opção válida !!!\n")
    boasVindas() 
    calculadora()
    
def mensagemDeErro2():
    print("\n!!! Escolha uma opção válida !!!\n")
    novaOperacao()

boasVindas()
calculadora()
novaOperacao()