"""
Глобальные переменные и константы.
"""

# стандартная библиотека
from re import compile
from pathlib import Path

PLAYERS_PATH = Path(r'..\data\players.ini')
SAVES_PATH = Path(r'..\data\saves.txt')
HELP_PATH = Path(r'..\data\rules_games.txt')

PROMPT = ' > '

MESSAGES = {
    'ввод команды': 'Введите команду',
    'ввод имени': 'Введите имя игрока',
    'некорректное имя': 'Имя игрока должно начинаться с буквы, содержать только буквы, цифры и символ подчёркивания',
    'правила игры': 'Показать правила игры? (Да/Нет)',
    'ввод размерности': 'введите новый размер поля',
    'некорректная размерность': 'размер поля должен находится в диапазоне от 3 до 20',
    # '': '',
}

COMMANDS = {
    'начать новую партию': ('new', 'n', 'начать', 'н'),
    'загрузить существующую партию': ('load', 'l', 'загрузка', 'з'),
    'отобразить раздел помощи': ('help', 'h', 'помощь', 'п'),
    'создать или переключиться на игрока': ('player', 'p', 'игрок', 'и'),
    'отобразить таблицу результатов': ('table', 't', 'таблица', 'т'),
    'изменить размер поля': ('dim', 'd', 'размер', 'р'),
    'выйти': ('quit', 'q', 'выход', 'в'),
}


NAME_PATTERN = compile(r'[A-Za-zА-ЯЁа-яё][A-Za-zА-ЯЁа-яё\d_]+')
DIM_PATTERN = compile(r'[3-9]|1[0-9]|20')


players_db: dict[str, dict[str, int]] = {}
saves_db: dict[tuple[str, str], dict] = {}


dim: int = 3
dim_range = range(dim)
all_cells: int = dim**2

# имя авторизованного игрока
authorized: str

TOKENS = ('X', 'O')
players: list[str] = []

turns: dict[int, str] = {}

field: str = ''