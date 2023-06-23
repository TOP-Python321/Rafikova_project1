"""
Раздел помощи.
"""
import data


def show_help() -> str:
    """Выводит на экран правила игры"""
    with open(data.HELP_PATH, 'r', encoding='utf-8') as file_in:
        text_file = file_in.read()
    print(text_file)
    return text_file

