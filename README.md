# Fal.ai Model Filter & Enricher

This project processes generative AI model metadata from [Fal.ai](https://fal.ai).  
It filters raw model data by key generation categories and enriches each model with structured settings.

## Features

- Fetches public model data from Fal.ai API
- Filters by generation categories:
  - `image-to-image`
  - `image-to-video`
  - `text-to-image`
  - `text-to-video`
- Adds predefined settings for each model based on its category

## Project Structure

```text
fal_model_parser/
│
├── data/                     # Raw and processed JSON
├── output/                   # Final enriched models
├── fal_parser/               # Core logic modules
│   ├── loader.py
│   ├── model_enricher.py
│   ├── settings_templates.py
│   ├── constants.py
│   └── ...
├── main.py                   # Entry point for the enrichment pipeline
├── config.py                 # Path configuration
└── requirements.txt          # Dependencies
