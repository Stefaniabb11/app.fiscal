import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 

data = pd.read_csv('munis.csv')

st.title("Primera aplicación ")

munis = data['entidad'].unique(). tolist() #guardamos en una lista las entidades unicas 

mun= st. selectbox("seleccione un municipio: ",
              munis)

filtro = data[data['entidad'] == mun] 

#aplica el filtro 

#st.dataframe(filtro) #dataframe original pero filtrado por municipio

gen = (filtro.groupby('clas_gen')['total_recaudo'].sum()) 
total_gen = gen.sum()

gen = (gen / total_gen).round(2) #proporciones para hacer el grafico de torta

det = (filtro.groupby('clasificacion_ofpuj')['total_recaudo'].sum())
total_det = det.sum()

det = (det/total_det).round(3) #proporciones para hacer el grafico de torta
#el codigo groupby separa las clasificaciones 

#st.dataframe(gen) #clasificacion general 
#st.dataframe(det) #clasificacion detallada 

#dataframe para mostrar el streamlit en internet.

#Transformamos a proporciones (grafico de torta)

fig, ax = plt.subplots(1, 1, figsize=(10, 6)) #fig(marco), axe(lienzo)
ax.pie(gen.values, labels=gen.index)

#st.pyplot(fig)

# Pie chart con plotly express

pie = px.pie(
    gen.reset_index(),
    names = "clas_gen",
    values = "total_recaudo",
    title = "Clacificación general por recaudo",)

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.pie(det.values, labels=det.index)

#st.pyplot(fig)

#treemap 
#creamos otro dataframe 

#gropuby agrupaaaaa
fin = (filtro.groupby(['clas_gen', 'clasificacion_ofpuj'])['total_recaudo'].sum().reset_index())
#st.dataframe(fin)

fig = px.treemap(fin, path = [px.Constant("Total"),'clas_gen' , 'clasificacion_ofpuj'], values= 'total_recaudo')
st.plotly_chart(fig)



# para abrir terminal control j
#control s para guardar 
# si nos paramos en la terminal y ponemos control c, se detiene la aplicaicon 

#para volver a activar la app (python -m streamlit run app.py) en la consola

#python -m pip install plotly, para instalar paquetes, usar en consola 
