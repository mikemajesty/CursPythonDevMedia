import cgi;


def printHeader():
    print("Content-Type:text/html");
    print()
    print("<html>")
    print("<head>")
    print("<title>")
    print("Formularios com python - Get");
    print("</title>")
    print("</head>")
    print("<body>");


def printFooter():   
    print("</body>");
    print("</html>");


printHeader();
print("<h1>Formularios com method GET </h1>");
print("<form method='GET' action='aula21-GET.py'>");
print("<p> Compania: <input type='text' name='txtCompania'/> </p>");

print("<p> Compania: <input type='submit' value='Enviar' name='btnEnviar'/> </p>");


pairs = cgi.parse();

if "txtCompania" in pairs:
    print("<p> sua compania e:<b> %s </b> </p>" % (cgi.escape(pairs["txtCompania"][0])))

print("</form>");
printFooter();



