import json
from nlp.keyword_extractor import extract_keywords_from_text

def build_persona_profile(persona_json_path="data/persona.json"):
    with open(persona_json_path, "r") as f:
        persona_data = json.load(f)

    text_blob = persona_data.get("persona", "") + " " + persona_data.get("job_to_be_done", "")
    keywords = extract_keywords_from_text(text_blob)

    # Heuristic rules for depth/style (can be improved)
    depth = "deep" if any(word in text_blob.lower() for word in ["analyze", "methodology", "impact"]) else "shallow"
    style = "focused" if "goal" in text_blob.lower() or "target" in text_blob.lower() else "exploratory"

    return {
        "intent_keywords": keywords,
        "depth": depth,
        "style": style,
        "persona": persona_data.get("persona", ""),
        "job_to_be_done": persona_data.get("job_to_be_done", "")
    }