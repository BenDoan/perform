import os
import subprocess
import sys

from os import path

def is_executable(f):
    return path.isfile(f) and os.access(f, os.X_OK)

def get_programs():
    programs = []
    for p in os.environ['PATH'].split(os.pathsep):
        if path.isdir(p):
            for f in os.listdir(p):
                if not is_executable(f):
                    programs.append(f)
    return programs

def get_function(name):
    def f(*args):
        args = [name] + list(args)
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        return p.communicate()
    return f
valid_names = (x for x in get_programs() if x.isalpha())
for f in valid_names:
    globals()[f] = get_function(f)
