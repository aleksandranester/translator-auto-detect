# Ветка system-modules: системные и вспомогательные модули

"""
Модуль локализации интерфейса
Обеспечивает поддержку нескольких языков интерфейса
"""

def get_localized_text(key, language):
    """
    Возвращает переведённый элемент интерфейса
    в зависимости от выбранного языка.
    """
    translations = {
        "hello": {"en": "Hello", "ru": "Привет"}
    }
    return translations.get(key, {}).get(language, key)
