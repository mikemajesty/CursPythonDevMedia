import datetime;
import mysql.connector;
import cgi;

def printHeader():
    print("Content-Type:text/html")
    print()
    print("<html>")
    print("<head>")
    print("<title>")
    print("Projeto pratico - Livro de visitas")
    print("</title>")
    print("</head>")
    print("<body>")


def printFooter():   
    print("</body>")
    print("</html>")


printHeader();
print("<h2>livro de visitas</h2>");
print("<form method='Post' action='aula25.py'>")#Abertura do form
print("<p>Nome:<input type='text' name='nome'/></p>")
print("<p>Email:<input type='email' name='email'/></p>")
print("<p>Mensagem:<input type='text' name='mensagem'/></p>")
print("<p><input type='submit' value='Enviar'/> </p>")#button
print("</form>")#Fechamento do form



form = cgi.FieldStorage();
if len(form) > 0 :
    print("<h5>Entrou</h5>");
    cnx = mysql.connector.connect(host="localhost",database="guestbook",user="root",password="mikemajesty");
    print("<h5>"+cnx+"</h5>");
    cursor = cnx.cursor();
    add_guest = ("INSERT INTO GUESTS(name,email,date,message) VALUES(%s,%s,%s,%s)");    
    data_guest = (form["nome"].value,form["email"].value,datetime.datetime.now(),form["mensagem"].value);
    cursor.execute(add_guest,data_guest);
    cnx.commit();
    cursor.close();
    cnx.close();
    print("Insert OK");

printFooter();