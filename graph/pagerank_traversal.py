import networkx as nx

def rank_nodes(graph, persona_profile):
    """
    Runs Personalized PageRank with persona intent keywords as teleport vector.
    Returns a dict of section_id -> score.
    """
    teleport_vector = {}
    keywords = persona_profile['intent_keywords']
    for node, data in graph.nodes(data=True):
        content = data.get("content", "").lower()
        weight = sum(1 for kw in keywords if kw.lower() in content)
        if weight > 0:
            teleport_vector[node] = weight
    if not teleport_vector:
        teleport_vector = {node: 1.0 for node in graph.nodes}
    pr_scores = nx.pagerank(graph, personalization=teleport_vector, weight='weight')
    return pr_scores