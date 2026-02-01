#Take URL and make filterlist, for example:
#aibullshit.slop = 
#duckduckgo.com,bing.com##a[href*="aibullshit.slop"]:upward(li):remove()
#google.com##a[href*="aibullshit.slop"]:upward(2):remove()
#*://*.aibullshit.slop/*
#*://aibullshit.slop/*

import os
import argparse
import pathlib
import re

def createList(URL, uBlockorig, uBlacklist):
    if URL.endswith("/"):
        URL = URL[:-1]
    #Remove http(s)://www.
    URL = re.sub("(https?:\/\/)(\s)*(www\.)?(\s)*", '', URL)

    DDGPattern = f'duckduckgo.com,bing.com##a[href*="{URL}"]:upward(li):remove()'
    GGLPattern = f'google.com##a[href*="{URL}"]:upward(2):remove()'
    HTTPPattern1 = f'*://*.{URL}/*'
    HTTPPattern2 = f'*://{URL}/*'

    uBlockorig.write(f'{DDGPattern}\n')
    uBlockorig.write(f'{GGLPattern}\n')
    uBlockorig.write(f'{HTTPPattern2}\n')
    uBlacklist.write(f'{HTTPPattern1}\n')
def main():
    output = pathlib.Path(os.getcwd())
    #Simply get an arg for the directory of the videos
    parser = argparse.ArgumentParser()
    parser.add_argument('-txt', '-t', type=str, help="Path for a txt file with list of URLs, seperated by newlines, to create filters for")
    parser.add_argument('-output', '-o', type=str, help="Enter output directory")
    parser.add_argument('-single', '-s', type=str, help="Enter a domain name to create one filter for")
    args = parser.parse_args()
    if args.output:
        output = pathlib.Path(args.output)
    outputuBlockorig = output / "uBlockorig.txt"
    outputuBlacklist = output / "uBlacklist.txt"

    with open(outputuBlockorig, 'a', encoding="UTF-8") as block, open(outputuBlacklist, 'a', encoding="UTF-8") as black:
        if args.single:
            singleStr = args.single
            createList(singleStr, block, black)
        elif args.txt:
            directory = pathlib.Path(args.txt)
            file = open(directory, 'r', encoding="UTF-8")
            for line in file:
                createList(str(line).rstrip(), block, black)
            file.close()
        else:
            print("Specify a .txt file of URLs with -t or a single URL with -s!")
            exit(1)

if __name__ == "__main__":
    main()
    