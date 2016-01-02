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
print("<h1>Escrever no txt</h1>")#Uma mensagem no form
print("<form method='Post' action='aula23-Escrever.py'>")#Abertura do form
print("<p> Nome: <input type='text' name='Nome'/> </p>")#Input de texto com uma label
print("<p> Sobrenome: <input type='text' name='Sobrenome'/> </p>")#Input de texto com uma label
print("<p>    Sexo: <br> Masculino: <input type='radio' value='Masculino' name='Sexo'/> </p>")
print("<p>Feminino: <input type='radio' value='Feminino' name='Sexo'/> </p>")
print("<p> Compania: <input type='text' name='Compania'/> </p>")#Input de texto com uma label
print("<p>")
print("Cor favorita: <select name='Cor'>")#Abertura do select

print("<option value='Select'>")#Abertura do option
print("Select")#opcao
print("</option>")#Fechamento do option
print("<option value='Cinza'>")#Abertura do option
print("Cinza")#opcao
print("</option>")#Fechamento do option
print("<option value='Vermelho'>")#Abertura do option
print("Vermelho")#opcao
print("</option>")#Fechamento do option
print("<option value='Azul'>")#Abertura do option
print("Azul")#opcao
print("</option>")#Fechamento do option
print("<option value='Verde'>")#Abertura do option
print("Verde")#opcao
print("</option>")#Fechamento do option
print("<option value='Amarelo'>")#Abertura do option
print("Amarelo")#opcao
print("</option>")#Fechamento do option
print("</select>")#Fechamento do select
print("</p>")
print("<hr>")
print("<p><input type='submit' value='Enviar'/> </p>")#button
print("</form>")#Fechamento do form


form = cgi.FieldStorage()

if len(form) > 0 and form["Cor"].value != "Select" and form["Nome"].value != "" and form["Sobrenome"].value != "" and form["Compania"].value != "":  
    with open("txtResult.txt","w") as fileOutput:
        fileOutput.write(cgi.escape(form["Nome"].value) + ".")
        fileOutput.write(cgi.escape(form["Sobrenome"].value) + ".")
        fileOutput.write(cgi.escape(form["Sexo"].value) + ".")
        fileOutput.write(cgi.escape(form["Compania"].value) + ".")
        fileOutput.write(cgi.escape(form["Cor"].value) + ".")
    print("<hr><h2>Mensagem salva com sucesso</h2>")
printFooter()

