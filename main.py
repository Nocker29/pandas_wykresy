import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#zad1
df = pd.read_excel('imiona.xlsx', header=0)
grupa=df.groupby(['Rok']).agg({'Liczba':['sum']})
wykres=grupa.plot()
wykres.set_xlabel('Rok')
wykres.set_ylabel('Liczba')
plt.title('Liczba urodzonych dzieci dla każdego roku')
plt.show()