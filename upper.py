n=input()
if n>='A' and n<='Z':
    print("upper case")
elif n>='a' and n<='z':
    print("lower case")
elif n.isdigit():
      print("digit")
else:
    print("spacial characters")
