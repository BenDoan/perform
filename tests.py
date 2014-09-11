import unittest
import perform

TEST_DIR = "testdir"
MOVE_DIR = "movedir"
NUM_FILES = 1000 #should be even

class TestCat(unittest.TestCase):
    def test_cat(self):
        "".join(open("tests.py", "r").readlines()) == perform.cat("tests.py")

if __name__ == '__main__':
    unittest.main()
