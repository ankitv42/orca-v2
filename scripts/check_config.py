"""Sanity check that configuration loads. Run after any .env change."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from orca.config import get_settings


def main() -> None:
    s = get_settings()

    print("=== ORCA v2 config ===")
    print(f"llm_provider     : {s.llm_provider}")
    print(f"gemini_model     : {s.gemini_model or '(not set yet)'}")
    print(f"google_api_key   : {'set, ' + s.google_api_key[:6] + '...' if s.google_api_key else '(not set yet)'}")
    print(f"storage_backend  : {s.storage_backend}")
    print(f"sqlite_path      : {s.sqlite_path}")
    print(f"max_iterations   : {s.agent_max_iterations}")
    print("======================")


if __name__ == "__main__":
    main()