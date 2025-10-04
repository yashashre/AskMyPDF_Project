from mistralai import Mistral
from config import API_KEY, EMBED_MODEL

client = Mistral(api_key=API_KEY)

def get_embedding(text):
    """Generate embedding for a given text"""
    resp = client.embeddings.create(
        model=EMBED_MODEL,
        inputs=[text]  # Use 'input' as the keyword argument
    )
    return resp.data[0].embedding