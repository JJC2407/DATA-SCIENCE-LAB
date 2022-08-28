print("JOYAL JOSE\n21MCA026")
n1=int(input("Enter the 1st side : "))
n2=int(input("Enter the 2nd side : "))
n3=int(input("Enter the 3rd side : "))
if n1==n2==n3:
    print("\nTraingle is equiltarel")
elif n1==n2 or n2==n3 or n1==n3:
    print("\nTriangle is isosiles")
else:
    print("\nTriangle is scalar")
