from mistralai import Mistral
from config import API_KEY, CHAT_MODEL
from vectordb import retrieve_context

client = Mistral(api_key=API_KEY)

def ask_rag(question):
    """Perform RAG: retrieve relevant chunks, then ask Mistral"""
    context_chunks = retrieve_context(question)
    context = "\n\n".join(context_chunks)

    response = client.chat.complete(
        model=CHAT_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers using the provided context."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
        ]
    )
    return response.choices[0].message.content