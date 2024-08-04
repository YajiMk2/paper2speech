import openai
from config import load_config

config = load_config()

def translate_abstract(abstract, model='openai', api_key=None):
    """
    論文のAbstractを英語から日本語に翻訳する。
    
    :param abstract: 英語のAbstractテキスト
    :param model: 使用する翻訳モデル（'openai' または 'sentence_transformers'）
    :param api_key: OpenAI APIキー（モデルが'openai'の場合に必須）
    :return: 日本語に翻訳されたAbstract
    """
    if model == 'openai':
        return translate_with_openai(abstract, api_key)
    elif model == 'sentence_transformers':
        return translate_with_sentence_transformers(abstract)
    else:
        raise ValueError("Unknown translation model: {}".format(model))

def translate_with_openai(abstract, api_key):
    """
    OpenAI APIを使用してAbstractを翻訳する。
    
    :param abstract: 英語のAbstractテキスト
    :param api_key: OpenAI APIキー
    :return: 日本語に翻訳されたAbstract
    """
    openai.api_key = api_key
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Translate the following abstract to Japanese:\n\n{abstract}",
            max_tokens=1000,
            temperature=0.3,
        )
        translated_text = response.choices[0].text.strip()
        return translated_text
    except Exception as e:
        print(f"Error during OpenAI API call: {e}")
        return "翻訳エラー: OpenAI APIで問題が発生しました。"

def translate_with_sentence_transformers(abstract):
    """
    Sentence Transformersを使用してAbstractを翻訳する（ダミー実装）。
    
    :param abstract: 英語のAbstractテキスト
    :return: 日本語に翻訳されたAbstract（ダミー）
    """
    # ダミーの翻訳を返す
    return "これはダミーの翻訳です。実際のSentence Transformersモデルを実装してください。"
