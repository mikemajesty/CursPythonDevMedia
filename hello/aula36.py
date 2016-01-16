from tkinter import *;

class EntryDemo(Frame):
    def __init__(self):
        
        Frame.__init__(self)
        self.pack(expand=YES,fill=BOTH)
        self.master.title("Minha area de calculo do retangulo");
        self.master.geometry("200x10");
        self.configure(bg="#FF0000");
         #Lado 1
        self.frame1 = Frame(self)
        self.frame1.pack(pady=5)
        
        self.label1 = Label(self.frame1,fg="blue",bg="yellow",text="Tamaho 1:");
        self.label1.pack(side=LEFT,padx=6);
       
        self.text1 = Entry(self.frame1,width=17,name="numero1");
        self.text1.insert(INSERT,"Entre com o tamanho do lado 1");
        self.text1.pack(side=LEFT,padx=5);
                #Lado 2
        self.frame2 = Frame(self)
        self.frame2.pack(pady=5)
        
        self.label2 = Label(self.frame2,fg="green",bg="yellow",text="Tamaho 2:");
        self.label2.pack(side=LEFT,padx=6);
       
        self.text2 = Entry(self.frame2,width=17,name="numero2");
        self.text2.insert(INSERT,"Entre com o tamanho do lado 2");
        self.text2.pack(side=LEFT,padx=5);
         #Lado 3
        self.frame3 = Frame(self)
        self.frame3.pack(pady=5)
        
        self.button1 = Button(self.frame3,text="Sair",command=self.sair);
        self.button1.pack(side=LEFT,padx=5)

        self.button2 = Button(self.frame3,text="Calcular",command=self.calcular);
        self.button2.pack(side=LEFT,padx=5)


    def sair(self):
        self.master.destroy();
    def calcular(self):
        area = int(self.text1.get()) * int(self.text2.get());
        messagebox.showinfo("Resultado: ","A area do retangulo e: "+str(area));
def main():
    EntryDemo().mainloop();
if __name__ == "__main__":
    main();
       

