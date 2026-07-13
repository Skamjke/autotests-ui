import pytest


@pytest.mark.skip(reason="Фича не включена")
def test_regression_case():
    ...
@pytest.mark.xfail
class TestSuit:
    def test_case1(self):
        assert 2==2
    def test_case2(self):
        ...
