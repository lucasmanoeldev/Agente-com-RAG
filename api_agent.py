"""Entrada compatível para a API; implementação em backend/api_agent.py."""

import runpy
from pathlib import Path

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().parent / "backend" / "api_agent.py"), run_name="__main__")
else:
    from backend.api_agent import app
