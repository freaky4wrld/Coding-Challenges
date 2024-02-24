#!/usr/bin/env python3
import argparse
import os
import sys

def count_bytes(filename):

    try:
        with open(filename,'rb') as file:
            #get file_size in bytes
            file_size = os.path.getsize(filename)
            return file_size
    except FileNotFoundError:
        print(f"Error: {filename} not found")
    except IOError:
        print(f"Error reading {filename}")

def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            #getting lines count with length of array
            lines_count = len(file.readlines())
            return lines_count
    except FileNotFoundError:
        print(f"Error: {filename} not found")
    except IOError:
        print(f"Error reading {filename}")

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            #getting words count
            word_count = 0
            for line in file.readlines():
                word_count+=len(line.split())
            return word_count    
    except FileNotFoundError:
        print(f"Error: {filename} not found")
    except IOError:
        print(f"Error reading {filename}")

def count_characters(filename):
    try:
        with open(filename, 'rb') as file:
            #getting words count
            char_count = len(file.read())
            return char_count    
    except FileNotFoundError:
        print(f"Error: {filename} not found")
    except IOError:
        print(f"Error reading {filename}")

def main():
    parser = argparse.ArgumentParser(description="sample text for tool")
    parser.add_argument('filename', help='Path to file')
    parser.add_argument('-c', action="store_true", help="sample text for details")
    parser.add_argument('-l', action="store_true", help="sample text for details")
    parser.add_argument('-w', action="store_true", help="sample text here for details")
    parser.add_argument('-m', action="store_true", help="sample text here for details")

    args = parser.parse_args()

    if args.c:
        print(f"{count_bytes(args.filename)} {args.filename}")
    elif args.l:
        print(f"{count_lines(args.filename)} {args.filename}")
    elif args.w:
        print(f"{count_words(args.filename)} {args.filename}")
    elif args.m:
        print(f"{count_characters(args.filename)} {args.filename}")
    else:
        print(f"{count_lines(args.filename)}  {count_words(args.filename)}  {count_bytes(args.filename)} {args.filename}")


if __name__ == "__main__":
    main()
