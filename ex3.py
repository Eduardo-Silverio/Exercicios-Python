import json

dados_json = '''
[
    {"dia": 1, "faturamento": 130.15},
    {"dia": 2, "faturamento": 150.99},
    {"dia": 3, "faturamento": 249.90},
    {"dia": 4, "faturamento": 0.0},
    {"dia": 5, "faturamento": 0.0},
    {"dia": 6, "faturamento": 233.80},
    {"dia": 7, "faturamento": 0.0},
    {"dia": 8, "faturamento": 784.95},
    {"dia": 9, "faturamento": 943.42},
    {"dia": 10, "faturamento": 1029.99},
    {"dia": 11, "faturamento": 0.0},
    {"dia": 12, "faturamento": 0.0},
    {"dia": 13, "faturamento": 534.43},
    {"dia": 14, "faturamento": 230.10},
    {"dia": 15, "faturamento": 1123.90},
    {"dia": 16, "faturamento": 982.99},
    {"dia": 17, "faturamento": 109.12},
    {"dia": 18, "faturamento": 0.0},
    {"dia": 19, "faturamento": 0.0},
    {"dia": 20, "faturamento": 322.10},
    {"dia": 21, "faturamento": 1234.98},
    {"dia": 22, "faturamento": 1323.42},
    {"dia": 23, "faturamento": 125.99},
    {"dia": 24, "faturamento": 1398.90},
    {"dia": 25, "faturamento": 0.0},
    {"dia": 26, "faturamento": 0.0},
    {"dia": 27, "faturamento": 10.90},
    {"dia": 28, "faturamento": 723.90},
    {"dia": 29, "faturamento": 1234.00},
    {"dia": 30, "faturamento": 1432.90}
]
'''

faturamento_diario = json.loads(dados_json)

valores_faturamento = [dia['faturamento'] for dia in faturamento_diario if dia['faturamento'] > 0]

menor_faturamento = min(valores_faturamento)
maior_faturamento = max(valores_faturamento)

media_mensal = sum(valores_faturamento) / len(valores_faturamento)

dias_acima_da_media = len([dia for dia in valores_faturamento if dia > media_mensal])

print(f"O menor valor de faturamento ocorrido em um dia do mês foi: {menor_faturamento:.2f}")
print(f"O maior valor de faturamento ocorrido em um dia do mês foi: {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
