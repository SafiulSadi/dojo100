# import google.generativeai as genai

# client = genai.Client(api_key="AIzaSyC4CITfd35eWv4HoDPnjJcsfFXBD6b1xzE")

# import google.generativeai as genai

# genai.configure(api_key="AIzaSyC4CITfd35eWv4HoDPnjJcsfFXBD6b1xzE")

# model = genai.GenerativeModel('gemini-pro')
# # response = model.generate_content("Tell me a joke about AI.")
# response = genai.list_models()
# for i in response():
#     print(i)
from google import genai
prompt = "Explain how robots works in a 50 words, response in json"

prompt = input("give a prompt: ")
client = genai.Client(api_key="AIzaSyC4CITfd35eWv4HoDPnjJcsfFXBD6b1xzE")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=prompt
)
print(response.text)

print(response.json())
x = "the idea is to learn prompt engineering"

print("hello, the idea is to use drone delivery and ai agent for education system")

print("this agent can read emotion and then give feedback ")
print("no progress has been made")