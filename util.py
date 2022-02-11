import csv

import pyperclip


def get_multi_line():
    print("(enter a blank line or . to stop)")
    results = []
    while True:
        line = input()
        if line in ("", "."):
            break
        results.append(line)
    return results


def write_file(results, filename):
    if len(results) == 0:
        print("No rows to print. Quitting.")
        return
    fields = results[0].keys()
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for row in results:
            writer.writerow(row)


def format_string(results):
    transformed = ["\t".join(row.values()) for row in results]
    result_str = "\n".join(transformed)
    return result_str


def copy_to_clipboard(results):
    formatted = format_string(results)
    pyperclip.copy(formatted)
