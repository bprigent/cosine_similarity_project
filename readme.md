# Text Similarity Evaluation Project

This project demonstrates how to quantitatively assess the semantic similarity between AI-generated text and human-generated (reference) text using a pre-trained Sentence Transformer model. It evaluates similarity by computing the cosine similarity between text embeddings.

## Project Structure

- `data.py`: Contains a function to generate a list of text pairs for evaluation.
- `similarity.py`: Defines the `SimilarityEvaluator` class, which includes methods for computing cosine similarity between text embeddings.
- `main.py`: The main script that loads the data, computes similarity scores, and prints the results.

## Usage

1. Run `main.py` to see the similarity scores for each pair of texts.
2. The script will print the AI-generated text, human-generated text, and the computed cosine similarity score for each pair.
3. It will also print the average similarity score across all pairs.

This project provides a basic framework for evaluating text similarity, which can be extended or customized for more complex scenarios.

## Why is cosine similarity the right method to use for text meaning similarity?

In LLMs, words are turned into tokens with are then turned into embeddings. Embeddings are vectors that represent the meaning of the text. if two embeddings are close to each other in degrees, the corresponding texts are similar. This means, modern NLP models (e.g., word2vec, GloVe, BERT, GPT, etc.) map words or sentences into high-dimensional embeddings where semantically similar texts tend to occupy nearby directions in vector space.

Cosine similarity measures the cosine of the angle between two vectors in an n-dimensional space. The result ranges from −1 (exactly opposite) to 1 (exactly the same). In most text embedding scenarios, the values usually fall between 0 and 1 since embeddings typically do not point in opposite directions. Therefore, Cosine similarity measures how similar two documents are by counting the number of words in common, weighted by the frequency of the words in the documents.

## Which library to use for text similarity?

Here are the options for text cosine similarity libraries:

- [Sentence Transformers](https://www.sbert.net/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [spaCy](https://spacy.io/)
- [NLTK](https://www.nltk.org/)
- [Gensim](https://radimrehurek.com/gensim/)
