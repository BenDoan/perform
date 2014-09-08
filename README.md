Perform is for calling processes from python in a simple and easy way.  Each program is added to the perform module as a function that returns a tuple of (stdout, stdin).

##usage:
- To call a normal program that whose name doesn't contain symbols:

```python
import perform
stdin, stdout = perform.ls()
```

- To pass arguments to a program:

```python
import perform
stdout = perform.git("ls-files", "-m")[0]
```

- To call a program that contains symbols in its name:

```python
import perform
stdin, stdout = perform._("pip2.7", "install", "perform")
```

##more examples

```python
import perform

stdout, stderr = perform.ls()

print(perform.git("ls-files", "-m")[0])

print(perform._("pip2.7", "install", "perform"))

stdout, _ = perform.raspistill("-o ~/image.jpg")
```
