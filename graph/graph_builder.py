import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_concept_graph(sections, similarity_threshold=0.2):
    """
    Constructs a graph where nodes are section IDs and edges are created based on TF-IDF similarity.
    """
    G = nx.Graph()
    section_texts = []
    section_ids = []
    for section in sections:
        section_id = section['section_id']
        G.add_node(section_id, **section)
        section_ids.append(section_id)
        section_texts.append(section['content'])
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(section_texts)
    sim_matrix = cosine_similarity(tfidf_matrix)
    n = len(section_ids)
    for i in range(n):
        for j in range(i + 1, n):
            sim = sim_matrix[i][j]
            if sim >= similarity_threshold:
                G.add_edge(section_ids[i], section_ids[j], weight=sim)

    return G, {s['section_id']: s for s in sections}