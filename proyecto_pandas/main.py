import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show

datos = pd.read_csv('data/5matriz-de-monitoreo-de-calidad-del-agua-2013.csv')
fecha = datos['FECHA'].tolist()
campana = datos.groupby(['FECHA']).
print(fecha)
print(campana)

print(datos.info())

nuevo = pd.DataFrame(datos)
print(nuevo)

p = figure(plot_width=800, plot_height=700)


p.line(datos['X'], datos['Y'], color='red', alpha=0.5)
output_file('prueba.html')
show(p)
