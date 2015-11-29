print("test Equality and relationla operators")
number1 = input("Enter first number: ")
number1 = int(number1)
number2 = input("Enter second number: ")
number2 = int(number2)

if number1 == number2:
    print("%d is Equals to %d" % (number1,number2))

if number1 != number2:
   print("%d is not Equals to %d" % (number1,number2))
if number1 < number2:
   print("%d is less than %d" % (number1,number2))
if number1 > number2:
   print("%d is greater than %d" % (number1,number2))
if number1 <= number2:
   print("%d is less or equals than %d" % (number1,number2))
if number1 >= number2:
   print("%d is graeter or equals than %d" % (number1,number2))