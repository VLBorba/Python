primeiro = int(input('Qual o primeiro termo? '))
razão = int(input('Qual é a razão? '))
enésimo = primeiro+(10-1)*razão
for pa in range(primeiro, enésimo+razão, razão):
    print(pa, end='|')