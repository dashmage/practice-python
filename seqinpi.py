"""
seqinpi.py

Usage: seqinpi <sequence size> <no of digits to search>

Example:
$ python seqinpi 7 10000
Finds whether a sequence of 7 digits repeats in the first 10000 digits of pi.
The script reads the file "pi-100k.txt" to retrieve upto the first 100k digits of pi.
"""

import sys


def findseq(seqsize, search_length):
    digit_index = 0
    seq_index_map = {}
    src = open("pi-100k.txt", "rb")
    # skip the "3." and start from 1415...
    src.read(2)
    current = bytearray(src.read(seqsize))
    seq_index_map.update({bytes(current): digit_index})

    while digit_index < search_length:
        digit_index += 1
        for x in range(seqsize - 1):
            current[x] = current[x + 1]
        # src.read(1) gives a number in bytes like b'5'
        # which needs to be converted to ascii integer when stored in the bytearray like 53
        # or do: current[seqsize - 1] = bytearray(src.read(1))[0]
        current[seqsize - 1] = ord(src.read(1))

        # has the current sequence been encountered before?
        duplicate_index = seq_index_map.get(bytes(current), -1)

        if duplicate_index == -1:
            seq_index_map.update({bytes(current): digit_index})
        else:
            print(
                f"Repeated sequence found for length {seqsize}, Sequence={current}, first index={duplicate_index + 1}, second index={digit_index + 1}, "
            )
            break
    src.close()


findseq(int(sys.argv[1]), int(sys.argv[2]))
