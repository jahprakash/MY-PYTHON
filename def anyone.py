def anyone():
  name=input("enter your name")
  age=int(input("enter your age"))
  rollnumber=int(input("enter your roll number"))
  addition=age+rollnumber
  print("the sum is: ",addition)
  mul=age*rollnumber
  print("the multiplication is: ",mul)
  return name,age,rollnumber
anyone()
