import time
import os

# Começo
os.system('clear')#Limpar o console
print("Bem vindo a Calculadora do Vitor!")
time.sleep(1)
print("Oque Deseja fazer?\n")
time.sleep(0.4)

# Opções
print("[a]Calculadora\n[b]Tabuada")
time.sleep(1)
escolha=str(input("Selecione uma opção: "))

# Tabuada
if(escolha == "b"):
    os.system('clear') #Limpar o Console
    print("Você escolheu Tabuada!")
    tabuada=int(input('Quer ver a tabuada de: '))
    time.sleep(1)
    for c in range(0,11):
        print(f'{tabuada} x {c} = {tabuada*c}')


# Calculadora
if(escolha == "a"):
    os.system('clear') #Limpar o Console
    print("Você escolheu Calculadora!")
    time.sleep(1)

    print("[1]Somar\n[2]Subtrair\n[3]Multiplicar\n[4]Dividir")
    escolha2=int(input("Oque quer fazer? "))

# Soma
    if(escolha2 == 1 ):
        num=int(input("Escreva o primeiro número que deseja somar: "))
        num2=int(input("escreva o segundo número: "))
        print(f'{num} + {num2} = {num + num2}')

# Subtração
    elif(escolha2 == 2):
         os.system('clear')
         print("Oque quer subtrair?")
         num=int(input("Escreva o primeiro número: "))
         num2=int(input("escreva o segundo número: "))
         print(f'{num} - {num2} = {num-num2}')
    
# Multiplicação
    elif(escolha2 == 3):
        num=int(input("Escreva o primeiro número que deseja multiplicar: "))
        num2=int(input("escreva o segundo número que deseja multiplicar: "))
        print(f'{num} x {num2} = {num*num2}')
    
# Divisão
    elif(escolha2 == 4):
        os.system('clear')
        print("Oque quer dividir?")
        num=int(input('Digite o primeiro número: '))
        num2=int(input('Digite o segundo número: '))
        print(f'{num} ÷ {num2} = {num/num2} ')