import argparse
import csv

class Dictionary:
    """辞書クラス
    辞書ファイル(csv)の内容を読み込んで表示する
    """
    def __init__(self, dictfile):
        self.dictfile = dictfile # 辞書ファイル名
        self.word_info = [] # 単語情報(初期値空リスト)
    
    def load_word_info(self):
        """単語情報を読み込む
        """
        with open(self.dictfile, "r", encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            for word in csv_reader:
                self.word_info.extend(word)

    def show_word_info(self):
        """単語情報をコンソール画面に表示する
        """
        for word in self.word_info:
            print(word)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dictfile", default="dictionary-data.csv", help="読み込む辞書ファイル名")

    args = parser.parse_args()
    dictionary = Dictionary(args.dictfile)
    dictionary.load_word_info() # 単語情報読み込み
    dictionary.show_word_info() # 単語情報表示
