import os

# Absolute path to the root of the project
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# Folders
DATA_DIR = os.path.join(ROOT_DIR, "data")
OUTPUT_DIR = os.path.join(ROOT_DIR, "output")

# Files
RAW_MODELS_PATH = os.path.join(DATA_DIR, "all_models_raw.json")
FILTERED_MODELS_PATH = os.path.join(OUTPUT_DIR, "filtered_models.json")