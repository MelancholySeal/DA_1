#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def find_undocumented_functions(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        return
    except IOError:
        print(f"Ошибка при открытии файла '{file_path}'.")
        return

    undocumented_functions = []

    in_function = False
    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if line.startswith("def "):
            function_name = line.split("(")[0].split("def ")[1]
            in_function = True
            if not (
                line_num > 1 and lines[line_num - 2].strip().startswith("#")
            ):
                undocumented_functions.append(
                    (function_name, file_path, line_num)
                )
        elif line.startswith("class "):
            in_function = False
        elif line.startswith("#") and in_function:
            in_function = False
    file.close()
    return undocumented_functions


def main():
    if len(sys.argv) < 2:
        print("Использование: python script.py file1.py file2.py ...")
        return

    for file_path in sys.argv[1:]:
        undocumented_functions = find_undocumented_functions(file_path)
        if undocumented_functions:
            print(f"Недокументированные функции в файле '{file_path}':")
            for function in undocumented_functions:
                print(
                    f"    - Функция '{function[0]}'"
                    f" начинается на строке {function[2]}"
                )
        else:
            print(f"В файле '{file_path}' нет недокументированных функций.")


if __name__ == "__main__":
    main()
