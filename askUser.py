import add
import subtract

def askUserToAdd():
      num1 = int(input("Enter number 1: ")) 
      num2 = int(input("Enter number 2: "))

      add.add(num1,num2)

def askUserToSubtract():
      num1 = int(input("Enter number 1: ")) 
      num2 = int(input("Enter number 2: "))

      subtract.subtract(num1,num2)

askUserToSubtract()
askUserToAdd()