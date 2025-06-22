# Amharic E-commerce Data Extractor
This project ingests raw messages from Ethiopian Telegram e-commerce channels, cleans & normalises Amharic text, and structures the output so that downstream models (e.g. entity-extractors or LLM fine-tuning pipelines) can discover seller insights.

```text
├── fetch/              # CLI entry-points & quick scripts
├── src/                # Importable Python modules
│   ├── ingestion/      # Telegram fetching logic
│   ├── utils/          # Shared helpers (text prep, IO)
│   └── config.py       # Paths & environment variables
├── notebooks/          # Exploratory notebooks
├── data/
│   ├── raw/            # Appended JSONL straight from Telegram
│   └── processed/      # Tokenised / cleaned records
├── requirements.txt
└── .env.example        # Fill with your Telegram API creds
```

## Quick start
1. Install deps
```bash
pip install -r requirements.txt
```
2. Copy `.env.example` → `.env` and fill `TELEGRAM_API_ID` & `TELEGRAM_API_HASH` (grab from [my.telegram.org](https://my.telegram.org)).
3. Run the ingestor with at least five channel handles:
```bash
python fetch/run_ingestion.py channel1 channel2 channel3 channel4 channel5
```
Messages are appended to `data/raw/<channel>.jsonl` as they arrive.

Feel free to share the collected JSONL files amongst the team—more data means better fine-tuning.
