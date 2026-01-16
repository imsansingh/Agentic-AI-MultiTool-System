import streamlit as st
import requests

st.title("Agentic AI System")

query = st.text_input("Enter your query")

if st.button("Run"):
    res = requests.post("http://localhost:8000/query", json={"query": query})
    st.write(res.json()["response"])
