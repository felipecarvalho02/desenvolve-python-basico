#Leitura de dados

comprimento = int(input("Digite o comprimento:  "))
largura = int(input('Digite a largura:  '))
preco_m2 = float(input("Valor do m2:  "))


#Processamento
area = comprimento * largura #m2
preco_total = area * preco_m2

#Impressão de dados (saida)
print(f"O terreno possui {area}m2 e custa R${preco_total:,.2f}")