import pytest

class Test:
    @pytest.fixture(scope='class', autouse=True)
    def setup(self):
        print("Setting up tests...")

    def test_pass(self):
        assert True

    def test_fail(self):
        assert False