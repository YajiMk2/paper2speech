import os
import openai
from config import load_config
from utils import check_and_create_dir

config = load_config()

def create_audio_file(text, title, model='openai', api_key=None):
    """
    テキストから音声ファイルを生成する。
    
    :param text: 音声に変換するテキスト
    :param title: 論文タイトル（ファイル名に使用）
    :param model: 使用する音声変換モデル（'openai' または 'sentence_transformers'）
    :param api_key: OpenAI APIキー（モデルが'openai'の場合に必須）
    :return: 音声ファイルのパス
    """
    if model == 'openai':
        return create_audio_with_openai(text, title, api_key)
    elif model == 'sentence_transformers':
        return create_audio_with_sentence_transformers(text, title)
    else:
        raise ValueError("Unknown speech conversion model: {}".format(model))

def create_audio_with_openai(text, title, api_key):
    """
    OpenAI APIを使用してテキストを音声に変換する。
    
    :param text: 音声に変換するテキスト
    :param title: 論文タイトル（ファイル名に使用）
    :param api_key: OpenAI APIキー
    :return: 音声ファイルのパス
    """
    openai.api_key = api_key

    # 音声ファイルの保存ディレクトリを確認・作成
    check_and_create_dir(config['audio_dir'])

    # ファイル名を生成
    filename = f"{title.replace(' ', '_').replace('/', '_')}.mp3"
    file_path = os.path.join(config['audio_dir'], filename)

    try:
        # OpenAIの音声合成API（仮のエンドポイントと設定）
        response = openai.Audio.create(
            engine="davinci",  # 仮のエンジン名。実際には適切なエンジンを指定
            prompt=text,
            format="mp3",
            max_tokens=1000,
            temperature=0.5
        )
        with open(file_path, 'wb') as audio_file:
            audio_file.write(response['data'])

        print(f"音声ファイルが生成されました: {file_path}")
        return file_path

    except Exception as e:
        print(f"Error during OpenAI API call: {e}")
        return None

def create_audio_with_sentence_transformers(text, title):
    """
    Sentence Transformersを使用してテキストを音声に変換する（ダミー実装）。
    
    :param text: 音声に変換するテキスト
    :param title: 論文タイトル（ファイル名に使用）
    :return: 音声ファイルのパス（ダミー）
    """
    # ダミーの音声ファイル生成を実装
    filename = f"{title.replace(' ', '_').replace('/', '_')}_dummy.mp3"
    file_path = os.path.join(config['audio_dir'], filename)
    print(f"ダミー音声ファイルが生成されました: {file_path}")
    return file_path
