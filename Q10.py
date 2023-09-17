# Write a python program to convert given values (Seconds) to Hour, Minutes and second
a=int(input("Enter second : "))
hour=a//3600
b=a-(hour*3600)
min=b//60
sec=b-(min*60)
print("Hour : ",hour,"Minute :",min,"Second :",sec)