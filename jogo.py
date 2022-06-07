from random import randint
from time import sleep

jogadas = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
ganhou = 0
perdeu = 0
empatou = 0
print(20 * '-=', f'\n{"PEDRA PAPEL TESOURA":^40}')
print(20 * '-=')
while True:
    escolhaComputador = randint(1, 3)
    while True:
        escolhaJogador = int(input("Escolha a sua jogada \n1- Pedra\n2- Papel\n3- Tesoura\nSua escolha: "))
        if escolhaJogador > 3 or escolhaJogador < 0:
            print("Escolha uma opção de 1 a 3!")
            print(20 * '-=')
        else:
            break
    print(20 * '-=')
    print("Pedra...", end=' ')
    sleep(0.5)
    print("Papel...", end=' ')
    sleep(0.5)
    print("Tesoura...")
    sleep(0.5)
    if escolhaJogador == 1:
        if escolhaComputador == 1:
            print("EMPATAMOS!")
            empatou += 1
        elif escolhaComputador == 2:
            print("VOCÊ GANHOU!")
            ganhou += 1
        else:
            print("VOCÊ PERDEU!")
            perdeu += 1
    elif escolhaJogador == 2:
        if escolhaComputador == 1:
            print("VOCÊ PERDEU!")
            perdeu += 1
        elif escolhaComputador == 2:
            print("EMPATAMOS!")
            empatou += 1
        else:
            print("VOCÊ GANHOU!")
            ganhou += 1
    else:
        if escolhaComputador == 1:
            print("VOCÊ PERDEU!")
            perdeu += 1
        elif escolhaComputador == 2:
            print("VOCÊ GANHOU!")
            ganhou += 1
        else:
            print("EMPATAMOS!")
            empatou += 1
    print(f"Eu joguei {jogadas[escolhaComputador]} e você jogou {jogadas[escolhaJogador]}!")
    print(20 * '-=')
    continuar = input("Quer continuar? [S/N]: ").upper()
    if continuar == 'N':
        break
print(20 * '-=', f'\n{"TABELA FINAL":^30}')
print(f"VOCÊ GANHOU {ganhou}"
      f"\nVOCÊ PERDEU {perdeu}"
      f"\nVOCÊ EMPATOU {empatou}")
print(20 * '-=')
print("Foi bom jogar com você, volte sempre!")