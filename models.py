import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY_HERE")  # Replace with your API key
for model in genai.list_models(): # loop to check all available models
    print(model.name) # Print all available models
