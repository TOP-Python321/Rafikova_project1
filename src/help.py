"""
Раздел помощи.
"""
import data

def read_rules() -> str:
    """Чтение файла Правила игры"""
    # ИСПРАВИТЬ: может, всё же прочитать файл один раз заранее, а не во время каждого вызова функции?)
    with open(data.HELP_PATH, 'r', encoding='utf-8') as file_in:
        text_file = file_in.read()
    # ИСПРАВИТЬ: и вывод, и возврат? я бы сказал: определитесь
    return text_file


def show_commands() -> None:
    """Выводит на экран команды игры"""
    print(*(f'{k!r}: {v}' for k, v in data.COMMANDS.items()), sep=',\n')


