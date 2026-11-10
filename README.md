# Panel de anuncios de venta de coches

Aplicación web hecha con Streamlit que permite explorar un conjunto de datos de anuncios de venta de coches (`vehicles_us.csv`).

## Aplicación desplegada

https://vehicles-project-dashboard.onrender.com

## Funcionalidad

- **Histograma:** al marcar la casilla "Construir un histograma", se muestra la distribución del odómetro (kilometraje) de los vehículos.
- **Gráfico de dispersión:** al marcar la casilla "Construir un gráfico de dispersión", se muestra la relación entre el odómetro y el precio.

Los gráficos son interactivos y se crean con Plotly Express.

## Estructura del proyecto

- `app.py`: aplicación de Streamlit
- `vehicles_us.csv`: conjunto de datos
- `notebooks/EDA.ipynb`: análisis exploratorio de datos
- `requirements.txt`: dependencias

## Cómo ejecutarla localmente

```
pip install -r requirements.txt
streamlit run app.py
```