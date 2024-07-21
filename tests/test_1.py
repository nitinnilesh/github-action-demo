import os, sys
sys.path.insert(0, os.getcwd())
from script import addition

def test_add():
    subj = addition(1, 2)
    assert subj == 3
    