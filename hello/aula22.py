import cgi;


def printHeader():
    print("Content-Type:text/html");
    print()
    print("<html>")
    print("<head>")
    print("<title>")
    print("Formularios com python");
    print("</title>")
    print("</head>")
    print("<body>");


def printFooter():   
    print("</body>");
    print("</html>");


printHeader();

print("<h1>Completar o formluario de exemplo</h1>");#Uma mensagem no form

print("<form method='Post' action='aula22.py'>");#Abertura do form

print("<p> Nome: <input type='text' name='Nome'/> </p>");#Input de texto com uma label
print("<p> Sobrenome: <input type='text' name='Sobrenome'/> </p>");#Input de texto com uma label
print("<p>    Sexo: <br> Masculino: <input type='radio' value='Masculino' name='Sexo'/> </p>");
print("<p>Feminino: <input type='radio' value='Feminino' name='Sexo'/> </p>");
print("<p> Compania: <input type='text' name='Compania'/> </p>");#Input de texto com uma label
print("<p>");
print("Cor favorita: <select name='Cor'>");#Abertura do select


print("<option value='Select'>");#Abertura do option
print("Select");#opcao
print("</option>");#Fechamento do option
print("<option value='Cinza'>");#Abertura do option
print("Cinza");#opcao
print("</option>");#Fechamento do option
print("<option value='Vermelho'>");#Abertura do option
print("Vermelho");#opcao
print("</option>");#Fechamento do option
print("<option value='Azul'>");#Abertura do option
print("Azul");#opcao
print("</option>");#Fechamento do option
print("<option value='Verde'>");#Abertura do option
print("Verde");#opcao
print("</option>");#Fechamento do option
print("<option value='Amarelo'>");#Abertura do option
print("Amarelo");#opcao
print("</option>");#Fechamento do option

print("</select>");#Fechamento do select
print("</p>")
print("<hr>")
print("<p><input type='submit' value='Enviar'/> </p>");#button


print("</form>");#Fechamento do form
printFooter();

form = cgi.FieldStorage();

if len(form) > 0 and form["Cor"].value != "Select":
    print("<hr><h3>Result:</h3>");
    if "Nome" in form:
         print("<br><h3>Nome: %s </h3>" % cgi.escape(form["Nome"].value));
    if "Sobrenome" in form:
         print("<br><h3>Sobrenome: %s </h3>" % cgi.escape(form["Sobrenome"].value));
    if "Sexo" in form:
         print("<br><h3>Sexo: %s </h3>" % cgi.escape(form["Sexo"].value));
    if "Compania" in form:
         print("<br><h3>Compania: %s </h3>" % cgi.escape(form["Compania"].value));
    if "Cor" in form:
         print("<br><h3>Cor: %s </h3>" % cgi.escape(form["Cor"].value));