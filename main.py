import numpy as np
from data import get_text_pairs
from similarity import SimilarityEvaluator

def main():
    evaluator = SimilarityEvaluator()
    text_pairs = get_text_pairs()
    
    similarity_scores = []
    
    for category, ai_text, human_text in text_pairs:
        score = evaluator.compute_cosine_similarity(ai_text, human_text)
        similarity_scores.append((category,score))
        
        print("AI Text:     ", ai_text)
        print("Human Text:  ", human_text)
        print("Cosine Similarity: {:.4f}".format(score))
        print("-" * 50)
    
    # Calculate average of just the scores, not the (category, score) tuples
    average_similarity = np.mean([score for _, score in similarity_scores])
    
    average_similarity_by_category = {}

    for category, score in similarity_scores:
        if category not in average_similarity_by_category:
            average_similarity_by_category[category] = []
        average_similarity_by_category[category].append(score)
    for category, scores in average_similarity_by_category.items():
        average_similarity_by_category[category] = np.mean(scores)

    print("Average similarity score across all pairs: {:.4f}".format(average_similarity))
    print("Average similarity score by category:")
    for category, avg_score in average_similarity_by_category.items():
        print(f"{category}: {avg_score:.4f}")

if __name__ == "__main__":
    main()
