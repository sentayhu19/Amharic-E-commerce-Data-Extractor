"""Project-wide configuration utilities.

Loads environment variables and defines constants used across modules.
"""
from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Ensure directories exist
for _dir in (DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR):
    _dir.mkdir(parents=True, exist_ok=True)

# Telegram API credentials (expected to be set in environment)
API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")
SESSION_NAME = os.getenv("TELEGRAM_SESSION", "telegram_session")

if not (API_ID and API_HASH):
    # Fallback to credentials.py (non-secure public credentials)
    try:
        from src.credentials import API_ID as CRED_ID, API_HASH as CRED_HASH, SESSION_NAME as CRED_SESSION_NAME  # noqa: E402
    except ImportError:
        CRED_ID = CRED_HASH = CRED_SESSION_NAME = None

    if CRED_ID and CRED_HASH:
        API_ID = CRED_ID
        API_HASH = CRED_HASH
        SESSION_NAME = CRED_SESSION_NAME
    else:
        raise EnvironmentError(
            "Telegram API credentials missing. Set env vars, provide a .env, or fill src/credentials.py."
        )
