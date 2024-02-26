#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import secrets
import string
import sys


def count_args():
    print("Number of arguments:", len(sys.argv), "arguments")
    print("Argument List:", str(sys.argv))


def find_args():
    for idx, arg in enumerate(sys.argv):
        print(f"Argument #{idx} is {arg}")
    print("No. of arguments passed is ", len(sys.argv))


def generate_password():
    if len(sys.argv) != 2:
        print("The password length is not given!", file=sys.stderr)
        sys.exit(1)

    chars = string.ascii_letters + string.punctuation + string.digits
    length_pwd = int(sys.argv[1])

    result = []
    for _ in range(length_pwd):
        idx = secrets.SystemRandom().randrange(len(chars))
        result.append(chars[idx])

    print(f"Secret Password: {''.join(result)}")


def main():
    generate_password()


if __name__ == "__main__":
    main()
