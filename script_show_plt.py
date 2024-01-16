# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os


cols = ['Severity', 'Start_Time', 'City', 'County', 'State', 'Temperature(F)', 'Visibility(mi)',
        'Humidity(%)', 'Precipitation(in)', 'Weather_Condition',
       'Traffic_Signal', 'Sunrise_Sunset']

df = pd.read_csv("US_Accidents_March23.csv", usecols=cols)

df.isnull().sum()


## Eliminar celdas en blanco y NAs
df['Precipitation(in)'].fillna(0, inplace=True)
df.dropna(axis=0, inplace=True)

df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')

# Opcional: eliminar filas donde 'Start_Time' es NaT
df.dropna(subset=['Start_Time'], inplace=True)


df['Week_day'] = df['Start_Time'].dt.dayofweek
df['Month'] = df['Start_Time'].dt.month
df['Year'] = df['Start_Time'].dt.year

df['Week_day'] = df['Week_day'].map({0:'Monday', 1:'Tuesday', 2: 'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'})
df['Month'] = df['Month'].map({1:'January', 2:'February', 3: 'March', 4:'April', 5:'May', 6:'June', 7:'July',
                                  8:'August', 9:'September', 10: 'October', 11:'November', 12:'December'})

df.drop("Start_Time", axis=1, inplace=True)



import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly
import plotly.graph_objs as go
import plotly.offline as py

# Asume que ya tienes el dataframe 'df' cargado y procesado como en tu script original

# Agrupar y contar severidades
severity = df['Severity'].groupby(by=df['Severity']).count()

# Seleccionar datos para graficar
data = [go.Pie(labels=severity.index,
               values=severity.values,
               direction='clockwise')]

# Editar estilo
layout = go.Layout(title='Severity of accidents',
                   width=600,
                   height=600)

# Crear figura
fig = go.Figure(data=data, layout=layout)

# Graficar y guardar en un archivo HTML
py.plot(fig, filename='severity_of_accidents.html')


import pandas as pd
import plotly.graph_objs as go
import plotly.offline as py

# Asume que ya tienes el dataframe 'df' cargado y procesado

# Crear un DataFrame para contar accidentes por año
accidents_years = pd.DataFrame(df['Year'].groupby(df['Year']).count())

