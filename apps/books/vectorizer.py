from sentence_transformers import SentenceTransformer
from pinecone.grpc import PineconeGRPC as Pinecone
from dotenv import load_dotenv
import os

load_dotenv()

class Vectorize:
    PINECONE_API_KEY = os.getenv('DATABASE_URL')
    INDEX_NAME = os.getenv('INDEX_NAME')

    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        self.pc = Pinecone(api_key=Vectorize.PINECONE_API_KEY)
        self.index = self.pc.Index(Vectorize.INDEX_NAME)

    def preprocess_text(self, text):
        text = text.lower()
        text = ''.join([c for c in text if c.isalnum() or c.isspace()])
        return text

    def generate_embeddings(self, text):
        embeddings = self.model.encode(text)
        return embeddings
    
    def search_similar_books(self, query_title, n):
        query_vector = self.generate_embeddings(query_title)
        result = self.index.query(
            # namespace="spotty_books",
            vector=query_vector,
            top_k=n,
            include_values=True
        )
        ids = [int(match['id']) for match in result['matches']]
        return ids
    