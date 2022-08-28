print("JOYAL JOSE\n21MCA026")
n=int(input("Enter the limit of list : "))
a=[]
print("Enter the elements of list : ")
for i in range(n):
    x=int(input())
    a.append(x)
print("Before the bubble sort the elements are : ")
print(a)
for i in range(n-1):
    for j in range(n-1):
        if (a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print("After the bubble sort the elements are : ")
print(a)

