Sum=0
n=input("Enter how many number if you input:")
n=int(n)

for i in range(n):
    num=input("Enter a " + str(i+1) + " number:")
    num=int(num)
    Sum=Sum+num
average=Sum/10
print("Sum:"+str(Sum))
print("average:"+str(average))