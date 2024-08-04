import os

# OpenAI APIキー
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-default-api-key")

# デフォルトの翻訳モデル
DEFAULT_TRANSLATION_MODEL = "openai"  # 'openai' または 'sentence_transformers'

# モデル関連設定
SENTENCE_TRANSFORMERS_MODEL_PATH = os.getenv("SENTENCE_TRANSFORMERS_MODEL_PATH", "./models/translation/sentence_transformers_model")

# arXiv API設定
ARXIV_MAX_RESULTS = 10

# ファイルパス設定
AUDIO_DIR = "./data/audio/"
ABSTRACTS_DIR = "./data/abstracts/"
RECORDS_FILE = "./data/records.json"

def load_config():
    """
    環境変数から設定を読み込み、設定値を取得するヘルパー関数。
    """
    config = {
        "openai_api_key": os.getenv("OPENAI_API_KEY", OPENAI_API_KEY),
        "default_translation_model": os.getenv("DEFAULT_TRANSLATION_MODEL", DEFAULT_TRANSLATION_MODEL),
        "sentence_transformers_model_path": os.getenv("SENTENCE_TRANSFORMERS_MODEL_PATH", SENTENCE_TRANSFORMERS_MODEL_PATH),
        "arxiv_max_results": int(os.getenv("ARXIV_MAX_RESULTS", ARXIV_MAX_RESULTS)),
        "audio_dir": os.getenv("AUDIO_DIR", AUDIO_DIR),
        "abstracts_dir": os.getenv("ABSTRACTS_DIR", ABSTRACTS_DIR),
        "records_file": os.getenv("RECORDS_FILE", RECORDS_FILE)
    }
    return config
