fname = 'mbox.txt'
fh = open(fname)
count = 0
adress = list()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From: ') : continue
    words = line.split()
    for x in words:
        if x not in adress:
            adress.append(x)
    count = count + 1
print(adress)
print ("there are", count, "entries in this file and", len(adress),"unique addresses")