# calculator for general store

sum = 0
while (True):
 userinput = input("enter the item price or press q to quit \n")
 if (userinput != 'q'):
     sum = sum + int(userinput)
     print(f"order total so far :{sum} \n")

 else:
    print(f"{sum} thanks for shopping")
    break






