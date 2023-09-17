# Divisibility of y/x
x=int(input("Enter number_1 : "))
y=int(input("Enter number_2 : "))
if x<1 or y<1:
    print("Invalid")
elif y%x==0:
    print({y},"is divisible by",{x})
else:
    print({y},"is not divisible by",{x})
