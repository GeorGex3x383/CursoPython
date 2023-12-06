import bs4
import requests

#resultado = requests.get("https://escueladirecta-blog.blogspot.com")
resultado = requests.get("https://www.escueladirecta.com/courses/")

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#print(sopa.select('title')[0].get_text())

#parrafo = sopa.select('h3')[2].get_text()
#print(parrafo)

#columna = sopa.select('.post-header-line-1')
#print(columna)

imagen = sopa.select('.course-box-image')[0]['src']
print(imagen)

imagen_curso = requests.get(imagen)

f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso.content)
f.close()