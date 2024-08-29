import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from hw1 import divide

def test_fail():
    assert divide(4, 5) == 2