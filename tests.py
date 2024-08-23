import pytest
from hw1 import divide

X = 10
Y = 2
Z = 5
class Test:
    @pytest.fixture(scope='class', autouse=True)
    def setup(self):
        print('INITAILIZING')

    def test_pass(self):
        assert divide(X, Y) == 5

    def test_fail(self):
        assert divide(X, Z) > 1