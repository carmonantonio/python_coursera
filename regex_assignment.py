# this program takes a .txt file retrieve the numbers in it and sums it
import re
fname = input('Please enter a file name: ')
handle =open(fname)
numbers = list()
for line in handle:
    line = line.rstrip()