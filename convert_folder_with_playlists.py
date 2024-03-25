import sys
from pathlib import Path
import re
import os

def main():
    if not (len(sys.argv) == 3):
        print(sys.argv)
        print("Need 2 arguments: directory and prefix path")
        exit
    #source_file = Path(sys.argv[1])
    #target_file = Path(sys.argv[2])
    #prefix_path = sys.argv[3]
    files = walkdir(Path(sys.argv[1]))
    print(files)

def walkdir(dirname: Path) -> [Path]:
    walk_files = []
    for cur, _dirs, files in os.walk(dirname):
        print(cur)
        for f in files:
            path = Path(cur + "/" + f)
            walk_files.append(path)
    return walk_files

def convert_file(source_file: Path, target_file: Path, prefix: str):
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
