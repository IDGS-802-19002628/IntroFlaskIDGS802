from io import open

#escribir en un archivo
archivo_texto = open("anombres.txt", 'r')
for lineas in archivo_texto.readlines():
    print(lineas.rstrip())
#print(archivo_texto.read())
#archivo_texto.seek(0)
#print(archivo_texto.read())
#archivo_texto.write('\n Datos de archivos')
archivo_texto.close()

#leer contenido de un archivo
#print(archivo_texto.read())