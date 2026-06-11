from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

import tempfile

from pdf_reader import read_pdf
from search_tool import web_search
from agent import learning_agent
from quiz_generator import generate_quiz

app = FastAPI()

@app.get("/")
def home():

    return {
        "message":"Student Learning Assistant Running"
    }


@app.post("/learn")
async def learn(

    question: str = Form(...),

    file: UploadFile = File(None)

):

    pdf_text = ""

    if file:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp:

            temp.write(await file.read())

            pdf_text = read_pdf(temp.name)

    web_result = web_search(question)

    explanation = learning_agent(
        question,
        pdf_text,
        web_result
    )

    quiz = generate_quiz(question)

    return {
        "explanation": explanation,
        "quiz": quiz
    }