from fal_parser.settings_template import CATEGORY_SETTINGS_MAP


def enrich_models(models: list[dict]) -> list[dict]:
    enriched = []
    for model in models:
        category = model.get("category", "").lower()

        # Add settings based on category
        model["settings"] = CATEGORY_SETTINGS_MAP.get(category, {})

        enriched.append(model)

    return enriched