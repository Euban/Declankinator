#Simply removes duplicate lines through the txt file. Inefficient? Yeah. 

import os
import argparse
import pathlib
import shutil

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-txt', '-t', type=str, help="Path for a txt file to check for duplicate lines")
    args = parser.parse_args()

    if args.txt:
        output = pathlib.Path(args.txt)
        inputFile = pathlib.Path(args.txt)

    backup = inputFile.name + ".backup"
    #Swear there's a better way to get the dir, stripped of the file name
    backupDir = inputFile.parents[0]
    shutil.copyfile(inputFile, backupDir / backup)
    
    newfile = inputFile.name + "newtmp"
    with open (backupDir / newfile, 'w', encoding="UTF-8") as new, open(inputFile, 'r', encoding="UTF-8") as old:
        seenb4 = set()
        for line in old:
            if line not in seenb4:
                new.write(line)
                seenb4.add(line)
            else:
                print(f"Seen this before: {line}")
    
    pathlib.Path.unlink(inputFile)
    os.rename(backupDir / newfile, inputFile)

if __name__ == "__main__":
    main()
    