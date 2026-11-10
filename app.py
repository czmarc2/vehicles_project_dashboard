import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Panel de anuncios de venta de coches')

build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Histograma de la columna odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, width='stretch')

build_scatter = st.checkbox('Construir un gráfico de dispersión')
if build_scatter:
    st.write('Precio vs. odómetro')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, width='stretch')