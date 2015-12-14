print('Ordenar list');
myList = [1,28.35,465,56,66,76,86,96];
print('\n Itens in original order: ');
for x in myList:
    print(x);
print('\n Itens after crescent sort : ');
myList.sort();
for x in myList:
    print(x);
print('\n Itens after descrecent sort : ');
myList.reverse();
for x in myList:
    print(x);
print('\n Size of list',len(myList));
print('\n Count itens in list',myList.count(465));

print('--------------Sorting and Searching in lits');
myNewList = ['Mike','Lima','Rodrigues','Programador','Fantasma','Igreja','Padre'];
searchString = input('Type your word: ');
if searchString in myNewList:
    print("Found at index: ",myNewList.index(searchString));
else: 
    print('Not found');

