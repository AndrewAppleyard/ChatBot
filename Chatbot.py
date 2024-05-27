import openai
import gradio

openai.api_key = "Enter your OpenAI key"

messages = [{"role": "system", "content": "You are a Robot"}]

def ChatBot(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatBotReply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatBotReply})
    return ChatBotReply

demo = gradio.Interface(fn=ChatBot, inputs = "text", outputs = "text", title = "OpenAI ChatBot")

demo.launch(share=True)