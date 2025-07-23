#REmove the IGNORE comments from the code
# Persona Extraction and Reading Path Generation System
from parser.section_extractor import extract_sections
from nlp.intent_model import build_persona_profile
from graph.graph_builder import build_concept_graph
from graph.pagerank_traversal import rank_nodes
from graph.reading_path_generator import generate_reading_path
from utils.io_utils import save_output
import config

def main():
    print("Extracting sections from PDFs...")
    sections = extract_sections(config.PDF_INPUT_DIR)
    if not sections:
        print("❌No sections extracted. Please check input PDFs.")
        return
    print("Parsing persona profile...")
    persona_profile = build_persona_profile(config.PERSONA_JSON_PATH)
    print("Building concept graph...")
    graph, section_map = build_concept_graph(sections, similarity_threshold=config.SIMILARITY_THRESHOLD)
    print("Running Personalized PageRank...")
    ranked_nodes = rank_nodes(graph, persona_profile)
    print("Generating reading path...")
    output_json = generate_reading_path(
        graph=graph,
        ranked_nodes=ranked_nodes,
        section_map=section_map,
        max_sections=config.MAX_READING_PATH_LENGTH,
        persona_profile=persona_profile
    )
    print(f"Saving output to {config.OUTPUT_JSON_PATH}...")
    save_output(output_json, config.OUTPUT_JSON_PATH)
    print("\n✅ Done! Output generated successfully.")

if __name__ == "__main__":
    main()