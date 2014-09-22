from __future__ import unicode_literals

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
"""

import os
import re
import subprocess
import sys

from os import path
from functools import partial

__author__ = "Ben Doan <ben@bendoan.me>"
__version__ = "0.0.2"

def _is_executable(f):
    return path.isfile(f) and os.access(f, os.X_OK)

def _run_program(name, *args, **kwargs):
    args = [name] + list(args)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = tuple(x.decode(sys.getdefaultencoding()) for x in p.communicate())
    if stderr != "":
        raise Exception(stderr)
    return stdout

def get_programs():
    """Returns a generator that yields the available executable programs"""
    programs = []
    os.environ['PATH'] += os.pathsep + os.getcwd()
    for p in os.environ['PATH'].split(os.pathsep):
        if path.isdir(p):
            for f in os.listdir(p):
                if _is_executable(path.join(p, f)):
                    yield f

def _refresh_listing():
    for f in get_programs():
        if re.match(r'^[a-zA-Z_][a-zA-Z_0-9]*$', f) is not None:
            globals()[f] = partial(_run_program,f)
    globals()["_"] = lambda name, *args, **kwargs: _run_program(name, *args, **kwargs)

_refresh_listing()
