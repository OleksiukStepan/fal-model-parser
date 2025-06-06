import json
import os

from config import RAW_MODELS_PATH, FILTERED_MODELS_PATH
from fal_parser.constants import TARGET_CATEGORIES
from fal_parser.model_fields import enrich_base_fields


def load_and_filter_models():
    if not os.path.exists(RAW_MODELS_PATH):
        raise FileNotFoundError(f"❌ File {RAW_MODELS_PATH} not found")

    with open(RAW_MODELS_PATH, "r", encoding="utf-8") as f:
        all_models = json.load(f)

    filtered_models = []
    for model in all_models:
        category = model.get("category", "").lower()
        if category in TARGET_CATEGORIES:
            enriched = enrich_base_fields(model)
            filtered_models.append(enriched)

    print(
        f"✅ Found {len(filtered_models)} models in categories {list(TARGET_CATEGORIES)}"
    )
    return filtered_models


def save_to_json(models):
    os.makedirs(os.path.dirname(FILTERED_MODELS_PATH), exist_ok=True)

    with open(FILTERED_MODELS_PATH, "w", encoding="utf-8") as f:
        json.dump(models, f, ensure_ascii=False, indent=2)

    print(f"📦 Save in {FILTERED_MODELS_PATH}")
