# Este programa busca una direccion de correo y guarda la frecuencia en un diccionario
mail = dict()
fh = open('mbox.txt')
for lines in fh:
    if not lines.startswith('From: ') : continue
    lines = lines.rstrip()
    words = lines.split()
    for word in words:
        mail[word] = mail.get(word,0)+1

print (mail)
