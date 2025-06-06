import os
from config import RAW_MODELS_PATH, FILTERED_MODELS_PATH
from fal_parser.loader import load_and_filter_models, save_to_json
from fal_parser.model_enricher import enrich_models
from utils.download_models import download_models


def main():
    if not os.path.exists(RAW_MODELS_PATH):
        print("Model file not found. Download from API...")
        download_models()

    filtered = load_and_filter_models()
    enriched = enrich_models(filtered)
    save_to_json(enriched)

    print(f"✅ Saved {len(filtered)} models to {FILTERED_MODELS_PATH}")


if __name__ == "__main__":
    main()
