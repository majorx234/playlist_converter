import sys
from pathlib import Path
import re

def main():
    if not (len(sys.argv) == 4):
        print(sys.argv)
        print("Need 3 arguments: source file, target file, prefix path")
        exit
    source_file = Path(sys.argv[1])
    target_file = Path(sys.argv[2])
    prefix_path = sys.argv[3]
    if not source_file.exists():
        print("source file error: not exist")
    with source_file.open('r') as sfile:
        with target_file.open('a') as tfile:
            lines = sfile.readlines()
            for line in lines:
                new_line = line.replace("E:\\", prefix_path).replace("\\", "/")
                tfile.write(new_line)

if __name__ == "__main__":
    main()
