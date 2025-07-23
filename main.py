from parser.section_extractor import extract_sections
from nlp.intent_model import build_persona_profile
from graph.graph_builder import build_concept_graph
from graph.pagerank_traversal import rank_nodes
from graph.reading_path_generator import generate_reading_path
from utils.io_utils import save_output
import config

def main():
    print("🧠 Round 1B: Persona-Driven Document Intelligence System\n")

    # Step 1: Extract structured sections from input PDFs
    print("🔍 Extracting sections from PDFs...")
    sections = extract_sections(config.PDF_INPUT_DIR)

    if not sections:
        print("❌ No sections extracted. Please check input PDFs.")
        return

    # Step 2: Build the persona cognitive profile
    print("🧑‍💼 Parsing persona profile...")
    persona_profile = build_persona_profile(config.PERSONA_JSON_PATH)

    # Step 3: Build concept graph with similarity links
    print("🔗 Building concept graph...")
    graph, section_map = build_concept_graph(sections, similarity_threshold=config.SIMILARITY_THRESHOLD)

    # Step 4: Run Personalized PageRank using persona intent
    print("📊 Running Personalized PageRank...")
    ranked_nodes = rank_nodes(graph, persona_profile)

    # Step 5: Generate the dynamic reading path
    print("📚 Generating reading path...")
    output_json = generate_reading_path(
        graph=graph,
        ranked_nodes=ranked_nodes,
        section_map=section_map,
        max_sections=config.MAX_READING_PATH_LENGTH,
        persona_profile=persona_profile
    )

    # Step 6: Save the output
    print(f"💾 Saving output to {config.OUTPUT_JSON_PATH}...")
    save_output(output_json, config.OUTPUT_JSON_PATH)

    print("\n✅ Done! Output generated successfully.")

if __name__ == "__main__":
    main()