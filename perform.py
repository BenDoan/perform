"""
Perform is for calling processes from python in a simple and easy way.  Each program is added to the perform module as a function that returns a tuple of (stdout, stdin).

Examples:
To call a normal program that whose name doesn't contain symbols:
    stdin, stdout = perform.ls()

To pass arguments to a program:
    stdout = perform.git("ls-files", "-m")[0]

To call a program that contains symbols in its name:
    stdin, stdout = perform._("pip2.7", "install", "perform")
"""

import os
import subprocess
import sys

from os import path

def _is_executable(f):
    return path.isfile(f) and os.access(f, os.X_OK)

def _run_program(name, *args):
    args = [name] + list(args)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return tuple((x.decode(sys.getdefaultencoding()) for x in p.communicate()))

def _get_function(name):
    return lambda *args: _run_program(name, *args)

def get_programs():
    """Returns a list of the available executable programs"""
    programs = []
    os.environ['PATH'] += os.pathsep + os.getcwd()
    for p in os.environ['PATH'].split(os.pathsep):
        if path.isdir(p):
            for f in os.listdir(p):
                if _is_executable(path.join(p, f)):
                    programs.append(f)
    return programs


valid_names = (x for x in get_programs() if x.isalpha())
for f in get_programs():
    if f.isalpha():
        globals()[f] = _get_function(f)

globals()["_"] = lambda name, *args: _run_program(name, *args)
