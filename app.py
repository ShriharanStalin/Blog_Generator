import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


genai.configure(api_key='AIzaSyB11UAjfWgJbkmmqiASugTwsWC0jtAFjOo')
print("---------------------------")
print("BLOG GENERATOR USING GAN")
print("---------------------------\n")
print("-----------------")
print("List of models ")
print("-----------------\n")

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)


model = genai.GenerativeModel('gemini-pro')


response = model.generate_content("Write a blog on food in India")


print("Response returned from genai:\n")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
print(response.text)
print("------------------------------------------------------------------------------------------------------------------------------------------------------")

"""
Store and print response
generated_text=response.text
print(generated_text)

"""
