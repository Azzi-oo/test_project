import pytest
from random import randrange


@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)

def calculate(a, b):
    return a + b


@pytest.fixture
def calculate():
    return calculate


@pytest.fixture
def make_number():
    number = randrange(1, 100, 5)
    yield number
    print(f'Number at home {number}')
