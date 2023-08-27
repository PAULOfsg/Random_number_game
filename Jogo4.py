import random

def jogo_de_adivinhação():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número correto entre 1 e 100.")

    while True:
        tentativa = int(input("Digite um numero: "))
        tentativa += 1 

        if tentativa < numero_secreto:
            print("Tente um numero maior")

        elif tentativa > numero_secreto:
            print("Tente um numero menor")
        
        else:
            print(f"Parabéns! você em {tentativas} tentativas.")
            break


jogo_de_adivinhação()
