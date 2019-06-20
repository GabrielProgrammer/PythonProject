print('#####Bem-vindo(a) ao BD dos dados históricos de jogos:#####\n ESCOLHA UMA OPÇÃO')
print('1 - Todos os Jogos que foram vendidos: \n 2 - Top 10 Developers mais bem-sucedidos: \n 3 - Top 10 jogos que mais venderam: \n 4 - Resumo de um Developer: \n 5 - Atualize a tabela ccom um novo jogo: \n')
op = int(input())

if op == 1:    
    arq = open('sales.csv', 'r')
    for linha in arq:
        jogos = linha.split(',')
        print (jogos[0])
    arq.close()




