# This section open the file and split it
name = 'romeo-full.txt'
handle = open(name,'r')
text = handle.read()
words = text.split()
adress = words[1]
# This section calculate the frequency

counts = dict()
for word in words:
    counts[word] = counts.get(word,0)+1

# This section select the more frequent
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print (bigword,bigcount) 
