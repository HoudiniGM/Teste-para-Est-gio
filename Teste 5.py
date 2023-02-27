# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

# NÃO SE ESQUEÇA DE INSERIR O LINK DO SEU REPOSITÓRIO NO GITHUB COM O CÓDIGO FONTE QUE VOCÊ DESENVOLVEU

def inverterString(string):
    novaString = ""
    
    #Faço um laço, começando pelo valor do último índice da String, decrementando de 1 em 1 até chegar ao índice 0.
    for indice in range( len(string)-1, -1, -1 ):
        #A cada laço, concateno esse elemento à minha nova String.
        novaString += string[indice]
    
    return novaString

# TESTES
print(inverterString("avadakedavra"))
print(inverterString("Hello, World"))