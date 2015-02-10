import os
import random
import stat
import unittest

import perform

class TestPerform(unittest.TestCase):
    BAD_LS_OUTPUT = "ls: invalid option -- '5'\nTry 'ls --help' for more information."

    def test_cat(self):
        with open("perform_test.py", "r") as f:
            self.assertEqual("".join(f.readlines()).strip(), perform.cat("perform_test.py"))

    def test_echo(self):
        self.assertEqual("Hello", perform.echo("Hello"))

    def test_local_exe(self):
        name = "deletemea2329f80396e11e495fd5c514f635c22"
        echo_program = '#!/usr/bin/bash\necho "Hello!"\n'

        with open(name, "w") as f:
            f.write(echo_program)

        st = os.stat(name)
        os.chmod(name, st.st_mode | stat.S_IEXEC)

        perform._refresh_listing()

        try:
            self.assertEqual(perform.deletemea2329f80396e11e495fd5c514f635c22(), "Hello!")
        finally:
            os.remove(name)

    def test_underscore(self):
        self.assertEqual("Hello all", perform._("echo", 'Hello all'))

    def test_underscore_shell(self):
        self.assertEqual(perform._("echo 'hello\nworld' | tac", shell=True), 'world\nhello')

    def test_return_object(self):
        self.assertEqual(perform.echo("Hello", return_object=True).stdout, "Hello")

        self.assertEqual(perform.ls("-5", return_object=True).stderr, self.BAD_LS_OUTPUT)

        self.assertEqual(perform.echo("Hello", return_object=True).errcode, 0)
        self.assertEqual(perform.ls("-5", return_object=True).errcode, 2)

        self.assertEqual(perform.echo("Hello", ro=True).stdout, "Hello")

    def test_single_import(self):
        from perform import echo
        self.assertEqual(echo("Hello"), "Hello")

    def test_return_object_underscore(self):
        self.assertEqual(perform._("echo", "hello", "world", return_object=True).stdout, "hello world")
        self.assertEqual(perform._("echo", "-E", r"hello\thello", return_object=True).stdout, r"hello\thello")

    def test_no_return(self):
        #no_return allows for non-blocking calls, so
        #this tests those as well
        perform.yes(no_return=True)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
