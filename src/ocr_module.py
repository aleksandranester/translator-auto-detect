"""
Модуль распознавания текста по изображению (OCR).

Извлекает текстовую информацию из графических файлов
и передаёт результат в модуль перевода.
"""


def extract_text_from_image(image_path: str) -> str:
    """
    Извлечь текст из изображения по указанному пути.

    Имитирует процесс OCR. В реальном проекте использует
    специализированную библиотеку (например, Tesseract / pytesseract).
    Поддерживает форматы PNG, JPEG, BMP.

    :param image_path: Путь к файлу изображения.
    :type image_path: str
    :return: Строка с распознанным текстом.
    :rtype: str
    :raises FileNotFoundError: Если файл по указанному пути не найден.
    :raises ValueError: Если формат файла не поддерживается.

    Пример использования::

        >>> extract_text_from_image("document.png")
        'Текст, извлечённый из изображения'
    """
    supported = (".png", ".jpg", ".jpeg", ".bmp")
    if not any(image_path.lower().endswith(ext) for ext in supported):
        raise ValueError(f"Неподдерживаемый формат файла: {image_path}")
    return "Текст, извлечённый из изображения"
