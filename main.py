import json
import csv
from matplotlib import pyplot

nome_arquivo = "dados\projetos-de-extensao.json"
arquivo = open(nome_arquivo, "r", encoding="utf-8")
base = json.load(arquivo)

print(base[0].keys())

# Pergunta 6 - <area_conhecimento, quantidade>
def projetos_por_area(dados):
    resultado = {}
    for p in dados:
        area = p['area_conhecimento']
        if area in resultado.keys():
            resultado[area] += 1
        else:
            resultado[area] = 1
    return resultado

# Pergunta 4 - <area_conhecimento, quantidade>
def projetos_por_area_AP(dados):
    resultado = {}
    for p in dados:
        if p['campus'] == 'AP':
            area = p['area_conhecimento']
            if area in resultado.keys():
                resultado[area] += 1
            else:
                resultado[area] = 1
    return resultado


# 7- (Carlos) Quantidade de projetos por ano do campus Apodi.,
#  (coluna, linha)
# <ano, quantidade>
# Pergunta7 - <ano, quantidade>
def projetos_por_ano_AP(dados):
    resultado = {}
    for p in dados:
        if p['campus']=='AP':
            dt_inicio = p['inicio_execucao']
            ano = int(dt_inicio[0:4])
            if ano in resultado.keys():
                resultado[ano] += 1
            else:
                resultado[ano] = 1
    return resultado


#  Resposta - Pergunta 4
resp4 = projetos_por_area(base)
for area in resp4.keys():
    print(f"{area}: {resp4[area]}")

pyplot.figure(41)
pyplot.title('Projetos Por Area')
pyplot.bar(range(len(resp4.keys())), resp4.values()) # range(len(
pyplot.savefig('figura-41.png')

pyplot.figure(42)
pyplot.title('Projetos Por Area')
pyplot.pie(resp4.values(), labels=resp4.keys())
#pyplot.legend(resp4.keys())
pyplot.savefig('figura-42.png')


# Resposta - Pergunta 7
resp7 = projetos_por_ano_AP(base)
for ano in resp7.keys():
    print(f"{ano}: {resp7[ano]}")

pyplot.figure(7)
pyplot.title('Projetos por Ano')
pyplot.xlabel('Anos')
pyplot.ylabel('Qtde. Projetos')
pyplot.plot( list(resp7.keys()), \
  list(resp7.values()), '-*r')
#pyplot.show()
pyplot.savefig('figura-7.png')
print(len(base))

# texto = arquivo.read()
# partes = texto.split(';')
# print(partes[0])

# for linha in arquivo.readlines():
#     partes = linha.split(';')
#     print(partes[0])
#     break