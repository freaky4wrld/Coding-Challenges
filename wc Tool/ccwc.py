#!/usr/bin/env python3
import argparse
import os
import sys

def count_bytes(filename):

    try:
        with open(filename,'rb') as file:
            #get file_size in bytes
            file_size = os.path.getsize(filename)
            print(f"{file_size} {filename}")
    except FileNotFoundError:
        print(f"Error: {filename} not found")
    except IOError:
        print(f"Error reading {filename}")

def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            #getting lines count with length of array
            lines_count = len(file.readlines())
            print(f"{lines_count} {filename}")
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
            print(f"{word_count} {filename}")    
    except FileNotFoundError:
        print(f"Error: {filename} not found")
    except IOError:
        print(f"Error reading {filename}")

def count_characters(filename):
    try:
        with open(filename, 'rb') as file:
            #getting words count
            char_count = len(file.read())
            print(f"{char_count} {filename}")    
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
        count_bytes(args.filename)
    elif args.l:
        count_lines(args.filename)
    elif args.w:
        count_words(args.filename)
    elif args.m:
        count_characters(args.filename)
    else:
        print(f"work in progress {args.filename}")


if __name__ == "__main__":
    main()
