print('Sequencias Multidimensionais');

myTableList = [[1,2,3],[4,5,6],[7,8,9]];
for row in myTableList:
    for item in row:
        print(item,end=" ");
    print();

print('------------------------');
myTableTutle = ((1,2,3),(4,5,6),(7,8,9));
for row in myTableTutle:
    for item in row:
        print(item,end=" ");
    print();
print('------------------------');

listDeGrades = [[6.4,8.8,5.5,9.3],[7.5,2.0,9.2,8.0],[8.2,8.0,2.6,9.9],[7.7,4.5,6.3,9.9]];


def printList(inputList):
    print("Valor na lista: ");
    for row in inputList:
        for item in row:
            print(item,end=" ");
    print();

def avarage(gradeEstudantes):
    total = 0.0;
    for grade in gradeEstudantes:
        total += grade;
    return total / len(gradeEstudantes);

printList(listDeGrades);
for item in range(len(listDeGrades)):
    print("Media / Estudante: ",item," e ", avarage(listDeGrades[item]));