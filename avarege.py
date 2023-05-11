total=0
count=0

inputStr= int(input("Enter range"))

for i in range (0,inputStr):
  #  print(inputStr)
    R1=float(input("Enter value"))
    total=total+R1
    count = count+1

    

    
if count>0:
    average = total/count
    print(average)
else:
    average= 0.0
    pri(average)
    
