#Take URL and make filterlist, for example:
#aibullshit.slop = 
#duckduckgo.com,bing.com##a[href*="aibullshit.slop"]:upward(li):remove()
#google.com##a[href*="aibullshit.slop"]:upward(2):remove()
#*://*.aibullshit.slop/*

import os
import argparse
import pathlib
import re

def createList(URL, outputFile):
    if URL.endswith("/"):
        URL = URL[:-1]
    #Remove http(s)://www.
    URL = re.sub("(https?:\/\/)(\s)*(www\.)?(\s)*", '', URL)

    DDGPattern = f'duckduckgo.com,bing.com##a[href*="{URL}"]:upward(li):remove()'
    GGLPattern = f'google.com##a[href*="{URL}"]:upward(2):remove()'
    HTTPPattern = f'*://*.{URL}/*'

    outputFile.write(f'{DDGPattern}\n')
    outputFile.write(f'{GGLPattern}\n')
    outputFile.write(f'{HTTPPattern}\n')
def main():
    output = pathlib.Path(os.getcwd())
    #Simply get an arg for the directory of the videos
    parser = argparse.ArgumentParser()
    parser.add_argument('-txt', '-t', type=str, help="Path for a txt file with list of URLs, seperated by newlines, to create filters for")
    parser.add_argument('-output', '-o', type=str, help="Enter output directory, will create/append to a 'output.txt'")
    parser.add_argument('-single', '-s', type=str, help="Enter a domain name to create one filter for")
    args = parser.parse_args()
    if args.output:
        output = pathlib.Path(args.output)
    output = output / "output.txt"

    with open(output, 'a', encoding="UTF-8") as outputFile:
        if args.single:
            singleStr = args.single
            createList(singleStr, outputFile)
        elif args.txt:
            directory = pathlib.Path(args.txt)
            file = open(directory, 'r', encoding="UTF-8")
            for line in file:
                createList(str(line).rstrip(), outputFile)
            file.close()
        else:
            print("Specify a .txt file of URLs with -t or a single URL with -s!")
            exit(1)

if __name__ == "__main__":
    main()
    