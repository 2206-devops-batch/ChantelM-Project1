# https://docs.pytest.org/en/7.1.x/
# flask testing with pytest: https://flask.palletsprojects.com/en/2.1.x/testing/

# pytest tests/

def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4

# def test_failure():
#     assert inc(3) == 5

