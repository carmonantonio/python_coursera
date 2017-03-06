# this program takes a .txt file retrieve the numbers in it and sums it
import re
fname = 'regex_sum_353133.txt'
handle =open(fname)
numbers = list()
for line in handle:
    line = line.rstrip()
    x = re.findall(('[0-9]+'),line)
    if len(x) > 0:
        for y in x:
            val = int(y)
            numbers.append(val)
print('There are:',len(numbers), 'numbers in the file')
print(sum(numbers))


