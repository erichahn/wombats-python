#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import bottle
from bottle import route, run, request, abort


import GithubPullFile
import Parse

def main():
    print("Test")
    Parse.run_command(input_file)

if __name__ == "__main__":
    main()
