from pydoc import describe
from turtle import width
import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Plotly with streamlit")
st.header('Gapminder dataset')
df = px.data.gapminder()


st.write(df)

# prints list of columns in dataframe
st.subheader('List of all columns in dataframes')
st.write(df.columns)

# prints summary of stats
st.subheader('Dataframe stats summary')
st.write(df.describe())

# data management
year_option = df['year'].unique().tolist()

year = st.selectbox('which year should we plot?', year_option, 0)

# df = df[df['year'] == year]

#plotting
fig = px.scatter(df, x='gdpPercap', y='lifeExp', size='pop', color='continent', hovecr_name='continent', log_x=True, size_max=55, range_x=[100, 100000], range_y=[20,90], animation_frame='year', animation_group='country')

#fig.update_layout(width=1000)
st.write(fig)