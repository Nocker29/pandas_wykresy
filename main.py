import numpy as np
import pandas as pd
import xlrd
import openpyxl

xlsx=pd.ExcelFile('imiona.xlsx')
df=pd.read_excel(xlsx,header=0)

#zad1
# df = pd.read_excel('imiona.xlsx', header=0)
# grupa=df.groupby(['Rok']).agg({'Liczba':['sum']})
# wykres=grupa.plot()
# wykres.set_xlabel('Rok')
# wykres.set_ylabel('Liczba')
# plt.title('Liczba urodzonych dzieci dla każdego roku')
# plt.show()

#zad2
# grupa=df.groupby(['Plec']).agg({'Liczba':['sum']})
# wykres=grupa.plot.bar()
# wykres.legend()
# plt.xticks(rotation=0)
# plt.title("Liczba urodzonych chłopców i dziewczynek")
# plt.show()

#zad3
# grupa=df[df['Rok']>2012].groupby(['Plec']).agg({'Liczba':['sum']})
# wykres=grupa.plot.pie(subplots=True,autopct='%.2f %%')
# plt.legend()
# plt.show()

#zad4
# df=pd.read_csv('zamowienia.csv',delimiter=';')
# grupa=df.groupby(['Sprzedawca']).size()
# grupa.plot.bar()
# plt.ylabel('Liczba zamówień')
# plt.show()