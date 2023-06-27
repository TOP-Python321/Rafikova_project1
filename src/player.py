"""
Работа с данными игроков.
"""
import data

def name_input() -> str:
    while True:
        name = input(f' {data.MESSAGES["ввод имени"]}{data.PROMPT}')
        if data.NAME_PATTERN.fullmatch(name):
            return name
        print(f' {data.MESSAGES["некорректное имя"]} ')
