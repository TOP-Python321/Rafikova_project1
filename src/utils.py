"""
Вспомогательные функции.
"""

from configparser import ConfigParser
from shutil import get_terminal_size

import data
import main


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
    config.read_dict(data.players_db)
    # КОММЕНТАРИЙ: а ещё у объектов типа ConfigParser есть метод read_dict()
    # for player_name in data.players_db:
    # config[player_name] = {key: value for key, value in data.players_db.items()}
    with open(data.PLAYERS_PATH, "w", encoding="utf-8") as file_out:
        config.write(file_out)

    return None


def show_title() -> None:
    """Выводит на экран заголовок игры при запуске программы"""
    width = get_terminal_size().columns - 1
    line1 = f"{'#' * width}"
    line2 = f"\n#{' ' * (width-2)}#\n"
    text_line = f"#{'Игра КРЕСТИКИ_НОЛИКИ'.center(width - 2)}#"
    print(line1+line2+text_line+line2+line1)
    # ИСПРАВИТЬ: это больше похоже на логику макро-уровня — вызов question_show_help() стоит вынести из данной функции, и использовать независимо (хотя бы потому, что вы можете захотеть добавить условия к этому вызову)
    # УДАЛИТЬ: избыточная строчка кода — если явный возврат отсутствует, то функция неявно вернёт None



def question_show_help() -> None:
    """Запрашивает у пользователя показать ли правила игры"""
    # ИСПРАВИТЬ: такие сообщения и подсказки для ввода нужно прописывать в data.MESSAGES (а на самом деле не прописывать литералами, а тоже считывать из файлов данных — но это в будущем, а пока хотя бы литералами прописать в одном модуле, откуда потом считывать)
    answer = input(f'{data.MESSAGES["правила игры"]}{data.PROMPT}').lower()
    # ИСПРАВИТЬ: а строковые методы конвертации регистра буквенных символов разве отменили?)
    if answer == 'да' or answer == 'yes':
        print(main.text_rules)


def field_template(dim: int) -> str:
    """Принимает размерность игрового поля и возвращает строку шаблона игрового поля:"""
    # ИСПРАВИТЬ: dim*3 + (dim-1) => dim*4 - 1
    width = dim * 4 - 1
    h_line, v_line = '–', '|'
    h_line = f'\n{h_line * width}\n'
    v_line = v_line.join(' {} ' for _ in range(dim))
    return h_line.join(v_line for _ in range(dim))
        # ИСПРАВИТЬ: эту строку тоже можно сгенерировать один раз заранее


def winning_combinations(dim: int) -> tuple[set]:
    """Генерирует и возвращает кортеж выигрышных комбинаций"""
    result = ()
    # горизонтали
    for i in range(0, dim**2, dim):
        result += (set(range(i, i+dim)), )
    # вертикали
    for i in range(0, dim):
        result += (set(range(i, dim**2, dim)), )
    # диагонали
    result += (set(range(0, dim**2 + 1, dim+1)), )
    result += (set(range(dim-1, dim**2-1, dim - 1)),)
    return result


