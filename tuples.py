fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
lst = list()
for key,val in counts.items():
    lst.append((val,key))

lst.sort(reverse=True)

for val,key in lst[:10]:
    print (key, val)

# shorter version:
c = {'a':1,'b':2,'c':3}
print(sorted([(v,k) for k,v in c.items()] ,reverse=True))