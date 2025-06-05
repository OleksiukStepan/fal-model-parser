import requests
import json
import os
from config import RAW_MODELS_PATH, DATA_DIR

URL = "https://fal.ai/api/models?tags=&type=&deprecated=false&pendingEnterprise=false&keywords=&sort=relevant"


def download_models():
    os.makedirs(DATA_DIR, exist_ok=True)

    print(f"🌐 Connecting to Fal.ai API...")
    response = requests.get(URL)
    response.raise_for_status()

    data = response.json()

    if isinstance(data, list):
        models = data
    elif isinstance(data, dict) and "models" in data:
        models = data["models"]
    else:
        raise ValueError("❌ Unexpected response format from API")

    if not models:
        raise ValueError("❌ Empty models list!")

    with open(RAW_MODELS_PATH, "w", encoding="utf-8") as f:
        json.dump(models, f, ensure_ascii=False, indent=2)

    print(f"✅ Downloaded {len(models)} models to {RAW_MODELS_PATH}")


if __name__ == "__main__":
    try:
        download_models()
    except Exception as e:
        print(f"❌ Error during download: {e}")
