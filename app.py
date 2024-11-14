import streamlit as st
from sklearn.datasets import load_iris

data = load_iris(as_frame=True)
df = data.frame

st.title("Example from AnyoneAI")
st.header("Hello, Juan Pablo Naranjo!")
st.subheader("This is a subheader")
st.write("This is just some basic text")

st.dataframe(df)