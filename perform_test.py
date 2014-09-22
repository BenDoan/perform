import os
import random
import stat
import unittest

import perform

class TestPerform(unittest.TestCase):
    def test_cat(self):
        with open("test.py", "r") as f:
            self.assertEqual("".join(f.readlines()), perform.cat("test.py"))

    def test_echo(self):
        self.assertEqual("Hello\n", perform.echo("Hello"))

    def test_error_ls(self):
        try:
            perform.ls("-5")
        except Exception as e:
            self.assertEqual("ls: invalid option -- '5'\nTry 'ls --help' for more information.\n", str(e))

    def test_local_exe(self):
        name = "deletemea2329f80396e11e495fd5c514f635c22"
        echo_program = '#!/usr/bin/bash\necho "Hello!"'

        with open(name, "w") as f:
            f.write(echo_program)

        st = os.stat(name)
        os.chmod(name, st.st_mode | stat.S_IEXEC)

        perform._refresh_listing()

        try:
            self.assertEqual(perform.deletemea2329f80396e11e495fd5c514f635c22(), "Hello!\n")
        finally:
            os.remove(name)

    def test_underscore(self):
        self.assertEqual("Hello all\n", perform._("echo", 'Hello all'))

if __name__ == '__main__':
    unittest.main()
