#!/usr/bin/python3

import requests
import argparse 

#assuming that a server is already running, with root dir for this program hard set


BASE = "http://localhost:5000/"
TIMEOUT = 500

def get_dir(args):
    dir_response = requests.get(BASE + '/dir/' + args.path, timeout=TIMEOUT)
    print(dir_response.json())

def get_file(args):
    file_response = requests.get(BASE + '/file/' + args.path, timeout=TIMEOUT)
    print(file_response.json())

parser = argparse.ArgumentParser(description='This program lets you explore a file system', exit_on_error=False)
sp = parser.add_subparsers()

lst = sp.add_parser("list", help="Shows the contents of the directory. Passing 'root' as the path displays the contents of the root directory.")
lst.add_argument("path", help="Path to directory")
lst.set_defaults(func=get_dir)

show = sp.add_parser("show", help="Display the contents of the file")
show.add_argument("path", help="Path to file")
show.set_defaults(func=get_file)


print("Welcome! To view possible commands enter \'--help\' at any time.\n")

PROMPT = ">>> "

while(True):
    user_input = input(PROMPT).split()
    
    try:
        args = parser.parse_args(user_input)
        args.func(args)

    except argparse.ArgumentError:
        print("parse error- retry or type \"--help\"\n")
    except SystemExit:
        continue