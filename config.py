# config.py
import os
from typing import Dict, List, Optional
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class Configuration(BaseModel):
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    mistral_model: str = os.getenv("MISTRAL_MODEL", "mistral:latest")
    searxng_url: str = os.getenv("SEARXNG_URL", "http://localhost:8080")
    search_enabled: bool = os.getenv("SEARCH_ENABLED", "true").lower() == "true"
    max_search_results: int = int(os.getenv("MAX_SEARCH_RESULTS", "5"))
    content_max_tokens: int = int(os.getenv("CONTENT_MAX_TOKENS", "2000"))
    output_dir: str = os.getenv("OUTPUT_DIR", "learning_guides")

config = Configuration()