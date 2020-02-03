
from moduloFuncoes import *
from selenium import webdriver
from time import *


# Tipos primitivos e saída de dados
'''
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma entre {} e {} vale:'.format(n1, n2, s))


n = float(input('Digite um valor: '))
print(n)
print(type(n))
#print(type(n1))

n = bool(input('Digite um valor: '))
print(n)
print(type(n))
#print(type(n1))

n = input('Digite um valor: ')
print(n.isnumeric())

n = input('Digite um valor: ')
print(n.isalpha())

n = input('Digite um valor: ')
print(n.isalnum())

n = input('Digite um valor: ')
print(n.isupper())
'''

# Manipulando Cadeias de Texto
# strip() remove todos os espaços inúteis no inicio e fim 
# rstrip() remove espaços da direita
# lstrip() remove espaços da esquerda
# Dividir strings: split() -> divide a cadeia de strings baseado no espaço ou outro parâmetro
# Juntar: '-'.join(frase)

#frase = 'Curso em Video Python'
#print(frase)
#print(frase[3])
#print(frase[3:13])
#print(frase[:13])
#print(frase[13:])
#print(frase[1:15])
#print(frase[1:15:2])
#print(frase[1::2])
#print(frase[::2])
#print("""Machine learning (ML) is the scientific study of algorithms and statistical models
#that computer systems use to perform a specific task without using explicit instructions, 
#relying on patterns and inference instead. It is seen as a subset of artificial intelligence. 
#Machine learning algorithms build a mathematical model based on sample data, known as "training data", 
#in order to make predictions or decisions without being explicitly programmed to perform the task.[1][2]:2 
#Machine learning algorithms are used in a wide variety of applications, such as email 
#filtering and computer vision, where it is difficult or infeasible to develop a conventional 
#algorithm for effectively performing the task.""")
#No Python tudo é um objeto
#print(frase.count('o'))
#print(frase.count('O'))
#print(frase.upper().count('O'))
#print(len(frase)) #verificando o tamanho da frase

'''
frase2 = '    Franciny Salles        '
print(len(frase2))
print(len(frase2.strip())) #verificando o tamanho da frase retirando os espaços
print(frase2.strip()) #mostrando frase2 sem os espaços

frase3 = 'Curso de Java'
print(frase3)
print(frase3.replace('Java','Python'))
print(frase3[0])

frase3.replace('Java','Python')
print(frase3)

frase3 = frase3.replace('Java','Python')
print(frase3)

print('Curso' in frase3)
print(frase3.find('Curso'))

print(frase.split()) # Cria uma lista
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2][3])
'''

# CONDIÇÕES - Curso Python #10
# Condiçoes Simples e Compostas

'''
nome = str(input('Qual é o seu nome?: '))
if nome == 'Franciny':
    print('Você é o administrador principal!')
else:
    print('Você não é o administrador principal! Cai fora!')
print('Bom dia {}'.format(nome))


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m)) 
print('APROVADO' if m>=6 else 'REPROVADO') #condição simplificada
#if m>=6.0:
#    print('Sua média é satisfatória')
#else:
#    print('Sua média é ruim')
'''

# AULA #012 - ESTRUTURAS DE CONTROLE - Condições Aninhadas
# Estrutura condicional aninhada:
'''
nome = str(input('Qual é o seu nome? '))
print('Tenha um bom dia {}!'.format(nome))
if nome == 'Franciny':
    print('Você é o administrador!')
elif nome == 'Patty' or nome == 'Andres' or nome == 'Flavio':
    print('Família de Franciny, Seja bem vindo(a)!')
elif nome in 'Sandra Rosa':
    print('Irmã de Patty')
else:
    print('Não te conheço!')
'''

# AULA #013 - ESTRUTURA DE REPETIÇÃO FOR
#for c in range(0, 10):
#    #print('Oi')
#    print(c)
#print('FIM')

#for c in range(6, 0, -1): #contando de 6 até 0, pra tras
#    print(c)

#for c in range(0, 7, 2):
#    print(c)

#for c in range(0, 10, 3):
#    print(c)

#n = int(input('Digite um número: '))
#for c in range(0, n):
#    print(c)
#print('FIM')

#n = int(input('Digite um número: '))
#for c in range(0, n+1): #para chegar no número que eu quero
#    print(c)
#print('FIM')

#i = int(input('Início: '))
#f = int(input('Fim: '))
#p = int(input('Passo: '))

#for c in range(i, f+1, p):
#    print(c)
#print('FIM')

