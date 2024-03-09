import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a personal doctor that specalizes in diagnosing patients based on a number of symptoms and which treatment plan to  recommend"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Personal Doctor")

demo.launch(share=True)