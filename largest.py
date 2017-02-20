largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if largest is None and smallest is None:
        largest = num
        smallest = num
    elif largest < num:
        largets = num
    elif smallest > num:
        smallest = num
        
    if num == "done" : break
    if len(num) < 1: break 
    try:
        num = float(num)
    except:
        print("Invalid input")	
    continue
    
        
       

print ("Maximum is", largest)
print ("Minimun is", smallest)