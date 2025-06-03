# Aqui eu defino as funções que serão utilizadas.

def boas_vindas(nome):                          #Função de boas-vindas
    print(f"Bem-vindo(a), {nome}!")

def dobro(numero):                              #Função que retorna o dobro de um número   
    return numero * 2 

def eh_par(numero):                             #Função que verifica se um número é par ou ímpar        
    if numero % 2 == 0:
        return f"{numero} é par."
    else:
        return f"{numero} é ímpar."

def area_retangulo(base, altura):               #Função que calcula a área de um retângulo    
    return base * altura

def contador(numero):                           #Função que conta de 1 até o número fornecido
    for n in range(1, numero + 1):
        print(f"contando: {n}")

# Aqui eu crio uma varável para pedir ao usuário qual função ele vai utilizar.
def opcao():
    opcao = input("Digite o que deseja executar, 1 para boas-vindas, 2 para dobro, 3 para verificar paridade, 4 para área do retângulo, 5 para contador: ")

    if opcao == '1':                                        
        nome = input("Digite seu nome: ")
        boas_vindas(nome)

    elif opcao == '2':
        numero = int(input("Digite um número inteiro para saber o seu dobro: "))
        dobro(numero)
        print(f"O dobro de {numero} é {dobro(numero)}")

    elif opcao == '3':
        numero = int(input("Digite um número inteiro para verificar se é par: "))
        eh_par(numero)
        print(f"{eh_par(numero)}")

    elif opcao == '4':
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area_retangulo(base, altura)
        print(f"A área do retângulo é {area_retangulo(base, altura)}")

    elif opcao == '5':
        numero = int(input("Digite um número para contar até ele: "))
        contador(numero)

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
    
continuar = input("Deseja continuar usando as funções? (s/n): ")
if continuar.lower() != 's':
    print("Obrigado por usar o programa!")
    exit()

# Aqui vamos criar um loop para o usuário poder continuar utilizando as funções.
while True:
    opcao()
