#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def main():
    filename = "ind1.txt"

    # Чтение текста из файла
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    # Разделение текста на предложения
    sentences = re.split(r"(?<=[.!?])\s+", text)

    # Вывод предложений, начинающихся с тире и пробельных символов перед ним
    for sentence in sentences:
        if re.match(r"\s*-", sentence):
            print(sentence)


if __name__ == "__main__":
    main()
