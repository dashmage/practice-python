"""
tail.py

Usage: tail.py <no of lines to print from end> <file name>

Example:
$ python tail.py 5 somelog.txt
This will print the last 5 lines from the file "somelog.txt"
"""

import sys


def tail(k, file):
    with open(file, "rb") as file:
        # Move the file pointer to the end of the file
        file.seek(-1, 2)

        # If last char is newline, skip it
        # meaning, if last char is newline, the file pointer would be at seek(-1, 2)
        # otherwise at seek(0, 2)
        if file.read(1) == b"\n":
            file.seek(-1, 1)

        end = file.tell()

        lines = []
        buffer = bytearray()

        # Iterate backwards through the file
        # The file pointer should be at the previous character to read the current one
        for pos in range(end - 1, -1, -1):
            file.seek(pos)
            char = file.read(1)

            if char == b"\n":
                lines.append(buffer.decode()[::-1])
                buffer = bytearray()
                if len(lines) == k:
                    break
            else:
                buffer.extend(char)

        # Handle the last line (in case there's no newline at the end)
        if buffer:
            lines.append(buffer.decode()[::-1])

        # Print lines in correct order
        for line in reversed(lines):
            print(line)


tail(int(sys.argv[1]), sys.argv[2])
