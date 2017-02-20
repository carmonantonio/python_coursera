count = 0
total = 0
while True:
	inp = input("Hello, please enter a number:")
	if inp == "done": break
	if len(inp) < 1 : break
	try:
		num = float(inp)
	except:
		print("Invalid input")	
		continue
	count = count + 1
	total = total + num
	print(num,"Total acumulado",total,"total numbers",count)
print("Average is ",total / count)



