import openai
import gradio as gr
# your api key
openai.api_key = "Your_API_key"
# a function that out put the text from the chat gpt responce
def talk_with_bot(msg):
    compeletion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user","content":msg}]
    ) 
    # we used this because the complation return a dictionary data structure 
    return compeletion["choices"][0]["message"]["content"]

# a simple gui for the website
gui = gr.Interface(fn=talk_with_bot,inputs="text",outputs="text")

gui.launch() 
