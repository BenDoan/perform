#perform

A python module for easily running processes from python.

##Examples
```python
import perform

stdout, stderr = perform.ls()

print(perform.git("ls-files", "-m")[0])

print(perform._("pip2.7", "install", "perform"))

stdout, _ = perform.raspistill("-o ~/image.jpg")
```
