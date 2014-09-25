"""
Perform is for calling processes from python in a simple and easy way.  Each program is added to the perform module as a function that returns the stdout printed by the program.

Examples:
To call a normal program that whose name doesn't contain symbols:
    stdout = perform.ls()

To pass arguments to a program:
    stdout = perform.git("ls-files", "-m")

To call a program that contains symbols in its name:
    stdout = perform._("pip2.7", "install", "perform")

To get stderr from a program:
    try:
        perform.git("asdad")
    except Exception as e:
        print(str(e))

To call a command in the shell:
    print(perform._("ls | grep 'py'", shell=True))
"""
from __future__ import unicode_literals

import os
import re
import subprocess
import sys

from os import path
from functools import partial

__author__ = "Ben Doan <ben@bendoan.me>"
__version__ = "0.0.3"

class StandardErrorException(Exception):
    pass

class ProgramNotFoundException(Exception):
    pass

def _is_executable(f):
    return path.isfile(f) and os.access(f, os.X_OK)

def _run_program(name, shell=False, *args):
    args = [name] + list(args)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=shell)
    stdout, stderr = tuple(x.decode(sys.getdefaultencoding()) for x in p.communicate())
    if stderr != "":
        raise StandardErrorException(stderr.strip())
    return stdout.strip()

def get_programs():
    """Returns a generator that yields the available executable programs"""
    programs = []
    os.environ['PATH'] += os.pathsep + os.getcwd()
    for p in os.environ['PATH'].split(os.pathsep):
        if path.isdir(p):
            for f in os.listdir(p):
                if _is_executable(path.join(p, f)):
                    yield f

def _underscore_run_program(name, *args, shell=False):
    if name in get_programs() or shell:
        return _run_program(name, shell, *args)
    else:
        raise ProgramNotFoundException()

def _refresh_listing():
    for f in get_programs():
        if re.match(r'^[a-zA-Z_][a-zA-Z_0-9]*$', f) is not None:
            globals()[f] = partial(_run_program,f, False)
    globals()["_"] = _underscore_run_program

_refresh_listing()
