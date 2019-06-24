print('#####Bem-vindo(a) ao BD dos dados históricos de jogos:#####\n ESCOLHA UMA OPÇÃO')
print('1 - Todos os Jogos que foram vendidos: \n 2 - Top 10 Developers mais bem-sucedidos: \n 3 - Top 10 jogos que mais venderam: \n 4 - Resumo de um Developer: \n 5 - Atualize a tabela ccom um novo jogo: \n')
op = int(input())

if op == 1:    
    arq = open('sales.csv', 'r')
    for linha in arq:
        jogos = linha.split(',')
        print (jogos[0])
    arq.close()

if op == 2:
    arq = open('sales.csv', 'r')
    dicio = {}
    k = 0
    for linha in arq:
        dev = linha.split(',')
        if dev[14] not in dicio:
            dicio[dev[14]] = 1
        else:
            dicio[dev[14]] = dicio.setdefault(dev[14], 0) + 1
    arq.close()
    print(dicio)
if op == 3:
    from operator import itemgetter

    arq = open('sales.csv', 'r')
    dicio = {}
    posicao = 1
    jump = 0
    stop = 0
    k = 0
    c = 0
    v = 1
    for nome in arq:
        jogo = nome.split(',')
        if jump == 0:
            jump += 1
            continue
        else:
            
            if jogo[0] not in dicio:
                stop = jogo[9]
                float(stop)
                dicio[jogo[0]] = float(stop)
            else:
                stop = jogo[9]
                float(stop)
                dicio[jogo[0]] = dicio.setdefault(jogo[0], 0) + float(stop)
    arq.close()
    dicio = sorted(dicio.items(), key = itemgetter(1), reverse = True)
    print('####### TOP 10 JOGOS MAIS VENDIDOS NA HISTÓRIA #######')
    
    for name, key in dicio:
        print(posicao,'º', ' LUGAR - ', name, '\n', '   VENDAS GLOBAIS:', key, '\n')
        posicao += 1
        if posicao == 10:
            break



