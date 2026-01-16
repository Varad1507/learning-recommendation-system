from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("backend/rag/topic_knowledge.txt", "r", encoding="utf-8") as f:
    documents = f.read().split("\n\n")

doc_embeddings = model.encode(documents)
dimension = doc_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))

def generate_explanation(topic, learner_type):
    query = f"Explain {topic} for a {learner_type} learner"
    query_embedding = model.encode([query])

    _, idx = index.search(np.array(query_embedding), k=1)
    explanation = documents[idx[0][0]]

    return explanation.strip()
