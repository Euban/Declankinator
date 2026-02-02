# As input, various filterlist raw URLs. Output is a merged filterlist of raw URLs, without duplicates. To be then used with GenerateList.py

import os
import argparse
import pathlib
import shutil

def main():
    directory = os.getcwd()
    outputname = "mergedlist.txt"
    parser = argparse.ArgumentParser()
    parser.add_argument('-filepath', '-f', type=str, help="Path with filterlists")
    args = parser.parse_args()

    if args.filepath:
        directory = pathlib.Path(args.filepath)
    
    with open(directory / outputname, 'w', encoding="UTF-8") as output:
        for filename in os.listdir(directory):
            if filename.endswith(".txt") and outputname not in filename:
                with open(os.path.join(directory, filename), 'r', encoding="UTF-8") as f:
                    output.write(f.read())
                    output.write("\n")
    
if __name__ == "__main__":
    main()
    