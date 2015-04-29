import subprocess

def buildup():
     subprocess.call("sudo apt-get install curl -y", shell=True)
     subprocess.call("sudo apt-get install python -y", shell=True)
     subprocess.call("sudo apt-get install python-dev -y", shell=True)
     subprocess.call("sudo apt-get install build-essential -y", shell=True)
     subprocess.call("sudo apt-get install libffi-dev -y", shell=True)
     subprocess.call("sudo apt-get install git -y", shell=True)
     subprocess.call("curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python", shell=True)

class TestRun(unittest.TestCase):

    def test_run(self):
        buildup()
        """Test to see if it even runs."""
        try:
            subprocess.call("python main.py", shell=True)
            pass
        except:
            assert False
