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
#for item in sorted(dicio, key = dicio.get, reverse=True):
  # print(item)

