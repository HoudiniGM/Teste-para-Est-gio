# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

dados = [
        {"UF": "SP", "valor": 67836.43},
        {"UF": "RJ", "valor": 36678.66},
        {"UF": "MG", "valor": 29229.88},
        {"UF": "ES", "valor": 27165.48},
        {"UF": "Outros", "valor": 19849.53}
    ]

def percentualRepresentado(arr, uf):
    valorTotal = 0
    uf = uf.upper()
    
    #Percorro o array e descubro o valor total.
    for elemento in arr:
        valorTotal += elemento["valor"]
    
    #Percorro novamente o arr, descubro o valor da representação do estado do parâmetro, retornando seu percentual formatado.
    for elemento in arr:
        if elemento["UF"].upper() == uf:
            percentual = elemento["valor"] / valorTotal * 100
            return f"{percentual:.2f}%"
    
    print("UF inválido!")
    
#TESTES
print(percentualRepresentado(dados, "SP"))
print(percentualRepresentado(dados, "Rj"))
print(percentualRepresentado(dados, "mg"))
print(percentualRepresentado(dados, "ES"))
print(percentualRepresentado(dados, "oUtRos"))
    
    