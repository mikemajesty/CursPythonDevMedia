from aula29_C_PrivateTest import PrivateTest, Retangle;
myClass = PrivateTest();
print(myClass.publicData);
print(myClass._PrivateTest__privateData);
myRectangle = Retangle();
myRetangle2 = Retangle(2,2);
print("\n O resultado da area e: ",myRectangle.resultAre)
print("\n O resultado da area e: ",myRetangle2.resultAre)

del myRectangle;

