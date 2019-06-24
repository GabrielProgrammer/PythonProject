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

if op == 4:
    from operator import itemgetter

    arq = open('sales.csv', 'r')
    entrada = input('Digite o nome do desenvolvedor:\n')
    entrada = entrada.lower()
    dicio = {}
    dicio_2 = {}
    k = 0
    sales = 0
    jump = 0
    h = 0
    for linha in arq:
        dev = linha.split(',')
        dev[14] = dev[14].lower()
        if entrada == dev[14]:
            dicio[dev[14]] = dicio.setdefault(dev[14], 0) + 1
            if jump == 0:
                jump += 1
                continue
            else: 
                if dev[0] not in dicio_2:
                    sales = dev[9]
                    float(sales)
                    dicio_2[dev[0]] = float(sales)
                else:
                    sales = dev[9]
                    float(sales)
                    dicio_2[dev[0]] = dicio_2.setdefault(dev[0], 0) + float(sales)
    
    dicio_2 = sorted(dicio_2.items(), key = itemgetter(1), reverse = True)

    for nome in dicio:
        print('Esse DEVELOPER desenvolveu',dicio[nome], 'jogos\n')
        
    arq.close()
    for c,v in dicio_2:
        if k == 0:
            string = c
            k = 1
    arq = open('sales.csv', 'r')
    for linha in arq:
       jogo = linha.split(',')
       if jogo[0] == string:
          print('¨¨¨¨¨ANO DO JOGO MAIS VENDIDO¨¨¨¨¨\n')
          print('JOGO: ',string, '\n')
          print('ANO DE LANÇAMENTO: ',jogo[2])
    arq.close()



