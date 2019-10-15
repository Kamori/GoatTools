#!/usr/bin/env python3

import os
from pathlib import Path
from typing import Dict, List, Tuple

dir_path = os.path.dirname(os.path.realpath(__file__))


def tool_data(tools: List[str]) -> Dict:
    # This isn't an ordered dict, but I wrote this with python3.7 so it s
    # It won't be for you if your version is too old. But, it doesn't need to
    # be
    datatable = {}
    results = []

    for line in tools:
        line = line.strip()
        tools = tool_written(line)

        # If we haven't written it, skip it
        if not tools:
            continue

        # results = []
        for status, language in tools:
            test_status, test_count = test_written(line, language)

            results.append(
                {
                    "test_status": test_status,
                    "test_count": test_count,
                    "status": status,
                    "language": language,
                    "name": line,
                }
            )
            datatable[line] = results

    return results


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
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Process some integers.")

    parser.add_argument(
        "--format",
        dest="output_format",
        choices=["markdown-table", "json"],
        default="json",
        help="How to import tool/test datas",
        required=True,
    )

    args = parser.parse_args()

    with open(f"{dir_path}/../tools.txt", "r") as f:
        f_contents = f.readlines()

    tool_list = tool_data(f_contents)

    if args.output_format == "json":
        print(json.dumps(tool_list))

    elif args.output_format == "markdown-table":

        # Print header
        print("|" + " | ".join(tool_list[0].keys()) + "|")
        print("|" + " | ".join(["-" * len(i) for i in tool_list[0].keys()]) + "|")

        for tool in tool_list:
            lineout = "|" + " | ".join([str(value) for _, value in tool.items()]) + "|"
            lineout = lineout.replace("True", ":white_check_mark:")
            lineout = lineout.replace("False", ":x:")
            print(lineout)

    else:
        print("To be developed")
