#Import the required Libraries

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="expanded", menu_items=None)

# Add a title and intro text
st.title('Ejemplo Grafica')
st.text('Esta pagina es el inicio de una linda historia para hacer')
st.text('analisis de sensibilidad de la demanda energética y generación de Colombia')

st.sidebar.title('Navegación')
# Create file uploader object
upload_file = st.sidebar.file_uploader('Adjunta un archivo csv que quieras plotear')


# Check to see if a file has been uploaded
if upload_file is not None:
    # If it has then do the following:

    # Read the file to a dataframe using pandas
    df = pd.read_csv(upload_file)

    # Create a section for the dataframe statistics
    st.header('Estadisticas del dataframe')
    st.write(df.describe())

    # Create a section for the dataframe header
    st.header('Cabecera del dataframe')
    st.write(df.head())

    # Create a section for matplotlib figure
    st.header('Gráfica')
    
    col1, col2 = st.columns(2)

    x_axis_val = col1.selectbox('Selecciona el eje X', options=df.columns)
    y_axis_val = col2.selectbox('Selecciona el eje Y', options=df.columns)

    
    plot = px.scatter(df, x=x_axis_val, y=y_axis_val)   
    st.plotly_chart(plot, use_container_width=True)
