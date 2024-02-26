#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def rename():
    os.rename("file2.txt", "file3.txt")


def remove():
    os.remove("file3.txt")


def create_dir():
    os.mkdir("new")


def getcwd():
    print(os.getcwd())


def ch():
    os.chdir("C:\\Windows")
    print(os.getcwd())


def remove_dir():
    os.rmdir("new")


def main():
    rename()
    remove()
    create_dir()
    getcwd()
    remove_dir()
    ch()


if __name__ == "__main__":
    main()
