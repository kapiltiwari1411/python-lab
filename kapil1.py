#check prime number
num=int(input("enter the number"))
i=2
while(i<num):
         if  num%i==0:
          print("not prime")
          i=i+1
else:
               print("prime")
