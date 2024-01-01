import argparse
import sys
import os

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, help='Шлях до зображення')
    parser.add_argument('--per_click', type=int, help='Кількість кліків')
    parser.add_argument('--threshold', type=int, help='Поріг для порівняння')
    return parser


def validate_threshold():
    args = get_parser().parse_args()

    if args.threshold and not isinstance(args.threshold, int):
        print('Значення не є числом.')
        sys.exit()

    if isinstance(args.threshold, int) and args.threshold > 1:
        print('Значення не має бути більше 1.')
        sys.exit()

    if args.threshold:
        return args.threshold
    
    return 0.8


def validate_args_per_click():
    args = get_parser().parse_args()

    if args.per_click and not isinstance(args.per_click, int):
        print('Значення не є числом.')
        sys.exit()

    if args.per_click:
        return args.per_click

    return 30


def validate_args_path():
    args = get_parser().parse_args()
    
    if not args.path:
        print('Відсутній необхідний параметр --path. Будь ласка, вкажіть шлях до зображення.')
        sys.exit()

    if not os.path.isfile(args.path):
        print('Файл не існує. Перевірьте правильність вводу маршруту.')
        sys.exit()

    if not args.path.lower().endswith(('.png', '.jpg', '.jpeg')):
        print("Файл не є зображенням.")
        sys.exit()

    return args.path