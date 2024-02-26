import sys
import os


def find_undocumented_functions(file_path):
    undocumented_functions = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if line.startswith("def "):
                if i > 0 and not lines[i - 1].strip().startswith("#"):
                    function_name = line.split("(")[0][4:]
                    undocumented_functions.append((function_name, i + 1))
    return undocumented_functions


def main():
    if len(sys.argv) < 2:
        print("Usage: python ind2.py test2.py [...]")
        sys.exit(1)

    files = sys.argv[1:]
    for file in files:
        if not os.path.exists(file):
            print(f"File '{file}' not found.")
            continue
        try:
            undocumented_functions = find_undocumented_functions(file)
            if undocumented_functions:
                print(f"Undocumented functions in '{file}':")
                for function in undocumented_functions:
                    print(f"  {function[0]} (Line {function[1]})")
        except Exception as e:
            print(f"Error processing file '{file}': {e}")


if __name__ == "__main__":
    main()
