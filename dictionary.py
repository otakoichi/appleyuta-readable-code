import argparse
import csv

class Dictionary:
    """辞書クラス
    辞書ファイル(csv)の内容を読み込んで表示する
    """
    def __init__(self, dictfile):
        self.dictfile = dictfile # 辞書ファイル名
        self.word_info = dict() # 単語情報(初期値空の辞書)
    
    def load_word_info(self):
        """単語情報を読み込む
        """
        word_info_list = []
        with open(self.dictfile, "r", encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            for word in csv_reader:
                word_info_list.extend(word)

        # リストをID付きの辞書へ変換
        for i, word in enumerate(word_info_list):
                self.word_info[i] = word.strip()

    def show_word_info(self, show_id=None):
        """単語情報をコンソール画面に表示する
            show_idが指定された場合は該当IDの単語のみ表示する
        """
        if show_id is not None:
            if show_id in self.word_info:
                print(f'{show_id}: {self.word_info[show_id]}')    
            else:
                print('指定されたIDが存在しません。')
        else:
            for id, word in self.word_info.items():
                print(f'{id}: {word}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dictfile", default="dictionary-data.csv", help="読み込む辞書ファイル名")
    parser.add_argument("--showid", type=int, default=None, help="表示するid")

    args = parser.parse_args()
    dictionary = Dictionary(args.dictfile)
    dictionary.load_word_info() # 単語情報読み込み
    dictionary.show_word_info(args.showid) # 単語情報表示
