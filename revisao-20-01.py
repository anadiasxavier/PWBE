#PRIMEIRO 
'''num1 = int (input("Digite um número: "))
num2 = int (input("Digite um segundo número: "))

print (f"A soma entre eles é: {num1 + num2}")'''

#SEGUNDO
'''ano = int (input("Digite o ano do seu nascimento:"))
nome = str (input("Digite o seu nome:"))

vintecinco = 2025 - ano

print(f"{nome} em 2025 você terá : {vintecinco}")'''

#TERCEIRO
'''num1 = int (input("Digite um número: "))

if num1 % 2 == 0 :
    print("O número é par.")
else :
    print("O número é impar.")'''

#QUARTO
'''nota1 = float (input("Digite sua primeira nota: "))
nota2 = float (input("Digite sua segunda nota: "))
nota3 = float (input("Digite sua terceira nota: "))
nota4 = float (input("Digite sua quarta nota: "))
nota5 = float (input("Digite sua quinta nota: "))

media = (nota1 + nota2 + nota3 + nota4 + nota5) /5

if media >= 5:
    print("Você está aprovado.")
elif media >=2.5 and media < 5:
    print("Você está em recuperação.")
else:
    print("Você está reprovado.")'''

#QUINTO
'''num1 = int (input("Digite um número: "))


for i in range (num1, 0, -1):
    print(i)'''

#SEXTO
'''nummaior = 0
num = 0 

while True:
    num = float (input("Digite um número: "))

    if num < 0:
        break

    elif num > nummaior:
        nummaior = num 
print(f"O número maior é {nummaior}")
'''

#SETIMO
'''def inverter_string(s):
    invertido = ''
    for i in s: 
        invertido = i + invertido
    return invertido

palavra = str (input("Digite uma palavra: "))
print (inverter_string(palavra))'''

#OITAVO
def contar_caracteres(s):
  dicionario = {}
  for i in s:
    if i not in dicionario:
        dicionario[i] = 1 
    else:
        dicionario[i] += 1
    print(dicionario)

    
palavra = str (input("Digite uma palavra: "))
print (contar_caracteres(palavra))
    
"""
d = {'G' : 1, 'i':1, 'o':1,'v':1,'a':2,'n':1, ' ':1, 'C':1}

s = "Giovana Clara"
i = a


"""