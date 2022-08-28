print("JOYAL JOSE\n21MCA026")
n1 = int(input("Enter the lower limit : "))
n2 = int(input("Enter the upper limit : "))
print("Amstrong numbers are:")

for i in range(n1,n2):
    count = len(str(i))
    temp = i
    sum = 0
    while i > 0:
        digit = i % 10
        sum += digit ** count
        i //= 10
    if temp == sum:
        print(temp)