print("JOYAL JOSE\n21MCA026")
a=int(input("Enter a number : "))
b=0
for i in range(1,a):
    if a%i == 0:
        b=b+i
if a == b:
    print("The number is perfect number ")
else:
    print("The number is not perfect ")