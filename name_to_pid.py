import csv
import readline

import pyperclip
from thefuzz import fuzz, process

import util

readline.parse_and_bind("tab: complete")


def format_result(result):
    (_, full_name), score, pid = result
    return f"{full_name} ({score})"


def main():
    master_list_name = input("Enter 5 year list path: ")
    print("Enter names:")
    in_names = util.get_multi_line()

    with open(master_list_name) as f:
        master_list = csv.DictReader(f)
        names = {}
        for row in master_list:
            full_name = row["FullName"]
            processed_name = fuzz.utils.full_process(full_name)
            names[row["PersonID"]] = (processed_name, full_name)

    result_pids = []
    result_names = []
    for name in in_names:
        results = process.extract(
            (fuzz.utils.full_process(name), name),
            names,
            limit=5,
            scorer=fuzz.WRatio,
            processor=lambda x: x[0],
        )

        print(name)
        for i, result in enumerate(results):
            print(f"    [{i + 1}] {format_result(result)}")

        correct_index = int(input("Which is correct? ")) - 1
        result_pids.append(results[correct_index][2])
        result_names.append(results[correct_index][0][1])

    outfile_name = input("Enter outfile name or press Enter to copy to clipboard: ")
    if len(outfile_name) < 2:
        results = [{"PersonID": x} for x in result_pids]
        util.copy_to_clipboard(results)
    else:
        results = [
            {"PersonID": pid, "FullName": name}
            for pid, name in zip(result_pids, result_names)
        ]
        util.write_file(results, outfile_name)


if __name__ == "__main__":
    main()
