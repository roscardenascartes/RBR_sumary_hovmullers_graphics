# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import os

#%%

#Directorio de datos
datadir = "/home/rc/Documents/OneDrive-UdeC/TRABAJOS_INDEPENDIENTES/COPAS_Diego_Narváez/TORTEL_hr/Horarios_Jun2024/Upgraded_processed2025_down/"

#Lista de archivos CSV
data_list=[
    "CTD Bahia de Tortel 24 Hrs 17 junio 1230 hrs_upgraded_profile0.csv",
    "CTD Bahia de Tortel 24 Hrs 17 Junio 1430_upgraded_profile0.csv",
    "CTD Bahia de Tortel 24 Hrs 17 junio 1630_upgraded_profile0.csv",
    "CTD Bahia de Tortel 24 Hrs 17 junio 1830_upgraded_profile0.csv",
    "CTD Bahia de Tortel 24 Hrs 17 Junio 2030_upgraded_profile0.csv",
    "CTD Bahia de Tortel 24 Hrs 17  Junio 2230 hrs_upgraded_profile0.csv",
    "CTD Bahia de Tortel 24 Hrs 18 Junio 0030 hrs_upgraded_profile0.csv",
    "CTd BAhia de Tortel 24 Hrs 18 Junio 0230 hrs_upgraded_profile0.csv",
    "CTD BAhia de Tortel 24 Hrs 18 Junio 0430 hrs_upgraded_profile0.csv",
    "CTD Bahia de Tortl  24 Hrs 18 Junio 0630hrs_upgraded_profile0.csv",
    "CTD Bahia de Tortel 24 Hrs 18 de Junio 0830 hrs_upgraded_profile0.csv",
    "CTD Bahia de Tortel 24 Hrs 18 Junio 1030 hrs_upgraded_profile0.csv",
    "CTD Bahia de Tortel 24 Hrs 18 Junio 1030 hrs_upgraded_profile1.csv",
    "CTD Bahia de Tortel 24 Hrs 18 junio 1230 hrs_upgraded_profile0.csv",
]

title='17 y 18 de junio 2024'
#%%

datadir = "/home/rc/Documents/OneDrive-UdeC/TRABAJOS_INDEPENDIENTES/COPAS_Diego_Narváez/TORTEL_hr/Horario_Jul2024_processed2025_down/"



#Lista de archivos CSV
data_list=[
    "CTD Bahia de tortel 17 de Julio de 2024 1200 Hrs_upgraded_profile0.csv",
    "CTD bahia de tortel 17 de julio de 2024 1400 Hrs_upgraded_profile0.csv",
    "CTD Bahia de tortel 17 de julio de 2024 1600_upgraded_profile0.csv",
    "CTD Bahia de Tortel 17 de Julio de 2024 1800 Hrs_upgraded_profile0.csv",
    "CTD Bahia de tortel 17 de Julio de 2024 2000 Hrs_upgraded_profile0.csv",
    "CTD Bahia de Tortel 17 de Julio de 2024 2200 Hrs_upgraded_profile0.csv",
    "CTD Bahia de Tortel 18 de julio de 2024 0000 hrs_upgraded_profile0.csv",
    "CTD Bahia de tortel 18 de julio de 2024 0200 Hrs_upgraded_profile0.csv",
    "CTD Bahia de tortel 18 de julio de 2024 0400 Hrs_upgraded_profile0.csv",
    "CTd Bahia de tortel 18 de Julio de 2024 0600 Hrs_upgraded_profile0.csv",
    "CTD Bahia de Tortel 18 de julio de 2024 0800 Hrs_upgraded_profile0.csv",
    "CTD Bahia de Tortel 18 de Julio de 2024 1000 Hrs_upgraded_profile0.csv",
    "Ctd Bahia de Tortel 18 de Julio de 2024 1200 Hrs_upgraded_profile0.csv"
]

title='17 y 18 de julio de 2024'
#%% 

datadir = "/home/rc/Documents/OneDrive-UdeC/TRABAJOS_INDEPENDIENTES/COPAS_Diego_Narváez/TORTEL_hr/Horarios_Abr2024_processed2025_down"

