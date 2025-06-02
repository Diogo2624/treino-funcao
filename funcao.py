def boas_vindas(nome):
    nome = input("Digite seu nome: ")
    print(f"Bem-vindo(a), {nome}!")

def dobro(numero):
    return numero * 2


def eh_par(numero):
    numero = int(input("Digite um número inteiro para verificação: "))
    if numero % 2 == 0:
        return "O número é par."
    else:
        "O número é ímpar."

def area_retangulo(base, altura):
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    print(f"A área do retângulo é: {area_retangulo(base, altura)}")
    return base * altura

def contador(numero):
    numero = int(input("Digite um número para contar até ele: "))
    print(f"Contando de 1 até {numero}:")
    for n in range(1, numero + 1):
        print(n)

opcao = input("Digite o que deseja executar, 1 para boas-vindas, 2 para dobro, 3 para verificar paridade, 4 para área do retângulo, 5 para contador: ")
if opcao == '1':
    boas_vindas(nome="")
elif opcao == '2':
    dobro(numero="")
elif opcao == '3':
    eh_par(numero="")
elif opcao == '4':
    area_retangulo(base="", altura="")
elif opcao == '5':
    contador(numero="")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

numero = int(input("Por favor, digite um número inteiro: "))
print(f"O resultado é {dobro(numero)}")
print(f"O resultado da verificação de paridade é: {eh_par(numero)}")
print(f"A área do retângulo é: {area_retangulo(0, 0)}")
print(f"A contagem até {numero} é: {contador(numero)}")
print("Programa finalizado.")