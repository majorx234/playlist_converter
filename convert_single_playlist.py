import sys

def main():
    if not (len(sys.argv) == 3):
        print(sys.argv)
        print("Need 2 arguments: source file, target file")
        exit
    else:    
        source_file = sys.argv[1] 
        target_file = sys.argv[2] 
if __name__ == "__main__":
    main()
