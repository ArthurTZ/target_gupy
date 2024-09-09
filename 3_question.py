#Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json


faturamento_dias = ''' 
[
    {"dia": 1, "faturamento": 2500.950},
    {"dia": 2, "faturamento": 24537.100},
    {"dia": 3, "faturamento": 26788.5640},
    {"dia": 4, "faturamento": 0.0},
    {"dia": 5, "faturamento": 0.0},
    {"dia": 6, "faturamento": 30000},
    {"dia": 7, "faturamento": 0.0},
    {"dia": 8, "faturamento": 45000},
    {"dia": 9, "faturamento": 46251.174},
    {"dia": 10, "faturamento": 123456.47}
]
'''

faturamento = json.loads(faturamento_dias)

def calcular_faturamento(faturamento : dict):
    # consideração que o faturamento zerado será considerado como dia invalido
    dias_validos = [dia['faturamento'] for dia in faturamento if dia['faturamento'] > 0]

    menor_faturamento = min(dias_validos)
    maior_faturamento = max(dias_validos)

    media = sum(dias_validos) / len(dias_validos)

    dias_acima_media = sum(1 for valor in dias_validos if valor > media)
    return menor_faturamento, maior_faturamento, dias_acima_media


menor,maior, dias_acima = calcular_faturamento(faturamento)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Número de dias acima da média: {dias_acima}")





