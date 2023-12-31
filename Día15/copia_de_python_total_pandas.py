# -*- coding: utf-8 -*-
"""Copia de Python TOTAL - Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fDU87eR_S8EGgdkCQZVC_4HZ_RPhIZaI

# Práctica de la librería Pandas

En este notebook, se desarrollarán una serie de tareas utilizando la librería Pandas (el "Excel" de Python).

Se proponen y documentan posibles formas de resolver los ejercicios, pero pueden existir varias formas de lograr los mismos resultados.

Siempre es una buena idea verificar la [Documentación Oficial de Pandas](https://pandas.pydata.org/pandas-docs/stable/), donde es posible encontrar todo tipo de información referida a esta librería. Y si te quedas trabado, busca en Google "como hacer [algo] con Pandas". Hay enormes probabilidades de que esa pregunta ya haya sido respondida!
"""

# Importamos Pandas
import pandas as pd

# Creamos una serie de números y hallamos su media
numeros = pd.Series([1,2,3,5,67,35,235,62])
numeros.mean()

# Hallamos la suma de dichos números
numeros.sum()

# Creamos una SERIE de tres colores diferentes
colores = pd.Series(['Rojo','Amarillo','Verde'])

# Visualizamos la serie creada
colores

# Creamos una serie con tipos de autos, y la visualizamos
autos = pd.Series(['Sedan','SUV','Pickup'])
autos

# Combinamos las series de tipos de autos y colores en un DATAFRAME
tabla_autos = pd.DataFrame({'Tipo de auto':autos,'Color':colores})
tabla_autos

# Conectamos el cuaderno actual con nuestro Drive
from google.colab import drive
drive.mount('/content/drive')

# Importar "ventas-autos.csv" y convertirlo en un nuevo DATAFRAME
ventas_autos = pd.read_csv('/content/drive/MyDrive/Mis_Colabs_CP/ventas-autos.csv')
ventas_autos

"""Este será nuestro "Dataframe de Flujo Vehicular"
"""

# Exportar el Dataframe como un archivo CSV a mi carpeta "/content/drive/MyDrive/Colab Notebooks/pruebas/"
ventas_autos.to_csv('/content/drive/MyDrive/Mis_Colabs_CP/este-archivo.csv')

# Analicemos los tipos de datos disponibles en el dataset de ventas autos
ventas_autos.dtypes

# Apliquemos estadística descriptiva (cantidad de valores, media, desviación estándar, valores mínimos y máximos, cuartiles) al dataset
ventas_autos.describe()

# Obtenemos información del dataset utilizando info()
ventas_autos.info()

# Listamos los nombres de las columnas de nuestro dataset
ventas_autos.columns

# Averiguamos el "largo" de nuestro dataset
len(ventas_autos)

# Mostramos las primeras 5 filas del dataset
ventas_autos.head()

# Mostramos las primeras 7 filas del dataset
ventas_autos.head(7)

# Mostramos las últimas 5 filas del dataset
ventas_autos.tail()

# Utilizamos .loc para seleccionar la fila de índice 3 del DataFrame
ventas_autos.loc[3]

# Utilizamos .iloc para seleccionar las filas 3, 7 y 9
ventas_autos.iloc[[3,7,9]]

"""En la documentación podrás observar la diferencia entre el funcionamiento de [.loc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html) e [.iloc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html)."""

# Seleccionar la columna "Kilometraje"
ventas_autos['Kilometraje']

# Encontrar el valor medio de la columnas "Kilometraje"
ventas_autos['Kilometraje'].mean()

# Seleccionar aquellas columnas que tengan valores superiores a 100,000 kilómetros en la columna Kilometraje
ventas_autos[ventas_autos['Kilometraje']>100000]

# Creamos una tabla cruzada de doble entrada entre Fabricante y cantidad de puertas
pd.crosstab(ventas_autos['Fabricante'],ventas_autos['Puertas'])

# Agrupamos las columnas por fabricante y buscandos el valor medio de las columnas numéricas
ventas_autos.groupby(['Fabricante']).mean()

# Commented out IPython magic to ensure Python compatibility.
# Importamos Matplotlib y creamos un gráfico con los valores de la columna Kilometraje
import matplotlib as plt
# %matplotlib inline
ventas_autos['Kilometraje'].plot()

# Puede que un gráfico más apropiado en este caso sea un histograma?
ventas_autos['Kilometraje'].hist()

# Intentamos graficar la columna de precios
ventas_autos['Precios (USD)'].plot()

"""No funcionó, verdad? Alguna idea de por qué esto puede ocurrir?

Una pista es buscar: "cómo convertir strings de Pandas a números"

[Aqui hay un enlace a StackOverflow referido a este tema](https://stackoverflow.com/questions/44469313/price-column-object-to-int-in-pandas).
"""

# Elimina la puntuación de la columna de precios
ventas_autos['Precio (USD)'] = ventas_autos['Precio (USD)'].str.replace("[\,\$\.]","")
ventas_autos['Precio (USD)'] = ventas_autos['Precio (USD)'].astype(int)/100
ventas_autos

ventas_autos['Precio (USD)'].plot()