import os
import json

def load_persona(persona_path="data/persona.json"):
    with open(persona_path, "r") as f:
        return json.load(f)

def save_output(output_data, output_path="data/output.json"):
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)