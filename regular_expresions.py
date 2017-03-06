import re
# This program retrieve the host on a email the traditional way
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = data.split()
email = words[1]
tmp = email.split('@')
host = tmp[1]
print(email)
print(host)
# And this lines do the same but in the regex way
y = re.findall('@([^ ]*)',data)
print (y)
x = 'From: Using the : character'
yy = re.findall('^F.+:', x)
print (yy)
xx=re.findall('\S+?@\S+',data)
print(xx)





