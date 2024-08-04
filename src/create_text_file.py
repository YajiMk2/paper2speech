import os
from config import load_config
from utils import check_and_create_dir

config = load_config()

def create_text_file(title, abstract_jp, abstract_en):
    """
    論文のタイトルとAbstractを含むテキストファイルを生成する。
    
    :param title: 論文タイトル
    :param abstract_jp: 日本語のAbstract
    :param abstract_en: 英語のAbstract
    :return: テキストファイルのパス
    """
    # テキストファイルの保存ディレクトリを確認・作成
    check_and_create_dir(config['abstracts_dir'])

    # ファイル名を生成
    filename = f"{title.replace(' ', '_').replace('/', '_')}.txt"
    file_path = os.path.join(config['abstracts_dir'], filename)

    # テキストファイルの内容を生成
    content = f"タイトル: {title}\n\n日本語Abstract:\n{abstract_jp}\n\n英語Abstract:\n{abstract_en}"

    # テキストファイルに書き込み
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    return file_path

