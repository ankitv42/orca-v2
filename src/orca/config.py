"""
Central configuration. Everything reads settings from here, never from
os.environ directly.

Why: in Week 4 we move from AI Studio to Vertex and SQLite to Firestore.
If config is scattered through the codebase, that migration touches
twenty files. Here, it touches one.
"""

from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # --- LLM ---
    llm_provider: Literal["gemini", "vertex"] = "gemini"
    google_api_key: str = ""
    gemini_model: str = ""

    # --- Storage ---
    storage_backend: Literal["sqlite", "firestore"] = "sqlite"
    sqlite_path: str = "data/orca.db"

    # --- GCP (week 4+) ---
    gcp_project_id: str = ""
    gcp_region: str = "asia-south1"

    # --- Observability ---
    langchain_tracing_v2: bool = False
    langchain_api_key: str = ""
    langchain_project: str = "orca-v2"

    # --- Agent ---
    agent_max_iterations: int = 8
    log_level: str = "INFO"


@lru_cache
def get_settings() -> Settings:
    """Cached so the .env file is parsed once per process."""
    return Settings()