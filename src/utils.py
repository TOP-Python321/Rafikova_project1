"""
Вспомогательные функции.
"""

from configparser import ConfigParser
import data
def read_players() -> bool:
    """Читает файл данных игроков, сохраняет информацию в соответствующую глобальную структуру данных. Возвращает True, если в файле данных игроков есть хотя бы одна запись, иначе False."""
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

