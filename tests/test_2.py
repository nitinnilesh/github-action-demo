import os, sys
sys.path.insert(0, os.getcwd())

from script import addition

def test_data_type():
    subj = addition(1, 2)
    assert type(subj) == int

    