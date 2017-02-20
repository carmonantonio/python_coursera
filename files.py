fname = "mbox.txt"
fh = open(fname)
count = 0 
add = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        add = add + float(line[line.find(":")+1:])
        count = count + 1
print("Se consiguieron",count,"Lineas")
print("las cuales suman",add)
print("Para un promedio de:", add / count)

