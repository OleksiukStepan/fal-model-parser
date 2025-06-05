IMAGE_TO_IMAGE_SETTINGS = {
    "seed": {"type": "fixed", "value": "random"},
    "guidance_scale": {"type": "slider", "min": 1, "max": 20, "step": 0.1, "default": 3.5},
    "sync_mode": {"type": "boolean", "default": False},
    "num_images": {"type": "slider", "min": 1, "max": 4, "default": 1},
    "safety_tolerance": {"type": "api_only", "options": ["Default"]},
    "output_format": {"type": "select", "options": ["JPEG", "PNG"], "default": "JPEG"},
    "aspect_ratio": {
        "type": "select",
        "options": ["21:9", "16:9", "4:3", "3:2", "1:1", "2:3", "3:4", "9:16", "9:21"],
        "default": "16:9"
    }
}

IMAGE_TO_VIDEO_SETTINGS = {
    "duration": {"type": "select", "options": [5, 10], "default": 5},
    "aspect_ratio": {"type": "select", "options": ["16:9", "9:16", "1:1"], "default": "16:9"},
    "negative_prompt": {"type": "textarea", "default": "blur, distort, and low quality"},
    "cfg_scale": {"type": "slider", "min": 0.0, "max": 1.0, "step": 0.1, "default": 0.5}
}

TEXT_TO_IMAGE_SETTINGS = {
    "negative_prompt": {"type": "textarea", "default": "blur, distort, and low quality"},
    "aspect_ratio": {"type": "select", "options": ["1:1", "16:9", "9:16", "3:4", "4:3"], "default": "1:1"},
    "num_images": {"type": "slider", "min": 1, "max": 4, "default": 1},
    "seed": {"type": "fixed", "value": "random"}
}

TEXT_TO_VIDEO_SETTINGS = {
    "duration": {"type": "select", "options": [5, 10], "default": 5},
    "aspect_ratio": {"type": "select", "options": ["16:9", "9:16", "1:1"], "default": "16:9"},
    "negative_prompt": {"type": "textarea", "default": "blur, distort, and low quality"},
    "cfg_scale": {"type": "slider", "min": 0.0, "max": 1.0, "step": 0.1, "default": 0.5}
}

CATEGORY_SETTINGS_MAP = {
    "image-to-image": IMAGE_TO_IMAGE_SETTINGS,
    "image-to-video": IMAGE_TO_VIDEO_SETTINGS,
    "text-to-image": TEXT_TO_IMAGE_SETTINGS,
    "text-to-video": TEXT_TO_VIDEO_SETTINGS
}
