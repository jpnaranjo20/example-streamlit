import streamlit as st
from sklearn.datasets import load_iris, load_wine

data1 = load_iris(as_frame=True)
df1 = data1.frame

data2 = load_wine(as_frame=True)
df2 = data2.frame

st.title("Example from Streamlit")
st.header("Hello, Juan Pablo!")
st.subheader("This is a subheader")
st.write("This is just some basic text")

st.header("Example with Iris Dataset")
st.dataframe(df1)

st.header("Example with Wine Dataset")
st.dataframe(df2)