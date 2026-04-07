from __future__ import annotations

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
ORDERS_DIR = DATA_DIR / "orders"
PROJECTS_DIR = DATA_DIR / "projects"
ASSETS_DIR = DATA_DIR / "assets"
OUTPUTS_DIR = DATA_DIR / "outputs"

DEFAULT_VIDEO_WIDTH = 1080
DEFAULT_VIDEO_HEIGHT = 1920
DEFAULT_FPS = 24
DEFAULT_VOICE_SPEED = 1.0
MAX_SHOTS_V1 = 8
MIN_DURATION_V1 = 15
MAX_DURATION_V1 = 30

APP_USE_MOCK_LLM = os.getenv("APP_USE_MOCK_LLM", "true").lower() == "true"
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "").rstrip("/")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

for _dir in [DATA_DIR, ORDERS_DIR, PROJECTS_DIR, ASSETS_DIR, OUTPUTS_DIR]:
    _dir.mkdir(parents=True, exist_ok=True)
