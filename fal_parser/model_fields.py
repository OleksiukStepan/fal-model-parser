def enrich_base_fields(model):
    return {
        **model,
        "visible": True,
        "internal_name": model["id"],
        "settings": {},
        "generation_price_internal": {},
        "generation_price_user": {},
    }
