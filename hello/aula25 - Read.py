import datetime
import mysql.connector
import cgi

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
cnx = mysql.connector.connect(host="localhost",database="guestbook",user="root",password="mikemajesty");
cursor = cnx.cursor();
cursor.execute("SELECT * FROM GUESTS")
row = cursor.fetchone()
print("<table>")
 while row is not None:
     print("<tr>");
     print("<td>");
     print(str(row[0]));
     print("</td>");
     print("<td>");
     print(str(row[1]));
     print("</td>");
     print("<td>");
     print(str(row[2]));
     print("</td>");
     print("<td>");
     print(str(row[3]));
     print("</td>");
     print("<td>");
     print(str(row[4]));
     print("</td>");
     row = cursor.fetchone();
     print("</tr>");
print("</table>");
cursor.close();
cnx.close();
printFooter();

 