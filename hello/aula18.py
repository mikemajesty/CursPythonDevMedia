print('dictionary method')

myMonths = {1:"Janeiro",2:"Fevereiro",3:"Marco",4:"Abril",5:"Maio",6:"Junho",7:"Julho",8:"Agosto",9:"Setembro",10:"Outubro",11:"Novembro",12:"Dezembro"};

print("Os itens no meu dicionario e: ",myMonths.items(),"\n");

print("Os chaves do meu dicionario e: ",myMonths.keys(),"\n");

print("Os valores do meu dicionario e: ",myMonths.values(),"\n");

print("Os quantidade de itens no meu dicionario e: ",len(myMonths),"\n");

myInput = input("Digite o mes do seu aniversario ");
myInput = int(myInput);
if myInput in myMonths:
    print("Seu mes de aniversario e ", myMonths[myInput])
else:
    print("Mes nao existe");


newCopia = myMonths.copy();

newCopia[13] = "Nada";
print("Item 13 do dicionario e :",newCopia[13],"\n");

myNewDict={0:"Zero",14:"Fora"}

myMonths.update(myNewDict);
print("Os valores do meu dicionario e: ",myMonths.values(),"\n");

myMonths.clear();
print("Os valores do meu dicionario e: ",myMonths.values(),"\n");

