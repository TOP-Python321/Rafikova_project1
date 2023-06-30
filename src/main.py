""" Точка входа: управляющий код """

import data
import game
import help
import player
import utils


# 1. Чтение файлов данных
text_rules = help.read_rules()
utils.show_title()

# 2. ЕСЛИ первый запуск, выводим правила игры:
if utils.read_players():
    print(text_rules)

# 3. Запрос имени игрока
player.get_player_name()

# суперцикл
while True:
    # 4. Ожидание ввода команды
    command = input(f'{data.MESSAGES["ввод команды"]}{data.PROMPT}')

    if command in data.COMMANDS['начать новую партию']:
        # 5. Запрос режима игры:
        ...
        # партия
        result = game.game()
        # 14. Обновление статистики в базе игроков и обновление файлов данных
        if result is not None:
            player.update_stats(result)

    elif command in data.COMMANDS['загрузить существующую партию']:
        # game.load()
        result = game.game()
        # 14. Обновление статистики в базе игроков и обновление файлов данных
        if result is not None:
            player.update_stats(result)
            ...

    elif command in data.COMMANDS['отобразить раздел помощи']:
        print(text_rules)

    elif command in data.COMMANDS['создать или переключиться на игрока']:
        ...

    elif command in data.COMMANDS['отобразить таблицу результатов']:
        ...

    elif command in data.COMMANDS['изменить размер поля']:
        utils.change_dim(utils.dim_input())

    elif command in data.COMMANDS['выйти']:
        break
    # если ввели некорректно команду, выводим "Команды игры"
    else:
        help.show_commands()

    # 15. Переход к этапу 4


# 16. Обработка завершения работы приложения
