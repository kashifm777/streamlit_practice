import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.title('Iris Dataset')
st.header('We call it phool')
st.text('this is phool data, aka Iris')

phool = sns.load_dataset('iris')
phool

st.header('Bar chart for Iris')
st.text('Iris barchart for sepal length')
st.bar_chart(phool[['sepal_length', 'sepal_width']])

st.header('Line Chart')
st.text('petal length vs sepal length (Iris)')
st.line_chart(phool[['petal_length', 'sepal_length']])

