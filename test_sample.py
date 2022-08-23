import pytest as pytest


def fnname(x):
    return x + 1


def test_sample():
    assert fnname(7) == 8
