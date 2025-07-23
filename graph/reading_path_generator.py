def generate_reading_path(graph, ranked_nodes, section_map, max_sections=10, persona_profile=None):
    """
    Generates a human-like reading path based on graph structure and PageRank scores.
    Returns JSON-style structured output.
    """
    sorted_sections = sorted(ranked_nodes.items(), key=lambda x: x[1], reverse=True)
    visited = set()
    path = []
    sub_section_analysis = []
    style = persona_profile.get("style", "focused") if persona_profile else "focused"
    for rank, (section_id, score) in enumerate(sorted_sections):
        if section_id in visited:
            continue
        section = section_map[section_id]
        visited.add(section_id)
        refined_text = section['content'].split(". ")
        refined_text = ". ".join(refined_text[:2]) + "."
        path.append({
            "document": section['doc_id'],
            "section_title": section['title'],
            "page_number": section['page_number'],
            "importance_rank": rank + 1
        })
        sub_section_analysis.append({
            "document": section['doc_id'],
            "page_number": section['page_number'],
            "refined_text": refined_text
        })
        if len(path) >= max_sections:
            break

    return {
        "metadata": {
            "persona": persona_profile.get("persona", ""),
            "job_to_be_done": persona_profile.get("job_to_be_done", ""),
        },
        "extracted_sections": path,
        "sub_section_analysis": sub_section_analysis
    }