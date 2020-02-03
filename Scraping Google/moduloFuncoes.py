from time import *
from random import *
from selenium import webdriver


#----------------------------------------------------------------------------------#
def dobrando(minhaLista):
    pos = 0
    while pos < len(minhaLista):
        minhaLista[pos] *= 2
        pos += 1
#----------------------------------------------------------------------------------#
def soma(a,b):
    s = a + b
    print(s)
    return soma
#----------------------------------------------------------------------------------#
def imprimirTexto(txt):
    print(txt)
    return txt
#----------------------------------------------------------------------------------#
def contador(* num):
    for n in num:
        print(f'{n} ', end='')
    print('FIM!')
#----------------------------------------------------------------------------------#
def contador2(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são todos ao todo {tam} números')
#----------------------------------------------------------------------------------#
def soma2(* variosvalores):
    s = 0
    for num in variosvalores:
        s += num
    print('Somando os valores {variosvalores} temos {s}')    
#----------------------------------------------------------------------------------#
def area(x,y):
    a = x*y
    print(f'Largura (m): {x}')
    print(f'Comprimento (m): {y}')
    print(f'A área do terreno é de {a} m2')
    return area
#----------------------------------------------------------------------------------#
def escreva(txt):
    s = len(txt)
    print('-'*s)
    print(txt)
    print('-'*s)
    return escreva
#----------------------------------------------------------------------------------#
def linha(tam):
    print('=' * tam)
#----------------------------------------------------------------------------------#
def contagemDesafio():   
    for c in range(0,2):
        linha(30)
        if c == 0:
            print('Contagem de 1 até 10 de 1 em 1')
            for n in range(1,11):
                sleep(0.5)
                print(n, end='')
            sleep(0.5)
            print('Fim')
        else:
            print('Contagem de 10 até 0 de 2 em 2')
            for n in range(10, -2, -2):
                sleep(0.5)
                print(n, end='')
            sleep(0.5)
            print('Fim')
        sleep(0.5)
    linha(30)
    print('Agora é a sua vez de personalizar a contagem!')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = abs(int(input('Passo: ')))
    resultado = inicio
    if passo == 0:
        passo = 1
    if passo <= abs(int(fim - inicio)):
        linha(30)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        if inicio < fim:
            while resultado <= fim:
                print(resultado, end=' ')
                sleep(0.4)
                resultado += passo
        elif inicio > fim:
            while resultado >= fim:
                print(resultado, end=' ')
                sleep(0.5)
                resultado -= passo
        print('\nFim :)')
    else:
        print('3RR0')
#----------------------------------------------------------------------------------#
def maior(* num):
    linha(200)
    print(f'Analisando os valores passados...'), sleep(1.2)
    if len(num) == 0:
        print('Foram informados 0 valores ao todo.'), sleep(1.8)
        print('O maior valor informado foi o 0.'), sleep(1.9)
    else:
        p = num[0]
        for n in range(1, len(num)):
            if num[n] > p:
                p = num[n]
        for n in num:
            print(n, end=' ')
            sleep(0.5)
        print(f'Foram informados {len(num)} valores ao todo.'), sleep(1.8)
        print(f'O maior valor informado foi {p}.'), sleep(1.9)

#----------------------------------------------------------------------------------#

def sorteia():
    n = []
    for c in range(0,5):
        n.append(randint(1,10))
    return n[:]

#----------------------------------------------------------------------------------#
def somaPar(num):
    par = 0
    for n in num:
        if n%2 == 0:
            par += n
    return par
#----------------------------------------------------------------------------------#
def estudandocontador(i,f,p):
    """
    -> Faz uma contagme e mostra na tela
    """
    c=i
    while c<= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')
#----------------------------------------------------------------------------------#
def somaropcional(a,b,c=0):
    s=a+b+c
    print(f'A soma vale: {s}')
#----------------------------------------------------------------------------------#
def somarReturn(a=0,b=0,c=0):
    s=a+b+c
    return s
#----------------------------------------------------------------------------------#
def fatorial(num=1):
    f = 1 # variavel local
    for c in range(num, 0, -1):
        f *= c
    return f
#----------------------------------------------------------------------------------#
def parOuImpar(n=0):
    if n%2==0:
        return True
    else:
        return False
#----------------------------------------------------------------------------------#
class Google:
    def __init__(self,driver):
        self.driver = driver
        self.url = 'http://google.com.br'
        self.search_bar = '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'
        self.btn_search = '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]'
        self.btn_lucky = '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[2]'
    def navigate(self):
        self.driver.get(self.url)
    
    def search(self, word='None'):
        self.driver.find_element_by_xpath(self.search_bar).send_keys(word)
        self.driver.find_element_by_xpath(self.btn_search).click()

    def lucky(self, word='None'):
        self.driver.find_element_by_xpath(self.search_bar).send_keys(word)
        self.driver.find_element_by_xpath(self.btn_lucky).click()
        
chromedriverPath = "//Users//fransalles//node_modules//chromedriver//lib//chromedriver//chromedriver"
chr = webdriver.Chrome(chromedriverPath)
g = Google(chr)
#----------------------------------------------------------------------------------#
