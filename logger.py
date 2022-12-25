# Модуль для записи результатов вычислений
import os


def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    if os.path.exists('log.txt'):
        file = open('log.txt', 'a', encoding='utf-8')
    else:
        file = open('log.txt', 'w', encoding='utf-8')
    file.write(f'{expr} -> {result}\n')
    file.close()


def get_history() -> str:
    """"Возвращает содержимое файла с результатами вычислений"""
    if os.path.exists('log.txt'):
        with open('log.txt', 'r', encoding='utf-8') as file:
            return file.read()
    else:
        return 'Файл log.txt не существует'