#Lista de archivos CSV
data_list=[
    "CTD Bahia de Tortel 19 de Abril  1200 Hrs de 2024_upgraded_profile0.csv", 
    "CTD Bahia de Tortel 19 de Abril 1600 Hrs_upgraded_profile0.csv",
    "CTD Bahia de tortel 19 de Abril 1800 Hrs_upgraded_profile0.csv",
  #  "CTD Bahia de Tortel 19 de abril 1400 Hrs_upgraded_profile0.csv",
    "CTD Bahia de Tortel 19 de Abril 2000 Hrs_upgraded_profile0.csv",
    "CTD Bahia de tortel 19 de Abril 2200 Hrs_upgraded_profile0.csv",
    "CTD Bahia de tortel 20 de Abril 0000 Hrs_upgraded_profile0.csv",
    "CTD Bahia de Tortel 20 de Abril 0200 Hrs_upgraded_profile0.csv",
    "CTD Bahia de Tortel 20 de Abril 0400 Hrs_upgraded_profile0.csv",
    "CTD BAhia de Tortel 20 de Abril 0600 Hrs_upgraded_profile0.csv",
    "CTD Bahia de Tortel 20 de Abril 0800 Hrs_upgraded_profile0.csv",
    "CTD bahia de Tortel 20 de Abril 1000 Hrs_upgraded_profile0.csv",
    "CTD BAhia de Tortel 20 de abril 1200 Hrs_upgraded_profile0.csv",
]

title='19 y 20 de abril 2024'
#%%

#Inicializa DataFrames vacíos
all_profiles_jnup = pd.DataFrame()
times_jnup = pd.DataFrame()
profundidad_jnup = pd.DataFrame()

#Itera sobre la lista de archivos
for archivo in data_list:
    ruta_archivo = os.path.join(datadir, archivo)
    
    # Lee el archivo CSV
    df = pd.read_csv(ruta_archivo,skiprows=25)
    
    # Selecciona columnas específicas (ajusta según sea necesario)
    p_jnup = df[[df.columns[8]]]
    t_jnup = (df[df.columns[0]])
    tt_jnup=([t_jnup.iloc[0]])
    tt_jnup = pd.Series(tt_jnup)
    tt_jnup = pd.to_datetime(tt_jnup,format='%Y-%m-%dT%H:%M:%S.%f')
    temp_jnup = df[[df.columns[2]]]
    temp_jnup = np.float64(temp_jnup)
    temp_jnup = pd.DataFrame(temp_jnup)
    
    # Concatena DataFrames
    all_profiles_jnup = pd.concat([all_profiles_jnup, temp_jnup], axis=1)
    times_jnup = pd.concat([times_jnup, tt_jnup], axis=1)
    profundidad_jnup = pd.concat([profundidad_jnup, p_jnup], axis=1)
    

# Ajustar el DataFrame final, asignando las profundidades como índice
all_profiles_jnup.index = profundidad_jnup.iloc[:, 0]  # Usamos la primera columna de profundidad como índice

# Transponer los tiempos para que coincidan con las columnas de los perfiles
times_jnup = times_jnup.T
times_jnup.columns = ['timestamp']

# Asignar los tiempos como nombres de las columnas de 'all_profiles'
all_profiles_jnup.columns = times_jnup['timestamp']

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

tiempos_jnup = pd.to_datetime(all_profiles_jnup.columns.values)  # Asegurarse que los tiempos son tipo datetime
tiempos_num_jnup = mdates.date2num(tiempos_jnup)  # Convertir las fechas a números flotantes
prof_jnup = all_profiles_jnup.index.values
T,P =  np.meshgrid(tiempos_jnup,prof_jnup)

fig,ax=plt.subplots()
cont=ax.contourf(T,P,all_profiles_jnup.values)
ax.set_ylabel('Profundidad [m]')
ax.set_xlabel('Perfil')
plt.title(title)

#ax.set_xlim(min(tiempos_jnup), max(tiempos_jnup))

# Personalización del eje X para mostrar dos niveles de etiquetas
ax.xaxis.set_major_locator(mdates.HourLocator(byhour=[0 ,15])) # Mostrar solo las 14:00 hrs como major ticks
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=3))


# Formato para las etiquetas de la hora (nivel inferior)
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))
ax.tick_params(which='minor', length=4, labelsize=8)  # Personalizamos las etiquetas menores

# Formato para las etiquetas de la fecha (nivel superior)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.tick_params(which='major', length=6, labelsize=10, pad=25)  # Etiquetas mayores más separadas

# Rotar solo los ticks que contienen las horas (los "minor ticks")
for label in ax.get_xticklabels(which='minor'):
    label.set_rotation(45)  # Rotar 45 grados solo las horas

fig.colorbar(cont,ax=ax)
plt.gca().invert_yaxis()
plt.savefig(datadir+title+'.png',
            dpi=300,
            bbox_inches='tight',     # Ajusta los márgenes automáticamente
            format='png',            # Especifica el formato
            transparent=False,       # Fondo transparente o no
            pad_inches=0.1)         # Padding adicional alrededor de la figura
plt.show()
