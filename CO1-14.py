print("JOYAL JOSE\n21MCA026")
num='9947168565'
ph=input("Enter phone numer : ")
if (len(ph)!=10):
    print("invalid number")
print("missing numbers are ")
for i in range(10):
    if num[i]!=ph[i]:
        print(num[i],end=" ")
