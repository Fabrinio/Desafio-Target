faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}


def calcular_percentual(faturamento_por_estado):
    total_faturamento = sum(faturamento_por_estado.values())

    percentual_por_estado = {}
    for estado, faturamento in faturamento_por_estado.items():
        percentual_por_estado[estado] = (faturamento / total_faturamento) * 100

    return percentual_por_estado


percentual_por_estado = calcular_percentual(faturamento_por_estado)


for estado, percentual in percentual_por_estado.items():
    print(f'{estado}: {percentual:.2f}%')
