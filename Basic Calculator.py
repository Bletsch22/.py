#operations
add = "+"
subtract ="-"
divide = "/"
multiply = "*"

#input variables
print("Basic Calculator")
num1 = input("Number1:")
operation = input("+ - * /  :  ")
num2 = input("Number2:")

#Error Variables

errors = "Missing inputs to calculate"
error1 = "Cannot calculate: Missing input 1"
error2 = "Cannot calculate: Missing input 2"
missing_ops = "No Operation Selected"

#error Statements
if num1 == "" or num2 == "":
  print(errors)
elif num1 =="":
  print(error1)
elif num2 == "":
  print(error2)
elif operation == "":
  print(missing_ops)  
else:
  num1 = int(num1)
  num2 = int(num2)

#convert from string to intiger

if operation == add:
  total = num1 + num2
elif operation == subtract:
  total = num1 - num2
elif operation == divide:
  total = num1 / num2
else: 
  operation == multiply
  total = num1 * num2


print("Total:", total)