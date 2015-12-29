import os;
import cgi;

def printHeader():
    print("Content-Type:text/html");
    print()
    print("<html>")
    print("<head>")
    print("<title>")
    print("Informacao sobre o sistema");
    print("</title>")
    print("</head>")
    print("<body>");


def printFooter():   
    print("</body>");
    print("</html>");


printHeader();



print("<----------------------------------------------------->")
print("<h1>Query String</h1>")


query = os.environ["QUERY_STRING"];
if len(query) == 0:
     print("<p>Por favor adcione alguma QUERY STRING</p>");
else:
     print("<p style='font-style:italic'>A QUERY STRING is: "+cgi.escape(query)+"</p>");
     pairs = cgi.parse_qs(query);
     for kay,value in pairs.items():
         print("<p>Voce adicionou a QUERY STRING '%s' para o valor '%s'</p>" %(kay,value));

rowNumber = 0;
backgroundColor ="";
print("<table style='border:1'>");



for x in os.environ.keys():
    rowNumber += 1;
    if rowNumber % 2 == 0:
        backgroundColor = "white"
    else:
         backgroundColor = "lightblue"
    print("<tr style='background-color:%s'>" % backgroundColor )
    print("<td>%s</td>" % cgi.escape(x))
    print("<td>%s</td>" % cgi.escape(os.environ[x]));
    print("</tr>")
print("</table");    
printFooter();


