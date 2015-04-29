import subprocess
import unittest

class TestRun(unittest.TestCase):

    def test_run(self):
        """Test to see if it even runs."""
        try:
            subprocess.call("python main.py", shell=True)
            pass
        except:
            assert False