# Crear datos para el gráfico de barras
data = [go.Bar(x=[2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
               y=accidents_years['Year'])]

# Configurar el layout del gráfico
layout = go.Layout(title='Accidents by year 2016-June 2023',
                   xaxis={'title': 'Year'},
                   yaxis={'title': 'Number of accidents'},
                   width=700,
                   height=600)

# Crear la figura
fig = go.Figure(data=data, layout=layout)
fig.update_yaxes(nticks=4)

# Guardar el gráfico en un archivo HTML
py.plot(fig, filename='accidents_by_year.html')



m2016 = pd.DataFrame(df['Month'].groupby(by=df['Month'].loc[df['Year']==2016]).count())

m2017 = pd.DataFrame(df['Month'].groupby(by=df['Month'].loc[df['Year']==2017]).count())

m2018 = pd.DataFrame(df['Month'].groupby(df['Month'].loc[df['Year']==2018]).count())

m2019 = pd.DataFrame(df['Month'].groupby(df['Month'].loc[df['Year']==2019]).count())

m2020 = pd.DataFrame(df['Month'].groupby(df['Month'].loc[df['Year']==2020]).count())

m2021 = pd.DataFrame(df['Month'].groupby(df['Month'].loc[df['Year']==2021]).count())

m2022 = pd.DataFrame(df['Month'].groupby(df['Month'].loc[df['Year']==2022]).count())

m2023 = pd.DataFrame(df['Month'].groupby(df['Month'].loc[df['Year']==2023]).count())

## First we filter the data by Month and then, count the times the month appear in a year (indexed by loc)
## Remember "Month" at the left is index, "month" at the right is the column, this will be usefull when creating a new organized dataframe later on

accidents_months_2016 = pd.DataFrame({'Month of the year - 2016': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
               'Total Accidents':          [0, 
                                            m2016['Month'].loc[m2016.index=='February'].sum(),      
                                            m2016['Month'].loc[m2016.index=='March'].sum(), 
                                            m2016['Month'].loc[m2016.index=='April'].sum(), 
                                            m2016['Month'].loc[m2016.index=='May'].sum(),
                                            m2016['Month'].loc[m2016.index=='June'].sum(), 
                                            m2016['Month'].loc[m2016.index=='July'].sum(), 
                                            m2016['Month'].loc[m2016.index=='August'].sum(),  
                                            m2016['Month'].loc[m2016.index=='September'].sum(),      
                                            m2016['Month'].loc[m2016.index=='October'].sum(), 
                                            m2016['Month'].loc[m2016.index=='November'].sum(), 
                                            m2016['Month'].loc[m2016.index=='December'].sum()]})

accidents_months_2017 = pd.DataFrame({'Month of the year - 2017': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                                      'Total Accidents': [m2017['Month'].loc[m2017.index=='January'].sum(), 
                                                          m2017['Month'].loc[m2017.index=='February'].sum(),
                                                          m2017['Month'].loc[m2017.index=='March'].sum(), 
                                                          m2017['Month'].loc[m2017.index=='April'].sum(), 
                                                          m2017['Month'].loc[m2017.index=='May'].sum(),
                                                          m2017['Month'].loc[m2017.index=='June'].sum(),
                                                          m2017['Month'].loc[m2017.index=='July'].sum(), 
                                                          m2017['Month'].loc[m2017.index=='August'].sum(),  
                                                          m2017['Month'].loc[m2017.index=='September'].sum(),      
                                                          m2017['Month'].loc[m2017.index=='October'].sum(), 
                                                          m2017['Month'].loc[m2017.index=='November'].sum(), 
                                                          m2017['Month'].loc[m2017.index=='December'].sum()]})
accidents_months_2018 = pd.DataFrame({'Month of the year - 2018': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
               'Total Accidents':          [m2018['Month'].loc[m2018.index=='January'].sum(), 
                                            m2018['Month'].loc[m2018.index=='February'].sum(),      
                                            m2018['Month'].loc[m2018.index=='March'].sum(), 
                                            m2018['Month'].loc[m2018.index=='April'].sum(), 
                                            m2018['Month'].loc[m2018.index=='May'].sum(),
                                            m2018['Month'].loc[m2018.index=='June'].sum(), 
                                            m2018['Month'].loc[m2018.index=='July'].sum(), 
                                            m2018['Month'].loc[m2018.index=='August'].sum(),  
                                            m2018['Month'].loc[m2018.index=='September'].sum(),      
                                            m2018['Month'].loc[m2018.index=='October'].sum(), 
                                            m2018['Month'].loc[m2018.index=='November'].sum(), 
                                            m2018['Month'].loc[m2018.index=='December'].sum()]})
accidents_months_2019 = pd.DataFrame({'Month of the year - 2019': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
               'Total Accidents':          [m2019['Month'].loc[m2019.index=='January'].sum(), 
                                            m2019['Month'].loc[m2019.index=='February'].sum(),      
                                            m2019['Month'].loc[m2019.index=='March'].sum(), 
                                            m2019['Month'].loc[m2019.index=='April'].sum(), 
                                            m2019['Month'].loc[m2019.index=='May'].sum(),
                                            m2019['Month'].loc[m2019.index=='June'].sum(), 
                                            m2019['Month'].loc[m2019.index=='July'].sum(), 
                                            m2019['Month'].loc[m2019.index=='August'].sum(),  
                                            m2019['Month'].loc[m2019.index=='September'].sum(),      
                                            m2019['Month'].loc[m2019.index=='October'].sum(), 
                                            m2019['Month'].loc[m2019.index=='November'].sum(), 
                                            m2019['Month'].loc[m2019.index=='December'].sum()]})
accidents_months_2020 = pd.DataFrame({'Month of the year - 2020': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
               'Total Accidents':          [m2020['Month'].loc[m2020.index=='January'].sum(), 
                                            m2020['Month'].loc[m2020.index=='February'].sum(),      
                                            m2020['Month'].loc[m2020.index=='March'].sum(), 
                                            m2020['Month'].loc[m2020.index=='April'].sum(), 
                                            m2020['Month'].loc[m2020.index=='May'].sum(),
                                            m2020['Month'].loc[m2020.index=='June'].sum(), 
                                            m2020['Month'].loc[m2020.index=='July'].sum(), 
                                            m2020['Month'].loc[m2020.index=='August'].sum(),  
                                            m2020['Month'].loc[m2020.index=='September'].sum(),      
                                            m2020['Month'].loc[m2020.index=='October'].sum(), 
                                            m2020['Month'].loc[m2020.index=='November'].sum(), 
                                            m2020['Month'].loc[m2020.index=='December'].sum()]})

accidents_months_2021 = pd.DataFrame({'Month of the year - 2021': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
               'Total Accidents':          [m2021['Month'].loc[m2021.index=='January'].sum(), 
                                            m2021['Month'].loc[m2021.index=='February'].sum(),      
                                            m2021['Month'].loc[m2021.index=='March'].sum(), 
                                            m2021['Month'].loc[m2021.index=='April'].sum(), 
                                            m2021['Month'].loc[m2021.index=='May'].sum(),
                                            m2021['Month'].loc[m2021.index=='June'].sum(), 
                                            m2021['Month'].loc[m2021.index=='July'].sum(), 
                                            m2021['Month'].loc[m2021.index=='August'].sum(),  
                                            m2021['Month'].loc[m2021.index=='September'].sum(),      
                                            m2021['Month'].loc[m2021.index=='October'].sum(), 
                                            m2021['Month'].loc[m2021.index=='November'].sum(), 
                                            m2021['Month'].loc[m2021.index=='December'].sum()]})

accidents_months_2022 = pd.DataFrame({'Month of the year - 2022': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
               'Total Accidents':          [m2022['Month'].loc[m2022.index=='January'].sum(), 
                                            m2022['Month'].loc[m2022.index=='February'].sum(),      
                                            m2022['Month'].loc[m2022.index=='March'].sum(), 
                                            m2022['Month'].loc[m2022.index=='April'].sum(), 
                                            m2022['Month'].loc[m2022.index=='May'].sum(),
                                            m2022['Month'].loc[m2022.index=='June'].sum(), 
                                            m2022['Month'].loc[m2022.index=='July'].sum(), 
                                            m2022['Month'].loc[m2022.index=='August'].sum(),  
                                            m2022['Month'].loc[m2022.index=='September'].sum(),      
                                            m2022['Month'].loc[m2022.index=='October'].sum(), 
                                            m2022['Month'].loc[m2022.index=='November'].sum(), 
                                            m2022['Month'].loc[m2022.index=='December'].sum()]})


accidents_months_2023 = pd.DataFrame({'Month of the year - 2023': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
               'Total Accidents':          [m2023['Month'].loc[m2023.index=='January'].sum(), 
                                            m2023['Month'].loc[m2023.index=='February'].sum(),      
                                            m2023['Month'].loc[m2023.index=='March'].sum(), 
                                            m2023['Month'].loc[m2023.index=='April'].sum(), 
                                            m2023['Month'].loc[m2023.index=='May'].sum(),
                                            m2023['Month'].loc[m2023.index=='June'].sum(), 
                                            m2023['Month'].loc[m2023.index=='July'].sum(), 
                                            m2023['Month'].loc[m2023.index=='August'].sum(),  
                                            m2023['Month'].loc[m2023.index=='September'].sum(),      
                                            m2023['Month'].loc[m2023.index=='October'].sum(), 
                                            m2023['Month'].loc[m2023.index=='November'].sum(), 
                                            m2023['Month'].loc[m2023.index=='December'].sum()]})

data = [go.Bar(x=accidents_months_2016['Month of the year - 2016'],
               y=accidents_months_2016['Total Accidents'],
               name='2016'),
        go.Bar(x=accidents_months_2017['Month of the year - 2017'],
               y=accidents_months_2017['Total Accidents'],
               name='2017'),
        go.Bar(x=accidents_months_2018['Month of the year - 2018'],
               y=accidents_months_2018['Total Accidents'],
               name='2018'),
        go.Bar(x=accidents_months_2019['Month of the year - 2019'],
               y=accidents_months_2019['Total Accidents'],
               name='2019'),
        go.Bar(x=accidents_months_2020['Month of the year - 2020'],
               y=accidents_months_2020['Total Accidents'],
               name='2020'),

        go.Bar(x=accidents_months_2021['Month of the year - 2021'],
               y=accidents_months_2021['Total Accidents'],
               name='2021'),

        go.Bar(x=accidents_months_2022['Month of the year - 2022'],
               y=accidents_months_2022['Total Accidents'],
               name='2022'),

        go.Bar(x=accidents_months_2023['Month of the year - 2023'],
               y=accidents_months_2023['Total Accidents'],
               name='2023')
        ]

layout = go.Layout(title='Accidents per month - February 2016 - May 2023',
                   xaxis={'title':'Month of the year'},
                   yaxis={'title':'Number of accidents'},
                   width=1700,
                   height=700)

fig = go.Figure(data=data, layout=layout)

py.plot(fig, filename='accidents_by_month.html')



d2016 = pd.DataFrame(df['Week_day'].loc[df['Year']==2016].groupby(df['Week_day']).count())

d2017 = pd.DataFrame(df['Week_day'].loc[df['Year']==2017].groupby(df['Week_day']).count())

d2018 = pd.DataFrame(df['Week_day'].loc[df['Year']==2018].groupby(df['Week_day']).count())

d2019 = pd.DataFrame(df['Week_day'].loc[df['Year']==2019].groupby(df['Week_day']).count())

d2020 = pd.DataFrame(df['Week_day'].loc[df['Year']==2020].groupby(df['Week_day']).count())
d2021 = pd.DataFrame(df['Week_day'].loc[df['Year']==2021].groupby(df['Week_day']).count())
d2022 = pd.DataFrame(df['Week_day'].loc[df['Year']==2022].groupby(df['Week_day']).count())
d2023 = pd.DataFrame(df['Week_day'].loc[df['Year']==2023].groupby(df['Week_day']).count())


days_2016 = pd.DataFrame({'Day of the week - 2016': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
               'Total Accidents':          [d2016['Week_day'].loc[d2016.index=='Monday'].sum(), 
                                            d2016['Week_day'].loc[d2016.index=='Tuesday'].sum(),      
                                            d2016['Week_day'].loc[d2016.index=='Wednesday'].sum(), 
                                            d2016['Week_day'].loc[d2016.index=='Thursday'].sum(), 
                                            d2016['Week_day'].loc[d2016.index=='Friday'].sum(),
                                            d2016['Week_day'].loc[d2016.index=='Saturday'].sum(), 
                                            d2016['Week_day'].loc[d2016.index=='Sunday'].sum()]})

days_2017 = pd.DataFrame({'Day of the week - 2017': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
               'Total Accidents':          [d2017['Week_day'].loc[d2017.index=='Monday'].sum(), 
                                            d2017['Week_day'].loc[d2017.index=='Tuesday'].sum(),      
                                            d2017['Week_day'].loc[d2017.index=='Wednesday'].sum(), 
                                            d2017['Week_day'].loc[d2017.index=='Thursday'].sum(), 
                                            d2017['Week_day'].loc[d2017.index=='Friday'].sum(),
                                            d2017['Week_day'].loc[d2017.index=='Saturday'].sum(), 
                                            d2017['Week_day'].loc[d2017.index=='Sunday'].sum()]})

days_2018 = pd.DataFrame({'Day of the week - 2018': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
               'Total Accidents':          [d2018['Week_day'].loc[d2018.index=='Monday'].sum(), 
                                            d2018['Week_day'].loc[d2018.index=='Tuesday'].sum(),      
                                            d2018['Week_day'].loc[d2018.index=='Wednesday'].sum(), 
                                            d2018['Week_day'].loc[d2018.index=='Thursday'].sum(), 
                                            d2018['Week_day'].loc[d2018.index=='Friday'].sum(),
                                            d2018['Week_day'].loc[d2018.index=='Saturday'].sum(), 
                                            d2018['Week_day'].loc[d2018.index=='Sunday'].sum()]})
days_2019 = pd.DataFrame({'Day of the week - 2019': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
               'Total Accidents':          [d2019['Week_day'].loc[d2019.index=='Monday'].sum(), 
                                            d2019['Week_day'].loc[d2019.index=='Tuesday'].sum(),      
                                            d2019['Week_day'].loc[d2019.index=='Wednesday'].sum(), 
                                            d2019['Week_day'].loc[d2019.index=='Thursday'].sum(), 
                                            d2019['Week_day'].loc[d2019.index=='Friday'].sum(),
                                            d2019['Week_day'].loc[d2019.index=='Saturday'].sum(), 
                                            d2019['Week_day'].loc[d2019.index=='Sunday'].sum()]})
days_2020 = pd.DataFrame({'Day of the week - 2020': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
               'Total Accidents':          [d2020['Week_day'].loc[d2020.index=='Monday'].sum(), 
                                            d2020['Week_day'].loc[d2020.index=='Tuesday'].sum(),      
                                            d2020['Week_day'].loc[d2020.index=='Wednesday'].sum(), 
                                            d2020['Week_day'].loc[d2020.index=='Thursday'].sum(), 
                                            d2020['Week_day'].loc[d2020.index=='Friday'].sum(),
                                            d2020['Week_day'].loc[d2020.index=='Saturday'].sum(), 
                                            d2020['Week_day'].loc[d2020.index=='Sunday'].sum()]})
days_2021 = pd.DataFrame({'Day of the week - 2021': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
               'Total Accidents':          [d2021['Week_day'].loc[d2021.index=='Monday'].sum(), 
                                            d2021['Week_day'].loc[d2021.index=='Tuesday'].sum(),      
                                            d2021['Week_day'].loc[d2021.index=='Wednesday'].sum(), 
                                            d2021['Week_day'].loc[d2021.index=='Thursday'].sum(), 
                                            d2021['Week_day'].loc[d2021.index=='Friday'].sum(),
                                            d2021['Week_day'].loc[d2021.index=='Saturday'].sum(), 
                                            d2021['Week_day'].loc[d2021.index=='Sunday'].sum()]})
days_2022 = pd.DataFrame({'Day of the week - 2022': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
               'Total Accidents':          [d2022['Week_day'].loc[d2022.index=='Monday'].sum(), 
                                            d2022['Week_day'].loc[d2022.index=='Tuesday'].sum(),      
                                            d2022['Week_day'].loc[d2022.index=='Wednesday'].sum(), 
                                            d2022['Week_day'].loc[d2022.index=='Thursday'].sum(), 
                                            d2022['Week_day'].loc[d2022.index=='Friday'].sum(),
                                            d2022['Week_day'].loc[d2022.index=='Saturday'].sum(), 
                                            d2022['Week_day'].loc[d2022.index=='Sunday'].sum()]})
days_2023 = pd.DataFrame({'Day of the week - 2023': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
               'Total Accidents':          [d2023['Week_day'].loc[d2023.index=='Monday'].sum(), 
                                            d2023['Week_day'].loc[d2023.index=='Tuesday'].sum(),      
                                            d2023['Week_day'].loc[d2023.index=='Wednesday'].sum(), 
                                            d2023['Week_day'].loc[d2023.index=='Thursday'].sum(), 
                                            d2023['Week_day'].loc[d2023.index=='Friday'].sum(),
                                            d2023['Week_day'].loc[d2023.index=='Saturday'].sum(), 
                                            d2023['Week_day'].loc[d2023.index=='Sunday'].sum()]})
data = [go.Bar(x=days_2016['Day of the week - 2016'],
               y=days_2016['Total Accidents'],
               name='2016'),
        go.Bar(x=days_2017['Day of the week - 2017'],
               y=days_2017['Total Accidents'],
               name='2017'),
        go.Bar(x=days_2018['Day of the week - 2018'],
               y=days_2018['Total Accidents'],
               name='2018'),
        go.Bar(x=days_2019['Day of the week - 2019'],
               y=days_2019['Total Accidents'],
               name='2019'),
        go.Bar(x=days_2020['Day of the week - 2020'],
               y=days_2020['Total Accidents'],
               name='2020'),
        go.Bar(x=days_2021['Day of the week - 2021'],
               y=days_2021['Total Accidents'],
               name='2021'),
        go.Bar(x=days_2022['Day of the week - 2022'],
               y=days_2022['Total Accidents'],
               name='2022'),
        go.Bar(x=days_2023['Day of the week - 2023'],
               y=days_2023['Total Accidents'],
               name='2023')]

layout = go.Layout(title='Accidents per day - February 2016 - June 2020',
                   xaxis={'title':'Day of the week'},
                   yaxis={'title':'Number of accidents'},
                   width=1700,
                   height=700)

fig = go.Figure(data=data, layout=layout)

py.plot(fig, filename='accidents_by_day_week.html')


cities = df['City'].value_counts()[df['City'].value_counts() > 0]

print(cities)


county = df['County'].value_counts()[df['County'].value_counts()>10000]
print(county)


state = df['State'].value_counts()
print(state)



df.loc[ (df['Humidity(%)'] > 0) & (df['Humidity(%)'] <= 20), 'Humidity(%)']=1
df.loc[ (df['Humidity(%)'] > 20) & (df['Humidity(%)'] <= 40), 'Humidity(%)' ]=2
df.loc[ (df['Humidity(%)'] > 40) & (df['Humidity(%)'] <= 60), 'Humidity(%)']=3
df.loc[ (df['Humidity(%)'] > 60) & (df['Humidity(%)'] <= 80),'Humidity(%)' ]=4
df.loc[  df['Humidity(%)'] > 80, 'Humidity(%)']=5

hum = df['Humidity(%)'].value_counts()
print(hum)

ts = df['Traffic_Signal'].value_counts()
print(ts)


ss = df['Sunrise_Sunset'].value_counts()
print(ss)


import matplotlib.pyplot as plt
import seaborn as sns


df['Severity'] = df['Severity'].astype('category')
df['Traffic_Signal'] = df['Traffic_Signal'].astype('category')

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Visibility(mi)', y='Severity')
plt.title('Relación entre Visibilidad y Severidad de Accidentes')
plt.xlabel('Visibilidad (mi)')
plt.ylabel('Severidad')
plt.savefig('Visibilidad_Severidad_Grafico.png')


import plotly.express as px

# Suponiendo que 'df' es tu DataFrame y que contiene las columnas 'Severity' y 'Traffic_Signal'

# Convertir 'Traffic_Signal' a tipo string para facilitar el manejo
df['Traffic_Signal'] = df['Traffic_Signal'].astype(str)

# Crear una tabla pivote para contar los accidentes por severidad y presencia de señal de tráfico
pivot_table = df.pivot_table(index='Severity', columns='Traffic_Signal', aggfunc='size', fill_value=0)

# Normalizar los valores por fila para obtener proporciones
normalized_pivot = pivot_table.div(pivot_table.sum(axis=1), axis=0).reset_index()

# Preparar los datos para Plotly
data_for_plotly = normalized_pivot.melt(id_vars='Severity', var_name='Traffic_Signal', value_name='Proportion')

# Crear el gráfico interactivo
fig = px.bar(data_for_plotly, x='Severity', y='Proportion', color='Traffic_Signal', barmode='stack',
             labels={'Proportion':'Proporción de Accidentes', 'Traffic_Signal':'Señal de Tráfico'},
             title='Proporción de Accidentes con y sin Señal de Tráfico por Severidad')

# Mostrar el gráfico
fig.show()
fig.write_html("proportion_accidents_traffic_signal.html")


