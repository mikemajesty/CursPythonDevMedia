print('------------------------Dictionaries----------------------------')

myDictionaryHeight = {"Mike":1.60,"Natali":1.60,"Mae":1.50,"Pai":2.0};

print("A altura do Mike e: ", myDictionaryHeight["Mike"]);
print("A altura da Natali e: ", myDictionaryHeight["Natali"]);
print("A altura do Mae e: ", myDictionaryHeight["Mae"]);
print("A altura do Pai e: ", myDictionaryHeight["Pai"]);
print("Todas as alturas ",myDictionaryHeight);
print("----------------------------------------------------");
myDictionaryHeight["Mike"] = 1.80;
print("A nova altura do Mike e: ", myDictionaryHeight["Mike"]);
myDictionaryHeight["Sergio"] = 1.0;

print("Todas as alturas ",myDictionaryHeight);

del myDictionaryHeight["Sergio"];

print("Todas as alturas ",myDictionaryHeight);
print('----------------------------------------------------')

def histogram(text):
    myDictionary = dict();
    for txt in text:
        if txt not in myDictionary:
            myDictionary[txt] = 1;
        else:
            myDictionary[txt] += 1;
    return myDictionary;

def print_histogram(dict):
    for c in dict:
        print(c,dict[c]);

result = histogram("mike is a great promgramming");
print_histogram(result);


