"""
Модуль локализации интерфейса.

Обеспечивает поддержку нескольких языков интерфейса приложения:
переводит элементы управления, сообщения и системные уведомления.
"""

from typing import Dict


#: Словарь локализованных строк интерфейса
_translations: Dict[str, Dict[str, str]] = {
    "hello":         {"en": "Hello",     "ru": "Привет"},
    "translate_btn": {"en": "Translate", "ru": "Перевести"},
    "clear_btn":     {"en": "Clear",     "ru": "Очистить"},
    "history_title": {"en": "History",   "ru": "История"},
    "settings_title":{"en": "Settings",  "ru": "Настройки"},
}


def get_localized_text(key: str, language: str) -> str:
    """
    Получить локализованный элемент интерфейса по ключу и языку.

    Возвращает строку интерфейса на указанном языке.
    Если ключ или язык не найден — возвращает сам ключ
    в качестве запасного значения.

    :param key: Ключ строки интерфейса (например, ``"translate_btn"``).
    :type key: str
    :param language: Код языка интерфейса (``"en"`` или ``"ru"``).
    :type language: str
    :return: Локализованная строка или ``key`` при отсутствии перевода.
    :rtype: str

    Пример использования::

        >>> get_localized_text("translate_btn", "ru")
        'Перевести'
        >>> get_localized_text("translate_btn", "en")
        'Translate'
        >>> get_localized_text("unknown_key", "ru")
        'unknown_key'
    """
    return _translations.get(key, {}).get(language, key)


def get_supported_languages() -> list:
    """
    Получить список кодов поддерживаемых языков интерфейса.

    :return: Список строковых кодов языков (например, ``["en", "ru"]``).
    :rtype: list[str]
    """
    langs = set()
    for translations in _translations.values():
        langs.update(translations.keys())
    return sorted(langs)
