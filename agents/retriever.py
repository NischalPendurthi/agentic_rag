import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class Retriever:
    def __init__(self, index_path='faiss_index.bin', corpus_path='corpus.txt', model_name='all-MiniLM-L6-v2'):
        self.index = faiss.read_index(index_path)
        self.model = SentenceTransformer(model_name)
        with open(corpus_path, 'r') as f:
            self.corpus = [line.strip() for line in f.readlines()]

    def retrieve(self, query, k=5):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding), k)
        return [self.corpus[i] for i in indices[0]]