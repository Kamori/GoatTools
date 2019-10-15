#!/usr/bin/env python3

import os
from pathlib import Path
from typing import List, Tuple

dir_path = os.path.dirname(os.path.realpath(__file__))


def tool_written(toolname: str) -> List[Tuple]:
    files = Path(f"{dir_path}/..").glob(f"goattools_*/{toolname}.*")
    res = []
    for file in files:
        res.append((True, file.parent.name.split("goattools_")[1]))
    return res


def test_written(toolname: str, language: str) -> Tuple[bool, int]:
    count = 0
    files = Path(f"{dir_path}/../tests").glob(f"{language}_tests/{toolname}_test.*")
    files = list(files)
    if files:
        test = files[0]
        count = test_counts(test)

    return bool(files), count


def test_counts(file: Path) -> int:
    # one of each of these must be present to count as a test
    function_def_labels = ["def", "func"]
    test_labels = ["_test", "test_"]

    count = 0

    with file.open() as f:
        for line in f.readlines():

            # Are func defs AND tests found in line?
            found_func = any([found in line for found in function_def_labels])
            found_test = any([found in line for found in test_labels])

            if found_func and found_test:
                count += 1

    return count


if __name__ == "__main__":
    with open(f"{dir_path}/../tools.txt", "r") as f:
        f_contents = f.readlines()

    # This isn't an ordered dict, but I wrote this with python3.7 so it s
    # It won't be for you if your version is too old. But, it doesn't need to
    # be
    datatable = {}

    for line in f_contents:
        line = line.rstrip()
        tools = tool_written(line)

        # If we haven't written it, skip it
        if not tools:
            continue

        results = []
        for status, language in tools:
            test_status, test_count = test_written(line, language)

            results.append(
                {
                    "status": status,
                    "language": language,
                    "test_status": test_status,
                    "test_count": test_count,
                }
            )
            datatable[line] = results

    from pprint import pprint

    pprint(datatable)

    ## TODO: turn this into a markdown table
