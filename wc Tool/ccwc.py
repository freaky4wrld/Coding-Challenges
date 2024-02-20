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

def main():
    parser = argparse.ArgumentParser(description="sample text for tool")
    parser.add_argument('filename', help='Path to file')
    parser.add_argument('-c', action="store_true", help="sample text for details")
    args = parser.parse_args()

    if args.c:
        count_bytes(args.filename)
    else:
        print(f"work in progress {args.filename}")


if __name__ == "__main__":
    main()
