print("Calculadora")

Operacao = str(input("Qual operação deseja fazer? "))

numero_1 = float(input("Digite o numero:" ))

numero_2 = float(input("Digite o numero:" ))

total_adicao = numero_1 + numero_2
total_subtração = numero_1 - numero_2
total_divisão = numero_1 / numero_2
total_multiplicacao = numero_1 * numero_2

if Operacao == "adição":
        print("o valor da sua adição é de " + str(total_adicao))
elif Operacao == "subtração":
        print("o valor da sua subtração é de " + str(total_subtração))
elif Operacao == "divisão":
        print("o valor da sua divisão é de " + str(total_divisão))
else: 
        print("o valor da sua multiplicação é de " + str(total_multiplicacao))

