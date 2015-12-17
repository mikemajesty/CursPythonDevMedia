print("Tuples");

myTuple = ('Mike',2015,'Fatec',900.80,'F');
print("\nItens in my Tuple: ",myTuple);
print('\nQuantity of itens: ',len(myTuple));
print('\nElements in position 3:',myTuple[3]);
print("--------------------------------");
myNewTuple = 1,'Fiat',  'Palio',2002;
print("\nItens in my Tuple: ",myNewTuple);
print('\nQuantity of itens: ',len(myNewTuple));
print('\nElements in position 3:',myNewTuple[3]);
print("--------------------------------");
mySecondTuple = 'XYZ',;
print("\nItens in my Tuple: ",mySecondTuple);
print('\nQuantity of itens: ',len(mySecondTuple));
print('\nElements in position 0:',mySecondTuple[0]);
print("--------------------------------");
myThirdTuple = tuple('Mike');
print("\nItens in my Tuple: ",myThirdTuple);
print('\nQuantity of itens: ',len(myThirdTuple));
print('\nElements in position 0:',myThirdTuple[0]);
for item in myThirdTuple:
    print(item);
print("--------------------------------");
myCarTuple = 'Fiat','Palio',2002,1.0,'Prata';
(automaker,model,year,cc,color) = myCarTuple;
print('automaker:',automaker);
print('model:',model);
print('year:',year);
print('cc:',cc);
print('color:',color);

