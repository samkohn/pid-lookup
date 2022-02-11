"""Extract records given a list of PersonIDs and a master list."""
import csv
import readline
readline.parse_and_bind("tab: complete")

import pyperclip



def write_file(results, filename):
    if len(results) == 0:
        print("No rows to print. Quitting.")
        return
    fields = results[0].keys()
    with open(filename, 'w') as f:
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

def get_multi_line():
    print("(enter a blank line or . to stop)")
    results = []
    while True:
        line = input()
        if line in ("", "."):
            break
        results.append(line)
    return results


def main():
    master_list_name = input("Enter 5 year list path: ")
    print("Paste in list of PIDs:")
    pids = get_multi_line()

    print("Enter field names:")
    field_names = get_multi_line()
    if "PersonID" not in field_names:
        field_names.append("PersonID")

    with open(master_list_name) as f:
        master_list = csv.DictReader(f)
        results = []
        for row in master_list:
            if row["PersonID"] in pids:
                entry = {field: row[field] for field in field_names}
                results.append(entry)
        results = sorted(results, key=lambda d: pids.index(d["PersonID"]))

    outfile_name = input("Enter outfile name or press Enter to copy to clipboard: ")
    if len(outfile_name) < 2:
        copy_to_clipboard(results)
    else:
        write_file(results, outfile_name)


if __name__ == "__main__":
    main()
