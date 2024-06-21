#Implemente um codigo que receba o nome e a data de nascimento de duas pessoas
#na forma "Nome completo,DD/MM/AAAA" e imprime o primeiro nome da pessoa mais velha. 
#Considere apenas o ano de nascimento

linha = "Alice de Sa, 29/12/1951"
linha.split('/')

Entrada:
Alice de Sa, 29/12/1951
Manuela Garcia, 11/02/1976
Camila Laranjeira, 11/02/1993
Saida:

mais_velha = ['', float('inf')]
for i in range(3):
    linha = input()
    primeiro_nome = linha.split()[0]
    ano_nascimento = int(linha.split('/') [-1])
    print(primeiro_nome, ano_nascimento)
    if ano_nascimento < mais_velha[1]:
        print('mais velha ate agora')
        mais_velha[0] = primeiro_nome
        mais_velha[1] = ano_nascimento

print(mais_velha[0])