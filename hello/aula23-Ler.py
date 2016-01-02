import cgi


def printHeader():
    print("Content-Type:text/html")
    print()
    print("<html>")
    print("<head>")
    print("<title>")
    print("Salvando no .txt")
    print("</title>")
    print("</head>")
    print("<body>")


def printFooter():   
    print("</body>")
    print("</html>")
printHeader()
print("<h1>Ler no txt</h1>")#Uma mensagem no form
print("<form method='Post' action='aula23-Ler.py' enctype='multipart/form-data'>")#Abertura do form
print("<p>Arquivo:<input type='file' name='file'/></p>")
print("<hr>")
print("<p><input type='submit' value='Enviar'/> </p>")#button
print("</form>")#Fechamento do form


form = cgi.FieldStorage()

if "file" in form:
    fileItem = form["file"]
    if not fileItem.file:
        print("<h3>Nenhum arquivo encontrado</h3>")
    else:
        txt_file = open(fileItem.filename,"r")
        print("<hr><h3>Result: </h3>")
        for line in txt_file:
            datas = line.split(".")
            print("<p>Nome: " + datas[0] + "<br>")
            print("Sobrenome: " + datas[1] + "<br>")
            print("Sexo: " + datas[2] + "<br>");
            print("Compania: " + datas[3] + "<br>");
            print("Cor: " + datas[4] + "<br>");
            print("</p>");
else:
    print("<h3>Nenhum arquivo selecionado</h3>")
printFooter();


