#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def fibo(sequencia : int) -> bool:
    # inicar sequencia
    a,b = 0 , 1

    # verificar se é 0 ou 1 na sequencia
    if sequencia in (a,b):
        return True 
    
    # gerar numeros ate que b seja maior ou igual a sequencia
    while b < sequencia:
        a,b = b, a + b

    # retornar True se b for igual ao numero da sequencia
    return b == sequencia    