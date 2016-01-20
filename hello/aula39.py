from tkinter import *;

root = Tk();

topFrame = Frame(root);
topFrame.pack();

lowFrame = Frame(root);
lowFrame.pack(side=BOTTOM,expand=YES,fill=BOTH);

button1 = Button(topFrame,text="Button 1");
button1.pack(side=LEFT);

button2 = Button(topFrame,text="Button 2");
button2.pack(side=LEFT);

button3 = Button(topFrame,text="Button 3");
button3.pack(side=LEFT);

button4 = Button(lowFrame,text="Button 4");
button4.pack(side=BOTTOM,expand=YES,fill=X);



button5 = Button(root,text="Button 5")
button5.grid(row=1,column=1,padx=5,pady=5);

button6 = Button(root,text="Button 6")
button6.grid(row=1,column=2,padx=5,pady=5);

button7 = Button(root,text="Button 7")
button7.grid(row=2,column=1,padx=5,pady=5);

button8 = Button(root,text="Button 8")
button8.grid(row=2,column=2,padx=5,pady=5);

button9 = Button(root,text="Button 9")
button9.grid(row=3,column=1,padx=5,pady=5);

button10 = Button(root,text="Button 10")
button10.grid(row=3,column=2,padx=5,pady=5);

root.mainloop();

