"""
Главный модуль проекта
Интеллектуальный переводчик с автоматическим определением языка
"""

from ui import UserInterface
from language_detection import detect_language
from translation_engine import translate_text


def main():
    print("Запуск приложения переводчика")
    
    # Пример имитации рабочего процесса
    text = "Hello world"
    language = detect_language(text)
    result = translate_text(text, "ru")
    
    print("Определённый язык:", language)
    print("Результат перевода:", result)


if __name__ == "__main__":
    main()
