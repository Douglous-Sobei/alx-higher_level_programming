#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_count = len(argv)
    index = 1
    result = 0
    while index <= argv_count:
        result += int(sys.argv[index])
        index += 1
    print("{:d}".format(result))
