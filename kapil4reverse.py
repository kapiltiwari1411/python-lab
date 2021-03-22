#program to find reverse of enterd number.
num=int(input("please enter any number"))
reverse=0.
while(num>0):
      reminder=num%10
      reverse=(reverse*10)+reminder
      num=num//10.
print(" reverse of the entered number\n", reverse)
