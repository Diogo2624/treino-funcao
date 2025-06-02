def boas_vindas(nome):
    print(f"Bem-vindo(a), {nome}!")

def dobro(numero):
    return numero * 2

def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def area_retangulo(base, altura):
    return base * altura

def contador(numero):
    for n in range(1, numero + 1):
        print(n)