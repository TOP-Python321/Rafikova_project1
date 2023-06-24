"""
Вспомогательные функции.
"""

from configparser import ConfigParser
from shutil import get_terminal_size

import data
import help


def read_players() -> bool:
    """
    Читает файл данных игроков, сохраняет информацию в соответствующую глобальную структуру данных. Возвращает True, если в файле данных игроков есть хотя бы одна запись, иначе False.
    """
    config = ConfigParser()
    config.read(data.PLAYERS_PATH)
    config = {
        player_name: {
            key: int(value)
            for key, value in config[player_name].items()
        }
        for player_name in config.sections()
    }
    data.players_db = config
    return bool(config)


def write_players() -> None:
    """Записывает в файл данных игроков информацию из соответствующей глобальной структуры данных."""
    config = ConfigParser()

    # КОММЕНТАРИЙ: а ещё у объектов типа ConfigParser есть метод read_dict()
    for player_name in data.players_db:
        config[player_name] = {key: value for key, value in data.players_db.items()}

    with open(data.PLAYERS_PATH, "w", encoding="utf-8") as file_out:
        config.write(file_out)

    return None


def show_title() -> None:
    """Выводит на экран заголовок игры при запуске программы"""
    width = get_terminal_size().columns - 1
    line1 = f'{"#" * width}'
    line2 = f"\n#{' ' * (width-2)}#\n"
    text_line = f'#{"Игра КРЕСТИКИ_НОЛИКИ".center(width-2)}#'
    print(line1+line2+text_line+line2+line1)
    question_show_help()
    return None


def question_show_help() -> None:
    """Запрашивает у пользователя показать ли правила игры"""
    answer = input('Показать правила игры? (Да/Нет) > ')
    if answer == 'Да' or answer == 'да':
        help.show_help()


def field_template(dim: int) -> str:
    """Принимает размерность игрового поля и возвращает строку шаблона игрового поля:"""
    # ИСПРАВИТЬ: dim*3 + (dim-1) => dim*4 - 1
    width = dim * 4 + 1
    h_line, v_line = '–', '|'
    h_line = f'\n{h_line * width}\n'
    return h_line.join(
        # ИСПРАВИТЬ: эту строку тоже можно сгенерировать один раз заранее
        v_line.join(' {} ' for _ in range(dim))
        for _ in range(dim)
    )

# >>> print(field_template(3).format(*['X']*9))
#  X | X | X
# –––––––––––––
#  X | X | X
# –––––––––––––
#  X | X | X

