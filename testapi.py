from fastapi import FastAPI
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key='###')

@app.post("/get_gpt_response/")
async def get_gpt_response(prompt: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return {"response": response.choices[0].message.content}
