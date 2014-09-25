Perform is for calling processes from python in a simple and easy way.  Each program is added to the perform module as a function that returns the stdout printed by the program.

##usage:
- To call a normal program that whose name doesn't contain symbols:

```python
import perform
stdout = perform.ls()
```

- To pass arguments to a program:

```python
import perform
stdout = perform.git("ls-files", "-m")
```

- To call a program that contains symbols in its name:

```python
import perform
stdout = perform._("pip2.7", "install", "perform")
```

- To get stderr from a program:

```python
try:
    perform.git("asdad")
except Exception as e:
    print(str(e))
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