#for c in range(0,10):
#    n = int(input('Digite um valor: '))
#print('FIM')

#s = 0
#for c in range(0,4):
#    n = int(input('Digite um valor: '))
#    s = s + n # s += n    
#print('O somatório de todos os valores foi {}'.format(s))


# Curso Python #014 - ESTRUTURA DE REPETIÇÃO WHILE
#for c in range(1,10):
#    print(c)
#print('FIM')
# Quando uso for e quando uso while: eu sei o limite?for ou while, não sei limite?while
#c = 1
#while c < 10:
#    print(c)
#    c += 1 #c = c + 1
#print('FIM')

#n=1
#while n != 0: #condição de parada
#    n = int(input('Digite um valor: '))
#print('FIM')

#r = 'S'
#while r == 'S':
#    s = int(input('Digite um valor: '))
#    r = str(input('Quer continuar [s/n]? ')).upper()
#print('FIM')

#n = 1
#par = impar = 0
#while n != 0:
#    n = int(input('Digite um número: '))
#    if n != 0:
#        if n % 2 == 0:
#            par += 1
#        else:
#            impar += 1
#print('Você digitou {} números pares e {} números ímpares!'.format(par,impar))   


# Curso Python #15 - INTERROMPENDO REPETIÇÕES WHILE
#cont = 1
#while cont <= 10:
#    print(cont, '-> ', end='')
#    cont += 1
#print('FIM')

#Entrando em loop infinito
#cont=1
#while True:
#    print(cont, '-> ', end='')
#    cont += 1
#print('FIM')

#n = cont = 0
#while cont < 3:
#    n = int(input('Digite um número: '))
#    cont += 1

#n = s = 0
#while n != 999:
#    n = int(input('Digite um número: '))
#    s += n
#s -= 999 # isso é gambiarra
#print('A soma vale {} '.format(s))


# Sem gambiarra
#n = s = 0
#while True:
#    n = int(input('Digite um número: '))
#    if n == 999:
#        break
#    s += n
#print('A soma vale {} '.format(s))

#n = s = 0
##while True:
#   n = int(input('Digite um número: '))
#    if n == 999:
#        break
#    s += n
#print('A soma vale {} '.format(s))
#print(f'A soma vale {s}')

#nome = 'Franciny'
#idade = 39
#print(f'O {nome} tem {idade} anos.') #PYTHON 3.6+
#print('O {} tem {} anos.'.format(nome,idade)) #PYTHON 3
#print('O %s tem %d anos.' % (nome, idade)) #PYTHON 2

#nome = 'Franciny'
#idade = 39
#salario = 3000
#print(f'O {nome} tem {idade} anos e ganha R$ {salario} reais.')




#imprimirTexto('Franciny Salles')
#soma(1,5)
#contador2(1,2,3)

#minhaLista=[0,1,2]
#print(minhaLista)
#dobrando(minhaLista)
#print(minhaLista)

# Faça um programa que tenha uma função chamara área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.
#area(5,10)


# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
# parâmetro e mostre uma mensagem com tamanho adaptável.
#escreva('fran')
#escreva('Franciny')
#escreva('Franciny Salles')
#escreva('Franciny Salles & Patty Rojas')


# Faça um programa que tenha uma função que receba três parâmetros:inicio, fim e passo e realize a contagem
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
#scontagemDesafio()


# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior
#maior(0)
#maior(0,1,2,3,4,5,6)
#maior(2,5,3,9)


# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vi sortear 5 números e vai colocá-la dentro da lista e a segunda função vai mostrar a soma
# entre todos os valores PARES sorteados pela função anterior.
''''
numeros = []
print('Sorteando 5 valores da lista: ', end = ' ')
sleep(0.5)
for s in sorteia():
    print(s, end=' ')
    numeros.append(s)
    sleep(0.5)
print('PRONTO!')
sleep(2)
print(f'Somando os valores pares de {numeros}, temos {somaPar(numeros)}.')
'''





# Interactive Help
#help(print)
#print(input.__doc__)

#somaropcional(2,3)

#estudandocontador(2,10,2)

#help(estudandocontador.__doc__)

#somarReturn(2,2,2)

'''
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')


print(parOuImpar(7))

num=int(input('Digite um número: '))
if parOuImpar(num):
    print('É par!')
else:
    print('É ímpar!')
'''

# Acessando o Google com o Chrome


g.navigate()
#g.search('Live de Python')
g.lucky('Live de Python')

