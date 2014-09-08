pysh
====

A python module for easily running processes from python

#Examples

    import pysh
    stdout, stderr = pysh.ls()
    print(pysh.git("ls-files", "-m")[0])
    print(pysh._("pip2.7", "install", "pysh"))

    stdout, _ = pysh.raspistill("-o ~/image.jpg")
