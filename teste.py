arq = open('sales.csv', 'r')
dicio = {}
k = 0
for linha in arq:
    dev = linha.split(',')
    if dev[14] not in dicio:
        dicio[dev[14]] = 1
    else:
        dicio[dev[14]] = dicio.setdefault(dev[14], 0) + 1
    
    print (dicio)
arq.close()
