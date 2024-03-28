import pytest
import yaml


def get_numbers_data(config_name):
    with open(config_name, 'r') as stream:
        config = yaml.safe_load(stream)
    return config['cases']


def add_numbers(a, b, c):
    try:
        return a + b + c
    except TypeError:
        raise 'Please check the parameters. All of them must be numeric'


def test_add_numbers():
    pass


def test_add_floats():
    a, b, c = 'a', 2, 1
    pass
