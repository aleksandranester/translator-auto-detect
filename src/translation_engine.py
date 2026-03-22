"""
Модуль перевода текста.

Выполняет преобразование текста с исходного языка на целевой.
В реальной реализации подключается к внешнему API перевода.
"""


def translate_text(text: str, target_language: str) -> str:
    """
    Перевести текст на указанный целевой язык.

    Имитирует процесс перевода. В реальном проекте здесь
    выполняется подключение к API (например, Google Translate).
    Поддерживает корректную обработку специальных символов
    и знаков препинания.

    :param text: Исходный текст для перевода.
    :type text: str
    :param target_language: Код или название целевого языка (например, ``"ru"``, ``"en"``).
    :type target_language: str
    :return: Строка с результатом перевода.
    :rtype: str
    :raises ValueError: Если текст или целевой язык пустые.

    Пример использования::

        >>> translate_text("Hello world", "ru")
        '[Перевод на ru]: Hello world'
    """
    if not text:
        raise ValueError("Текст для перевода не может быть пустым.")
    if not target_language:
        raise ValueError("Целевой язык не указан.")
    return f"[Перевод на {target_language}]: {text}"
