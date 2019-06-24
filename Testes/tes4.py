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

#for l in dicio:
 #   h = l
  #  print(dicio)

#print('Esse DEVELOPER criou ',l,'jogos\n')
    
#print(dicio_2)
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

#print(dicio)
#print('\n')
#print(dicio_2)
