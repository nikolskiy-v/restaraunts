import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

DB_PATH = BASE_DIR / "data" / "restaraunts.db" 
DB_PATH_V2 = BASE_DIR / "data" / "restaraunts_v2.db"
