import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# make containers

header = st.container()
datasets = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("kashti ki app")
    st.text("In the project we will work on titanic data")

with datasets:
    st.header("Kashti doob gye.....shit")
    df = sns.load_dataset('titanic')
    df = df.dropna()

    st.write(df.head())

    st.subheader('Gender counts')
    st.bar_chart(df['sex'].value_counts())

    st.subheader('Class counts')
    st.bar_chart(df['class'].value_counts())

    st.subheader('count a/c to age')
    st.bar_chart(df['age'].sample(10))


with features:
    st.header("These are our app features")
    st.text('Our features are listed below:')

    st.markdown('1. **feature 1**: This is feature 1')
    st.markdown('2. **feature 2**: This is feature 2')

with model_training:
    st.header("Kashti walon ka kai bana? Model training")

    input, display = st.columns(2)

    max_depth = input.slider('How many people do you want?', min_value=10, max_value=100, value=20, step=5)

n_estimators = input.selectbox('How many tree should be there in a RF?', options=[50, 100, 200, 300, 'no limit'])

input.write(df.columns)

# input features from user
input_features = input.text_input('Which features we should use?')

# ML model
model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
if n_estimators == 'no limit':
    model = RandomForestRegressor(max_depth=max_depth, )
else:
    model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)



# define x and y (input )
X = df[[input_features]]
y = df[['fare']]

# fit our model
model.fit(X, y)
pred = model.predict(y)

# display metrices
display.subheader('Mean absolute error is: ')
display.write(mean_absolute_error(y, pred))
display.subheader('Mean squared error is: ')
display.write(mean_squared_error(y, pred))
display.subheader('R squared score error is: ')
display.write(r2_score(y, pred))