import streamlit as st
from graph import graph

st.set_page_config(
    page_title="NewsBot",
    layout="wide"
)

st.title("NewsBot")
st.write("Ask news or general questions")

user_input = st.text_input("Ask something")

if st.button("Submit"):

    result = graph.invoke({
        "input": user_input,
        "decision": "",
        "output": "",
        "history": [],
        "sentiment": "",
        "fact_check": "",
        "error": ""
    })

    st.subheader("Response")
    st.write(result["output"])

    st.subheader("Analysis")
    st.write(f"Sentiment: {result['sentiment']}")
    st.write(f"Fact Check: {result['fact_check']}")

    if result["error"]:
        st.error(result["error"])
