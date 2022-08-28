print("JOYAL JOSE\n21MCA026")
n=int(input("Enter the limit : "))
a=0
b=1
print("\nFibonacci numbers are: \n")
print(a,"    ",end="")
print(b,"    ",end="")

for i in range(1,n):
    c=a+b
    a=b
    b=c
    print(c,"    ",end="")
