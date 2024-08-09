import google.generativeai as genai
API_KEY = "AIzaSyALQx-26oVWs-Yng9FJ1E3awuTOXVUKOOg"
genai.configure(api_key=API_KEY)

# Initialize the model

model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

user_input = input("Enter your Prompt = ")
output = getResponseFromModel(user_input)
print(output)

