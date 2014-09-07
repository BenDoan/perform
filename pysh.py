import os
import subprocess
import sys

from os import path

def _is_executable(f):
    return path.isfile(f) and os.access(f, os.X_OK)

def _run_program(name, *args):
    args = [name] + list(args)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return [x.decode(sys.getdefaultencoding()) for x in p.communicate()]

def _get_function(name):
    return lambda *args: _run_program(name, *args)

def get_programs():
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
