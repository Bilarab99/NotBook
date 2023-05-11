# perfect number
for i in range (2,101):
    sum=0
    for j in range (1,i):
        if  i % j == 0:
            sum=sum+j
    if sum == i :
        print("the perfec number" , i )
        