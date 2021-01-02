import re

ref_texto = open("texto.txt",encoding="utf-8") #variable que contiene la referencia al archivo

cont_texto = ref_texto.read() #leemos el archivo

ref_texto.close() #cerramos el archivo de la memoria

print(cont_texto)

#match, search y findall metodos para buscar expresiones
#match busca en la primer linea de nuestro archivo
#search busca en todo el archivo pero devuelve un match
#findall busca en todo el archivo y devuelve todos los matchs!

print(re.findall(r"\+\d\(\d{3}\)-\(\d{4}\)-\(\d{4}\)-\(\d{4}\)",cont_texto))
#https://regexr.com/

#nuevo ejercicio 

