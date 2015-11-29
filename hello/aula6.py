print("Test if/else")
velocity = input("Enter your name")
velocity = int(velocity)
if velocity > 100:
    print("velocity, you are too fast!!!!")
else:
    print("velocity, you are not too fast!!!!")

print("Finish")

grade1 = input("Enter your grade")
grade1 = int(grade1)
if grade1 > 9:
   print("Your grade is A");
   print("Congratulation");
elif grade1 > 8:
   print("Your grade is B");
   print("Good");
elif grade1 > 7:
   print("Your grade is C");
   print("Maybe");
elif grade1 > 6:
   print("Your grade is D");
   print("Bad");
else:
   print("Your grade is E");
   print("Horrible");