from groq import Groq

client = Groq(api_key="your_groq_api_key_here")
print(client.models.list())  # Lists all models you can access
