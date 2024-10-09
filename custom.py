import transformers
import torch
from transformers import BitsAndBytesConfig
from transformers import AutoModelForCausalLM, AutoTokenizer
from deepeval.models import DeepEvalBaseLLM
import os
from groq import Groq
import os 
from dotenv import load_dotenv
load_dotenv()

# creating a class for custom model
class CustomB(DeepEvalBaseLLM):
    def __init__(self):
        self.client = Groq( api_key=os.environ.get(os.getenv("GROQ_API_KEY")))
        # self.client = Groq( api_key=os.getenv("GROQ_API_KEY"))
    

    def load_model(self):
        return self.client
        
        
    def generate(self, prompt: str) -> str:
        model = self.load_model()
        # chat_completion = self.client.chat.completions.create(messages=[{
        #     "role": "user",
        #     "content": prompt,
        # }],
        # model="llama3-8b-8192",
        # )

        # return chat_completion
        try:
            # Correctly handle the response from the chat completion API
            chat_completion = self.client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": prompt,
                }],
                model="llama3-8b-8192",
            )

            # Access the generated content (assuming it's in choices[0]['message']['content'])
            # return chat_completion.choices[0]['message']['content']
            # Access the generated content using attribute-style access
            completion_text = chat_completion.choices[0].message.content
            return completion_text

        except Exception as e:
            print(f"An error occurred during completion: {str(e)}")
            return ""

    async def a_generate(self, prompt: str) -> str:
        return self.generate(prompt)

    def get_model_name(self):
        return "Llama-3 8B"


# model=CustomB()
# print(model.generate("Hi"))




