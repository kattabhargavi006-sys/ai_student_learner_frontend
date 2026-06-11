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
    "https://ai-student-learner-backend.onrender.com/learn",
    data={"question": question},
    files=files
)

st.write("Status Code:", response.status_code)

if response.status_code == 200:
    result = response.json()

    st.subheader("Explanation")
    st.write(result["explanation"])

    st.subheader("Quiz")
    st.write(result["quiz"])
else:
    st.error(response.text)