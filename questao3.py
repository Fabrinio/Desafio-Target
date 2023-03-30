import json

def readJSON():
    with open('dados.json') as f:
        dados = json.load(f)
    return dados

def calcula_faturamento(dados):
    minimo = dados[0]['valor']
    maximo = dados[0]['valor']
    soma = 0

    for dia in dados:
        valor = dia['valor']
        soma += valor

        if valor < minimo:
            minimo = valor
        elif valor > maximo:
            maximo = valor

    media = soma / len([dia for dia in dados if dia['valor'] > 0])

    dias_acima_da_media = 0
    for dia in dados:
        if dia['valor'] > media:
            dias_acima_da_media += 1

    return (minimo, maximo, dias_acima_da_media)

def main():
    dados = readJSON()
    minimo, maximo, dias_acima_da_media = calcula_faturamento(dados)

    print(f'Menor valor de faturamento diário: {minimo}')
    print(f'Maior valor de faturamento diário: {maximo:.2f}')
    print(f'Número de dias com faturamento acima da média mensal: {dias_acima_da_media}')

main()
