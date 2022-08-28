import math
print("JOYAL JOSE\n21MCA026")
a=int(input("Enter a number : "))
b=int(input("Enter another number : "))
if math.gcd(a,b) == 1:
    print("Given numbers are Co-prime")
else:
    print("Given numbers are not  Co-prime ")
