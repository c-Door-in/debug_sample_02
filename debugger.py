"""Общий для всех алгоритмов дебага код.
Писать его каждый раз не нужно, достаточно импортировать готовое.
К этому документу код debugger.py приложен лишь для наглядности.
"""
import random

HEADER = '\033[95m'
BOLD = '\033[1m'
ENDC = '\033[0m'


def input_answer():
    while True:
        answer = input('да или нет: ').lower()
        if answer == 'да' or answer == 'нет':
            return answer

def check(вопрос: str) -> bool:
    print(f'{BOLD}Вопрос:{ENDC} {вопрос}')
    result_flag = True if input_answer() == 'да' else False
    print(f'{BOLD}Ответ:{ENDC} {HEADER}{result_flag and "Да" or "Нет"}{ENDC}')
    print()
    return result_flag

def do(что_сделать: str):
    print(f'{BOLD}Делаю{ENDC}: {что_сделать}')