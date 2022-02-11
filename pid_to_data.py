"""Extract records given a list of PersonIDs and a master list."""
import csv
import readline

import util

readline.parse_and_bind("tab: complete")


def main():
    master_list_name = input("Enter 5 year list path: ")
    print("Paste in list of PIDs:")
    pids = util.get_multi_line()

    print("Enter field names:")
    field_names = util.get_multi_line()
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
        util.copy_to_clipboard(results)
    else:
        util.write_file(results, outfile_name)


if __name__ == "__main__":
    main()
