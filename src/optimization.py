"""
Модуль оптимизации производительности.

Повышает скорость обработки переводов за счёт кэширования
часто используемых результатов и снижения нагрузки на API.
"""

from typing import Dict, Optional


#: Внутреннее хранилище кэша переводов
_cache: Dict[str, str] = {}


def cache_translation(text: str, translated: str) -> None:
    """
    Сохранить результат перевода в кэш.

    Добавляет пару «исходный текст — перевод» в словарь кэша.
    При повторном запросе система возвращает кэшированный результат,
    не обращаясь к внешнему API.

    :param text: Исходный текст, используемый как ключ кэша.
    :type text: str
    :param translated: Переведённый текст для сохранения.
    :type translated: str
    :return: None

    Пример использования::

        >>> cache_translation("Hello", "Привет")
        Перевод сохранён в кэше
    """
    _cache[text] = translated
    print("Перевод сохранён в кэше")


def get_cached_translation(text: str) -> Optional[str]:
    """
    Получить кэшированный перевод по исходному тексту.

    :param text: Исходный текст для поиска в кэше.
    :type text: str
    :return: Кэшированный перевод или ``None``, если запись отсутствует.
    :rtype: str or None

    Пример использования::

        >>> cache_translation("Hello", "Привет")
        Перевод сохранён в кэше
        >>> get_cached_translation("Hello")
        'Привет'
    """
    return _cache.get(text)


def clear_cache() -> None:
    """
    Полностью очистить кэш переводов.

    :return: None
    """
    _cache.clear()
