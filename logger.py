# Модуль для записи результатов вычислений
import os


def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    if os.path.exists('log.txt'):
        file = open('log.txt', 'a')
    else:
        file = open('log.txt', 'w')
    file.write(f'{expr} -> {result}\n')
    file.close()


def get_history() -> str:
    """"Возвращает содержимое файла с результатами вычислений"""
    if os.path.exists('log.txt'):
        with open('log.txt', 'r') as file:
            return file.read()
    else:
        return 'Файл log.txt не существует'
