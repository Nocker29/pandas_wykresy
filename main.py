import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl as op

#zad1
df = pd.read_excel('imiona.xlsx', header=0)
grupa=df.groupby(['Rok']).agg({'Liczba':['sum']})
wykres=grupa.plot.bar()
wykres.set_xlabel('Rok')
wykres.set_ylabel('Liczba')
plt.title('Liczba urodzonych dzieci dla każdego roku')
plt.show()