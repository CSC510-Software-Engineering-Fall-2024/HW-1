import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from hw1 import divide

def test_pass():
    assert divide(5, 1) == 5