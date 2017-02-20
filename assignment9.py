# this section open and split the file
name = 'mbox.txt'
handle = open(name)
text = handle.read()
words = text.split()
# This section count the frequencies 
counts = dict()
for word in words:
   counts[word] = counts.get(word,0)+1
print(counts)
