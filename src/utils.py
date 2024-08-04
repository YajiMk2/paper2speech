import json
import os
from datetime import datetime

def read_json(file_path):
    """
    JSONファイルを読み込み、Pythonの辞書形式で返す。
    
    :param file_path: 読み込むJSONファイルのパス
    :return: JSONデータを格納した辞書
    """
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_json(file_path, data):
    """
    辞書形式のデータをJSONファイルに書き込む。
    
    :param file_path: 書き込むJSONファイルのパス
    :param data: 書き込むデータ（辞書形式）
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def format_date(date_str):
    """
    日付文字列をYYYY-MM-DD形式に変換する。
    
    :param date_str: 変換する日付文字列
    :return: フォーマットされた日付文字列
    """
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        return date_str

def check_and_create_dir(directory):
    """
    指定されたディレクトリが存在しない場合は作成する。
    
    :param directory: チェックするディレクトリのパス
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def is_duplicate_entry(paper, records):
    """
    論文情報がすでにrecords.jsonに存在するかをチェックする。
    
    :param paper: チェックする論文情報（辞書形式）
    :param records: 既存の論文情報リスト
    :return: 重複している場合はTrue、それ以外はFalse
    """
    for record in records:
        if (paper['title'] == record['title'] and
                paper['publication_date'] == record['publication_date'] and
                set(paper['authors']) == set(record['authors'])):
            return True
    return False
