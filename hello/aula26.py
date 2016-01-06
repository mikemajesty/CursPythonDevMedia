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
print("<h2>Bem vindo ao PYTHON");

printFooter();