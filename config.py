import os

# Абсолютний шлях до кореня проєкту
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# Папки
DATA_DIR = os.path.join(ROOT_DIR, "data")
OUTPUT_DIR = os.path.join(ROOT_DIR, "output")

# Файли
RAW_MODELS_PATH = os.path.join(DATA_DIR, "all_models_raw.json")
FILTERED_MODELS_PATH = os.path.join(OUTPUT_DIR, "filtered_models.json")