import gradio as gr

from openai import OpenAI

import os 

import json

from dotenv import load_dotenv

load_dotenv()

key = os.environ.get('OPENAI_API_KEY')

os.environ['OPENAI_API_KEY'] = key

client = OpenAI()

formatted_history = [
    {"role": "system", "content": "Eres un tutor que enseña con el método socrático. Debe guiar al estudiante hacia la respuesta y no dársela directamente."}
]

def generate_response(message, history):

    if history:
        for exchange in history:
            if len(exchange) == 2:
                user, assistant = exchange
                formatted_history.append({"role": "user", "content": user})
                formatted_history.append({"role": "assistant", "content": assistant})

    formatted_history.append({"role": "user", "content": message})
  
    response = client.chat.completions.create(
        model='ft:gpt-4o-mini-2024-07-18:personal::AWPw2HSW',
        messages=formatted_history,
        stream=True
    )

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
              partial_message = partial_message + chunk.choices[0].delta.content
              yield partial_message


with gr.Blocks() as demo:
    gr.ChatInterface(
        generate_response,
        type="messages",
        chatbot=gr.Chatbot(height=300, type="messages"),
        textbox=gr.Textbox(placeholder="Puedes preguntarme lo que quieras", container=False, scale=7),
        title="Edu AI")

demo.launch(share=True)
