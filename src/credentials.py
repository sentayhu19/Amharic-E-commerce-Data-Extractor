"""Hard-coded Telegram API credentials for non-dotenv workflows.

WARNING: Embedding credentials directly in code is not recommended for open-source
projects. Replace the placeholder values below with your actual *public* API ID
and hash if you are certain they can be committed safely.
"""

API_ID: int | None = None  # e.g. 12345678
API_HASH: str | None = None  # e.g. "0123456789abcdef0123456789abcdef"
SESSION_NAME: str = "telegram_session"

if API_ID is None or API_HASH is None:
    raise RuntimeError(
        "Fill API_ID and API_HASH in src/credentials.py or switch back to the .env approach."
    )
