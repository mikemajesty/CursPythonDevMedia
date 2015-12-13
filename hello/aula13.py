print("Lists");
myList = [1,2,3,4,5,1,2,3,4,5];
print("position 0:",myList[0]);
print("position 1:",myList[1]);
print("position 2:",myList[2]);
print("position 3:",myList[3]);
print("position 4:",myList[4]);
print("position 5:",myList[5]);
print("position 6:",myList[6]);
print("position 7:",myList[7]);
print("position 8:",myList[8]);
print("position 9:",myList[9]);
print("Quantity: ",len(myList));
print('--------------------------------------------------------');
myNewList = [];

myNewList.insert(0,"Mike");
myNewList.insert(1,"Lima");
myNewList.insert(3,"DevMedia");
myNewList.insert(6,"Cursos");
myNewList.insert(9,"SP");
myNewList.insert(2,"Rio");

myNewList[1] = "69";

for x in myNewList:
    print(x);
print("Quantity: ",len(myNewList));
print('----------------------');

import random;

myRandomList = [];

for x in range(25):
    myRandomList.append(random.randrange(1,100,1));
print(myRandomList);
print("Quantity of items in list: ",len(myRandomList));