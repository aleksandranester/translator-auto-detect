"""
Главный модуль проекта.

Интеллектуальный переводчик с автоматическим определением языка.
Точка входа в приложение: инициализирует компоненты системы
и запускает основной рабочий процесс.
"""

from ui import UserInterface
from language_detection import detect_language
from translation_engine import translate_text
from history_manager import HistoryManager
from optimization import cache_translation, get_cached_translation


def main() -> None:
    """
    Запустить основной рабочий процесс приложения-переводчика.

    Инициализирует модули интерфейса и истории, выполняет
    автоматическое определение языка введённого текста,
    перевод и сохранение результата в историю.
    Перед обращением к движку перевода проверяет кэш.

    :return: None

    Пример запуска::

        $ python main.py
        Запуск приложения переводчика
        Определённый язык: Английский
        Результат перевода: [Перевод на ru]: Hello world
    """
    print("Запуск приложения переводчика")

    ui = UserInterface()
    history = HistoryManager()

    # Имитация ввода пользователя
    text = "Hello world"
    ui.input_text = text

    # Определение языка
    language = detect_language(ui.get_user_input())
    print("Определённый язык:", language)

    # Проверка кэша перед переводом
    cached = get_cached_translation(text)
    if cached:
        result = cached
    else:
        result = translate_text(text, "ru")
        cache_translation(text, result)

    # Отображение результата и сохранение в историю
    ui.display_result(result)
    history.save_translation(text, result)

    print("Результат перевода:", result)


if __name__ == "__main__":
    main()
