import bs4
import requests

#crear una url sin numero de página
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

#lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

#iterrar paginas
for pagina in range(1,51):
    #crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text,'lxml')
    
    #seleccionar datos de los libros
    libros = sopa.select('.product_pod')
    
    #iterar libros
    for libro in libros:
        #checar estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):
            #guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']
            
            #agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)
            
#Ver los libros en consola
for t in titulos_rating_alto:
    print(t)

#resultado = requests.get(url_base.format('1'))
#sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
#libros = sopa.select('.product_pod')
#ejemplo = libros[0].select(".star-rating.Three")
#ejemplo = libros[0].select("a")[1]['title']
#print(ejemplo)