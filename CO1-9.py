print("JOYAL JOSE\n21MCA026")
n1=int(input("Enter the limit of 1st and 2nd list list : "))
l1=[]
print("Enter the 1st list elements : ")
for i in range(0,n1):
   x=int(input())
   l1.append(x)
l2 = []
print("Enter the 2nd list elements : ")
for i in range(0, n1):
   y = int(input())
   l2.append(y)
l3=[]
for i in range(0,len(l1)):
   l3.append(l1[i] + l2[i])
print("First list           : ",l1)
print("Second list          : ",l2)
print("Lists after addition : ",l3)