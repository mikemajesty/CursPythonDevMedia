from tkinter import*;
root = Tk();
myLbl = Label(root,text="Hello Word!!!");
myLbl.pack();



class App:
   def __init__(self, master):
        frame  = Frame(master);
        frame.pack();

        self.btnQuit = Button(frame,text="Sair",fg="yellow",command=self.sair);
        self.btnQuit.pack(side=LEFT);
    
        self.btnHello = Button(frame,text="Hello",command=self.hello);
        self.btnHello.pack(side=LEFT);
        
   def sair(self):
        root.destroy();
   def hello(self):
       print("Hello Mike");


app = App(root);
root.mainloop()
