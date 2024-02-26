#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def edit_utf8():
    # open the text.txt in append mode.
    # Create a new file if no such file exists.
    with open("text.txt", "w", encoding="utf-8") as fileptr:
        # appending the content to the file
        print(
            "UTF-8 is a variable-width character encoding used"
            " for electronic communication.",
            file=fileptr,
        )
        print(
            "UTF-8 is capable of encoding all 1,112,064"
            " valid character code points.",
            file=fileptr,
        )
        print(
            "In Unicode using one to four one-byte (8-bit) code units.",
            file=fileptr,
        )


def find_sent():
    with open("text.txt", "r", encoding="utf-8") as fileptr:
        sentences = fileptr.readlines()

    # Вывод предложений с запятыми.
    for sentence in sentences:
        if "," in sentence:
            print(sentence)


def main():
    edit_utf8()
    find_sent()


if __name__ == "__main__":
    main()
