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
#for c,v in dicio.items():
dicio = sorted(dicio.items(), key = itemgetter(1), reverse = True)
print('####### TOP 10 JOGOS MAIS VENDIDOS NA HISTÓRIA #######')

for name, key in dicio:
    print(posicao,'º', ' LUGAR - ', name, '\n', '   VENDAS GLOBAIS:', key, '\n')
    posicao += 1
    if posicao == 10:
        break

        
    


    
    


#for nome in arq:
 #   jogo = nome.split(',')
  #  if jump == 0:
   #     jump = 1
    #    continue
    #else:
    #    print(posicao,'º', ' Lugar - ', jogo[0])
     #   posicao += 1
    #stop += 1
    #if stop == 10:
     #   break
    
        
    
    








#for linha in arq:
 #   jogo = linha.split(',')
  #  print(jogo[9])
    #if jogo[0] not in dicio:
     #   number = float(jogo[9])
      #  dicio[jogo[0]] = number
    #break
#arq.close()


