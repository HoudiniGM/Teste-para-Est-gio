# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
# pertence ou não a sequência.

# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

fibonacci = [0, 1]
pertence = False

numero = int(input("Qual número deseja saber se pertence à sequência de Fibonacci? "))

if numero == 0 or numero == 1:
    pertence = True
    
else:
    while numero > fibonacci[-1]:
        fibonacci.append( fibonacci[-1] + fibonacci[-2])
        
        if numero in fibonacci:
            pertence = True
            break
        

if pertence == True:
    print(f"O número {numero} pertence à sequência")
else:
    print(f"O número {numero} não pertence à sequência")