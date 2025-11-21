import time

result = None

def add(num1, num2):
  try:
    result = int(num1) + int(num2)
    time.sleep(1)
    print(f"Result: {result}")
  except ValueError:
    print("Cannot perform operations with letters!")
  finally:
    time.sleep(1)
    print("Restarting...")
    time.sleep(1)

def subtract(num1, num2):
  try:
    result = int(num1) - int(num2)
    print(f"Result: {result}")
  except ValueError:
    print("Cannot perform operations with letters!")
  finally:
    print("Done...")

def multiply(num1, num2):
  try:
    result = int(num1) * int(num2)
    print(f"Result: {result}")
  except ValueError:
    print("Cannot perform operations with letters!")
  finally:
    print("Done...")

def divide(num1, num2):
  try:
    result = int(num1) / int(num2)
    print(f"Result: {result}")
  except ZeroDivisionError:
      print("Cannot divide a number by zero!")
  except ValueError:
    print("Cannot perform operations with letters!")
  finally:
    print("Exiting...")


