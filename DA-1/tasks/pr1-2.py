#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def writefile():
    # open the file2.txt in append mode.
    # Create a new file if no such file exists.
    # open the file2.txt in append mode.
    # Create a new file if no such file exists.Ω
    with open("file2.txt", "w") as fileptr:
        fileptr.write(
            "Python is the modern day language. "
            "It makes things so simple.\n"
            "It is the fastest-growing programing language"
        )
    # closing the opened the file
    fileptr.close()


# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def writefile2():
    # open the file2.txt in write mode.
    with open("file2.txt", "a") as fileptr:
        # overwriting the content of the file
        fileptr.write(
            " Python has an easy syntax and user-friendly interaction."
        )


def main():
    writefile2()


if __name__ == "__main__":
    main()
