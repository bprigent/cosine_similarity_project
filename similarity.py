from sentence_transformers import SentenceTransformer, util
from typing import Dict, List, Tuple



class SimilarityEvaluator:
    """
    A class to encapsulate the logic for computing text similarity.
    """
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        """
        Initializes the evaluator with a pre-trained sentence transformer model.
        Args:
            model_name: The name of the pre-trained model to use (default is all-MiniLM-L6-v2)
        """
        # Initialize the sentence transformer model
        self.model = SentenceTransformer(model_name)

        

    def compute_cosine_similarity(self, text1: str, text2: str) -> float:
        """
        Computes the cosine similarity between the embeddings of two texts.
        
        Parameters:
            text1 (str): The first text.
            text2 (str): The second text.
            
        Returns:
            float: Cosine similarity score.
        """
        embeddings = self.model.encode([text1, text2])
        cosine_score = util.cos_sim(embeddings[0], embeddings[1])
        return cosine_score.item()
