import calculator_logic as cl

# collect user input
while True:
  operation = input("Choose action-> Add(a), Subtract(s), Multiply(m), Divide(d) [EXIT](e): ")
  if operation == 'e':
    print("Goodbye")
    break
  num1 = int(input("Enter num1: "))
  num2 = input("Enter num2: ")
  



  if operation == 'a':
    print(cl.add(num1, num2))
  elif operation == 's':
    print(cl.subtract(num1, num2))
  elif operation == 'm':
    print(cl.multiply(num1, num2))
  elif operation == 'd':
    print(cl.divide(num1, num2))
  else:
    print("Invalid input!")
