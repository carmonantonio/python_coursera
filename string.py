word = 'banana'
count = 0
for letter in word:
    if letter == "a":
        count = count + 1
    print(count)

if "ba" in word:
    print("Yeah baby")
elif "nana" in word:
    print("You got it")
dir(word)
x = 'From marquard@uct.ac.za'
print(x[15:18])
print (len('banana')*7)
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print (data[pos:pos+3])
stuff = "X\nY"
stuff
print(stuff)
print(len(stuff))
