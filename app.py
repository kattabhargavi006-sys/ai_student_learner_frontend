import streamlit as st
import requests

st.set_page_config(
    page_title="AI Student Learning Assistant",
    layout="wide"
)

st.title("AI Student Learning Assistant")

question = st.text_input(
    "Ask your question"
)

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if st.button("Generate"):

    files = {}

    if uploaded_file:

        files["file"] = (
            uploaded_file.name,
            uploaded_file,
            "application/pdf"
        )

    response = requests.post(
        "http://127.0.0.1:8000/learn",
        data={
            "question": question
        },
        files=files
    )

    result = response.json()

    st.subheader("Explanation")
    st.write(result["explanation"])

    st.subheader("Quiz")
    st.write(result["quiz"])