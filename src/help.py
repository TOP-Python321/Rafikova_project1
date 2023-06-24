"""
Раздел помощи.
"""

import data


def show_help() -> str:
    """Выводит на экран правила игры"""
    # ИСПРАВИТЬ: может, всё же прочитать файл один раз заранее, а не во время каждого вызова функции?)
    with open(data.HELP_PATH, 'r', encoding='utf-8') as file_in:
        text_file = file_in.read()
    # ИСПРАВИТЬ: и вывод, и возврат? я бы сказал: определитесь
    print(text_file)
    return text_file

