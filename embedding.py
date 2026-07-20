from sentence_transformers import SentenceTransformer
import numpy as np

from typing import List
class EmbeddingManager:
    """ handles document embedding generation using SentenceTransformer"""
    def __init__(self,model_name: str="all-MiniLM-L6-v2"):
        """
        Intialize the embedding manager
        Args:
        model_name= Huggingface model name for sentence embeddings
        """
        self.model_name=model_name
        self.model=None
        self._load_model()
    def _load_model(self):
        """
        load the sentencetransformer model
        """
        try:
            print(f"loading embedding model:{self.model_name}")
            self.model= SentenceTransformer(self.model_name)
            print(f"model loaded successfully. Embedding dimension: {self.model.get_sentence_embedding_dimension()}")
        except Exception as e:
            print(f"Error loading model {self.model_name}: {e}")
            raise
    def generate_embeddings(self, texts: List[str])-> np.ndarray:
        """
        Generate embeddings for a list of texts
        
        Args:
            texts: list of text strings to embed
        Returns:
            numpy array of embeddings with shape(len(texts),embedding_dim)
        """
        if not self.model:
            raise ValueError("Value not loaded")
        print(f"Generating embeddings for {len(texts)} texts...")
        embeddings = self.model.encode(texts, show_progress_bar=True)
        print(f"generated embeddings with shape: {embeddings.shape}")
        return embeddings



