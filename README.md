Perform is a python module for calling processes in a simple and easy way.  Each program is added to the perform module as a function that returns the stdout printed by the program.

##Usage
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
obj = perform.ls(return_object=True) # or perform.ls(ro=True)

stdout = obj.stdout
stderr = obj.stderr
errcode = obj.errcode
```

- To call a command in the shell:

```python
print(perform._("ls | grep 'py'", shell=True))
```

- To import a specific command:

```python
from perform import ls

print(ls("-a"))
```

- To use perform for a non-blocking call:

```python
perform.firefox("google.com", no_return=True)
perform.firefox("github.com", no_return=True)
perform.firefox("kernel.org", nr=True)
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
