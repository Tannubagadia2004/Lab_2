# To calculate simple intrest
principal=int(input("ENter principal value : "))
rate=7.1/100
time=int(input("Enter months : "))
si=principal*rate*time/100
if principal<500:
    print("Principal value is small.")
elif time<6:
    print("Time must be atleast 6 months")
else :
    print("simple intrest :",si)