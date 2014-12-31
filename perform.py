"""
Perform is a python module for calling processes in a simple and easy way.  Each program is added to the perform module as a function that returns the stdout printed by the program.

##usage:
- To call a program:

```python
import perform
stdout = perform.ls()
```

- To pass arguments to a program:

```python
stdout = perform.git("ls-files", "-m")
```

- To call a program that contains symbols in its name:

```python
stdout = perform._("pip2.7", "install", "perform")
```

- To get extra information from a program:

```python
command_object = perform.ls(return_object=True)

stdout = command_object.stdout
stderr = command_object.stderr
stdout = command_object.stdout
```

- To call a command in the shell:

```python
print(perform._("ls | grep 'py'", shell=True))
```

##more examples

```python
import perform

stdout = perform.ls()

print(perform.git("ls-files", "-m"))

print(perform._("pip2.7", "install", "perform"))

stdout = perform.raspistill("-o ~/image.jpg")

print(perform.python("-c", "import perform;print(perform.echo('hello'))")
```
"""
from __future__ import unicode_literals

import os
import re
import subprocess
import sys
import doctest

from os import path
from functools import partial

__author__ = "Ben Doan <ben@bendoan.me>"
__version__ = "0.0.6"

class StandardErrorException(Exception):
    pass

class ProgramNotFoundException(Exception):
    pass

class CommandOutput():
    def __init__(self, stdout, stderr, errcode):
        self.stdout = stdout
        self.stderr = stderr
        self.errcode = errcode

    def __str__(self):
        return self.stdout

def _is_executable(f):
    return path.isfile(f) and os.access(f, os.X_OK)

def _run_program(name, *args, **kwargs):

    shell = kwargs.get("shell", False)
    return_object = kwargs.get("return_object", False)

    args = [name] + list(args)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=shell)

    stdout, stderr = tuple(x.decode(sys.getdefaultencoding()).strip() for x in p.communicate())


    if return_object:
        return CommandOutput(stdout, stderr, p.returncode)
    else:
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

def _underscore_run_program(name, *args, **kwargs):
    """Runs the 'name' program, use this if there are illegal python method characters in the program name

    >>> _underscore_run_program("echo", "Hello")
    'Hello'
    >>> _underscore_run_program("echo", "Hello", return_object=True).stdout
    'Hello'
    """
    if name in get_programs() or kwargs.get("shell", False):
        return _run_program(name, *args, **kwargs)
    else:
        raise ProgramNotFoundException()

def _refresh_listing():
    for program in get_programs():
        if re.match(r'^[a-zA-Z_][a-zA-Z_0-9]*$', program) is not None:
            globals()[program] = partial(_run_program, program,
                                    shell=False, return_object=False)

    globals()["_"] = _underscore_run_program

_refresh_listing()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
