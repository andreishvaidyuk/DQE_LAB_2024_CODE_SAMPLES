import time
import pytest


@pytest.fixture()
def track_suite_time():
    pass


@pytest.fixture()
def track_test_time():
    pass


def add_numbers(a, b):
    return a + b


def test_add_two_positive_numbers():
    a, b = 3, 5
    result = add_numbers(a, b)
    time.sleep(2)
    assert result == 8


def test_add_two_negative_numbers():
    a, b = -3, -5
    result = add_numbers(a, b)
    time.sleep(3)
    assert result == -8


def test_add_negative_and_positive_numbers():
    a, b = -3, 5
    result = add_numbers(a, b)
    time.sleep(10)
    assert result == 2
