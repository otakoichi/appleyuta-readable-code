# 辞書ファイル
DICT_FILE = "dictionary-data.txt"

# 辞書ファイルから単語情報を取得
with open(DICT_FILE, "r" ,encoding="utf-8") as f:
    word_info = f.read()

# 単語情報をコンソール画面に出力する
print(word_info)
