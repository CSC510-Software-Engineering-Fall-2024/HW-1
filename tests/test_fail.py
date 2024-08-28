import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from hw1 import divide

def divide_pass():
    assert divide(4, 2) == 2