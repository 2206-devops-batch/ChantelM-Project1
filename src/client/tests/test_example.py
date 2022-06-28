import sys
sys.path.append("../")

import app
import pytest

# https://docs.pytest.org/en/7.1.x/

def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5

