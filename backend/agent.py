import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def learning_agent(
        question,
        pdf_content,
        web_content
):

    prompt = f"""
    You are an AI Student Learning Assistant.

    Student Question:
    {question}

    PDF Content:
    {pdf_content[:5000]}

    Web Content:
    {web_content}

    Explain clearly.

    Also provide:

    1. Explanation
    2. Key Notes
    3. Summary
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content