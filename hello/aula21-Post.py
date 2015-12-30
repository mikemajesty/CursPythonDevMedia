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
print("<form method='Post' action='aula21-Post.py'>");

print("<p> Sexo: <br> Masculino: <input type='radio' value='Masculino' name='rdbSexo'/> </p>");
print("<p>Feminino: <input type='radio' value='Feminino' name='rdbSexo'/> </p>");
print("<p><input type='submit' value='Enviar'/> </p>");

pairs = cgi.parse();

if "rdbSexo" in pairs:
    print("<p> sua sexo e:<b> %s </b> </p>" % (cgi.escape(pairs["rdbSexo"][0])))

print("</form>");
printFooter();



