# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import dados #Importo o array de objetos de outro arquivo
dadosImportados = dados.arr #Atribuo uma nova variável para os dados


def menorValor(arr):
    arrDeValores = []
    
    #Percorro o array e adiciono a um novo array os valores que são diferentes de 0.
    for elemento in arr:
        if elemento["valor"] != 0:
            arrDeValores.append(elemento["valor"])
            
    #Por fim, uso o método min() para filtrar o menor valor do array.
    return min(arrDeValores)

print(f"Menor valor: {menorValor(dadosImportados)}")



def maiorValor(arr):
    arrDeValores = []
    
    #Percorro o array e adiciono a um novo array os valores.
    for elemento in arr:
        arrDeValores.append(elemento["valor"])
    
    #Por fim, uso o método max() para filtrar o maior valor desse array.
    return max(arrDeValores)

print(f"Maior Valor: {maiorValor(dadosImportados)}")



def diasAcimaDaMedia(arr):
    arrDeValores = []
    
    #Primeiramente, armazeno em um array os valores válidos.
    for elemento in arr:
        if elemento["valor"] != 0:
            arrDeValores.append(elemento["valor"])
            
    #Depois, descubro a média desses valores.
    media = 0
    for valor in arrDeValores:
        media += valor
    media /= len(arrDeValores)
    
    #Por fim, armazeno em um array os dias cujos seus respectivos valores são superiores à média mensal.
    diasAcimaDaMedia = []
    for elemento in arr:
        if elemento["valor"] > media:
            diasAcimaDaMedia.append(elemento["dia"])

    return diasAcimaDaMedia

print(f"Dias cujos valores estavam acima da média mensal: {diasAcimaDaMedia(dadosImportados)}")
    
    
    

