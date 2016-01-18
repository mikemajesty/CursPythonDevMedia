from tkinter import *;

class MouseLocation(Frame):
    def __init__(self):
       Frame.__init__(self)
       self.pack(expand=YES,fill=BOTH)
       self.master.title("Mouse Evente e KeyBoard");
       self.master.geometry("300x300");

       self.mousePosition = StringVar();
       self.mousePosition.set("Mouse outside window");

       self.positionLabel = Label(self,textvariable=self.mousePosition);
       self.positionLabel.pack(side=BOTTOM);

       self.bind("<Button-1>",self.buttonLeftClick);
       self.bind("<Button-3>",self.buttonRigthClick);

       self.bind("<ButtonRelease-1>",self.buttonLeftRelease);

       self.bind("<Enter>",self.enterWindow);
       self.bind("<Leave>",self.exitWindow);

       self.bind("<B1-Motion>",self.mouseDragged);


       self.master.bind("<KeyPress>",self.keyPressed);
       self.master.bind("<KeyRelease>",self.keyReleased);

    def buttonLeftRelease(self,event):
        self.mousePosition.set("LEFT BUTTON RELEASED AT: ["+str(event.x)+" , "+str(event.y)+"]");

    def keyPressed(self,event):
        messagebox.showinfo("keyPressed")
    def keyReleased(self,event):    
        messagebox.showinfo("keyReleased")
    def enterWindow(self,event):
        self.mousePosition.set("Mouse in Window");
    def exitWindow(self,event):
        self.mousePosition.set("Mouse outside Window");
    def mouseDragged(self,event):
        self.mousePosition.set("Mouse dragged at  ["+str(event.x)+" , "+str(event.y)+"]");

    def buttonLeftClick(self,event):
        self.mousePosition.set("LEFT BUTTON PRESSED AT: ["+str(event.x)+" , "+str(event.y)+"]");
    def buttonRigthClick(self,event):
        self.mousePosition.set("RIGHT BUTTON PRESSED AT: ["+str(event.x)+" , "+str(event.y)+"]");

def main():
    MouseLocation().mainloop();

if __name__ == "__main__":
    main()
