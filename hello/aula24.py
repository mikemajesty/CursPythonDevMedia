import cgi;
import os;
import sys;

import cgitb;

def printHeader():
    print("Content-Type:text/html")
    print()
    print("<html>")
    print("<head>")
    print("<title>")
    print("Upload arquivo")
    print("</title>")
    print("</head>")
    print("<body>")


def printFooter():   
    print("</body>")
    print("</html>")


printHeader();
print("<h1>Upload arquivos com python</h1>");

print("<h2>Upload de arquivos com python CGI</h2> <form action='aula24.py' method='post' enctype='multipart/form-data'> <p>Arquivo para upload <input type='file' name='fileName' /></p> <p><input type='submit' value='Upload File' /></p> </form>");
form = cgi.FieldStorage();

fileItem = form["fileName"];

if fileItem.filename:
    fn = os.path.basename(fileItem.file);
    open("./upload/"+fn,'wb').write(fileItem.file.read());
    print("<h1>O arquivo"+ fn +" foi salvo</h1>");
    print("<p>O tamanho do arquivo "+ fn +" e:"+str(os.path.getsize("./upload/"+fn))+" bytes</p>");
    print("<p>Link para o arquivo: <a href='"+"./upload/"+fn+"' target='_blank'>"+fn+"</a> </p>");
else:
    print("<h1>arquivos nao encontrado</h1>");
printFooter();