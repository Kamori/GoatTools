# Purpose
# To mimic the GNU/cat utility for printing file contents

# Lessons learned
# * If you want to print b'' without the prefix. Just write straight to stdout

# TODO: implement GNU/cat flags

import sys


def readfile(file):
    with open(file, "rb") as f:
        return basic(f)


def basic(filehandle):
    if isinstance(filehandle, str):
        return filehandle

    filehandle.seek(0)
    return [i for i in filehandle][::-1]


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        # Assume its stdin
        data = sys.stdin.read()
        sys.stdout.buffer.write(basic(data))

    # Lets cat out each file in order
    for file in sys.argv[1:]:
        for line in readfile(file):
            sys.stdout.buffer.write(line)
