import streamlit

streamlit.title("My Mom's New Healthy Dinner")

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 and Blackberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlig.dataframe(my_fruit_list)
