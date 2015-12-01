print('Estrutura while')
total = 0
while total <= 100:
    print("%d loop interaction \n " % total)
    total = total + 1

print('Outra Estrutura while')
fator = input("Type your number")
fator = int(fator)
if fator > 0:
    step = fator;
    total = fator;
    while step > 1:
        step = step -1;
        total = total * step;
    print('The factor is',(fator));
elif fator == 0:
    print('The factor of 0 is',(fator));
else:
     print('The factor isnt exists');