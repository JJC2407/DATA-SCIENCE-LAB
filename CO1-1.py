print("JOYAL JOSE\n21MCA026")
n1=int(input("Enter the fist number : "))
n2=int(input("Enter the last number : "))
for i in range(n1,n2):
    for j in range(2,i):
        if i % j == 0 :
           print(i)
           break
