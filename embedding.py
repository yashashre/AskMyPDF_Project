# embedding.py

from sentence_transformers import SentenceTransformer
from config import EMBED_MODEL

# Initialize embedding model
embed_model = SentenceTransformer(EMBED_MODEL)

def get_embedding(text):
    """Generate embedding vector for given text"""
    return embed_model.encode(text).tolist()
