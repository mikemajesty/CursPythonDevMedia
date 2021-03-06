from tkinter import *;

class RadioFont(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES,fill=BOTH);
        self.master.title("Demo of radiobutton, checkbutton and button with image");

        self.frame1 = Frame(self)
        self.frame1.pack();

        self.text = Entry(self.frame1,width=40,font="Arial 10");
        self.text.insert(INSERT,"lorem ipsum dolor sit amet")
        self.text.pack(padx=5,pady=5);


        self.frame2 = Frame(self);
        self.frame2.pack();

        self.chosenColor = StringVar();
        self.chosenColor.set(0);
        self.radioRed = Radiobutton(self.frame2,text="red",variable=self.chosenColor,value="red",command=self.changeColor);
        self.radioRed.pack(side=LEFT,padx=5,pady=5);

        self.radioGreen = Radiobutton(self.frame2,text="green",variable=self.chosenColor,value="green",command=self.changeColor);
        self.radioGreen.pack(side=LEFT,padx=5,pady=5);

        self.radioBlue = Radiobutton(self.frame2,text="blue",variable=self.chosenColor,value="blue",command=self.changeColor);
        self.radioBlue.pack(side=LEFT,padx=5,pady=5);

        
        self.frame3 = Frame(self);
        self.frame3.pack();
        
        self.boldOn = BooleanVar();
        self.checkBold = Checkbutton(self.frame3,text="Bold",variable=self.boldOn,command=self.ChangeFont)
        self.checkBold.pack(side=LEFT,padx=5,pady=5)

        self.italicOn = BooleanVar();
        self.checkItalic = Checkbutton(self.frame3,text="Italic",variable=self.italicOn,command=self.ChangeFont)
        self.checkItalic.pack(side=LEFT,padx=5,pady=5)

        self.frame4 = Frame(self);
        self.frame4.pack();


        path = "C:/Users/Mike/Documents/Visual Studio 2015/Projects/CursoDePython/hello/clear.jpg"

        self.myImageClear = PhotoImage(file=path);
        self.clearButton = Button(self.frame4,image=myImageClear,command=self.ClearText)
        self.clearButton.pack(side=LEFT,padx=5,pady=5)

       

    def ClearText(self):
        self.text.delete(0,END);

    def ChangeFont(self):
        desiredFont = "Arial 10"

        if self.boldOn.get():
            desiredFont += " bold"
        if self.italicOn.get():
            desiredFont += " italic"
        self.text.config(font=desiredFont);




    def changeColor(self):
        if self.chosenColor.get() == "red":
           self.text.configure(fg="red");
        elif self.chosenColor.get() == "green":
           self.text.configure(fg="green");
        elif self.chosenColor.get() == "blue":
           self.text.configure(fg="blue");
def main():
    RadioFont().mainloop();

if __name__ =="__main__":
    main();