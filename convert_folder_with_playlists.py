import sys
from pathlib import Path
import re
import os
import codecs

def main():
    if not (len(sys.argv) == 4):
        print(sys.argv)
        print("Need 2 arguments: source dir, target_dir and prefix path")
        exit
    source_folder = Path(sys.argv[1])
    target_folder = Path(sys.argv[2])
    prefix_path = sys.argv[3]
    files = walkdir(source_folder)
    for file in files:
        source_file = source_folder / file
        target_file = target_folder / file
        print(source_file)
        if not target_file.parent.exists():
            target_file.parent.mkdir(parents=True)
        convert_file(source_file, target_file, prefix_path)

def walkdir(dirname: Path) -> [Path]:
    walk_files = []
    for cur, _dirs, files in os.walk(dirname):
        for f in files:
            path = Path(cur + "/" + f)
            walk_files.append(path.relative_to(dirname))
    return walk_files

def convert_file(source_file: Path, target_file: Path, prefix_path: str):
    if not source_file.exists():
        print("source file error: not exist")
    with source_file.open('r', encoding="ISO-8859-1") as sfile:
        with target_file.open('a', encoding="ISO-8859-1") as tfile:
            lines = sfile.readlines()
            for line in lines:
                new_line = line.replace("E:\\", prefix_path).replace("\\", "/")
                tfile.write(new_line)

if __name__ == "__main__":
    main()
