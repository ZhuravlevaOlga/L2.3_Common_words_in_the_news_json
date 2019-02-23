import collections
import json
import os

import chardet


def forming_list_files():  # формируем список файлов
    path = os.path.join(os.getcwd())  # находим путь где лежат файлы, они должны лежать в папке с программой
    list_files = []  # создаем пустой список файлов
    for root, dirs, files in os.walk(path):  # проходим по всем файлам по нашему пути
        for file in files:  # для каждого файла в файлах
            if '.json' in file:  # файл с форматом json
                list_files.append(file)  # добавляем в список файлов
    return list_files


def detects_encoding(file):  # ищем кодировку файла
    with open(file, 'rb') as text:
        encoding = chardet.detect(text.read())
        return encoding['encoding']


def find_common_word(encod):  # находит чаще употребляемые слова
    worde_list = []
    with open(file, encoding=encod) as f:
        file_json = json.load(f)
        for x in file_json['rss']['channel']['items']:
            for word in x['description'].split(' '):
                if len(word) >= 6:
                    worde_list.append(word)
        for common_words in collections.Counter(worde_list).most_common(10):
            print(common_words[0])


for file in forming_list_files():
    print('\n В файле {} чаще всего встречаются следующие слова:'.format(file))
    encod = detects_encoding(file)
    find_common_word(encod)
