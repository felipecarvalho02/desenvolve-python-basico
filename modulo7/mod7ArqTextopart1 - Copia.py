import sys, os

if len(sys.argv) == 1:
    print("Informe o nome do arquivo como argumento! Encerrando...")
    sys.exit()

    nome_arquivo = sys.argv[1]
    if not os.path.islife(nome_arquivo):
        print(f'Arquivo {nome_arquivo} não encontrado. Encerrando...')
        sys.exit()

fp = open(nome_arquivo, 'rt')
fp_saida = open("invertido.txt", 'w')
for linha in fp:
    fp_saida.write(linha[::-1])
p_saida.close()
fp.close()

input()
    
    