import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # Importanto dataset

st.header('Análisis de carros')  # Encabezado

# Botones por casilla de verificación
build_histogram = st.checkbox('Construir histograma')
if build_histogram:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer', nbins=50,
                       title='Histograma de Precios')
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir gráfico de dispersión')
if build_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x='odometer', y='price',
                     title='Gráfico de Dispersión de Precios')
    st.plotly_chart(fig, use_container_width=True)
