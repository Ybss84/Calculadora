#Calculadora
resposta = ""

while resposta!="sair":

    numero1 = float(input("\nDigite o primeiro número: "))
    oper = str(input("Digite a operação: "))
    numero2 = float(input("Digite o segundo número: "))
    



    if oper=='+':
        resultado = numero1+numero2
    elif oper=='-':
        resultado = numero1-numero2
    elif oper=='*':
        resultado = numero1*numero2
    elif oper=='/':
        resultado = numero1/numero2
    else:
        print("Opção inválida")



    print("Resultado da operação: {}".format(resultado))
    resposta = str(input("\nDigite ""sair"" para encerrrar o programa: "))