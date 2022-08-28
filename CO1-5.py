import math
print("JOYAL JOSE\n21MCA026")
a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
c=int(input("Enter 3rd number : "))
d=(b*b)-(4*a*c)
if d==0:
    result=-b/2*a
    print ("The solution is : ",result)
elif (d<0):
    print("No solution")
else:
    result = (-b+math.sqrt(d))/(2*a)
    result1 = (-b-math.sqrt(d))/(2*a)
    print("The solutions are : ",result , result1)
