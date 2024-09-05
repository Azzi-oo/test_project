import pytest
import requests
from jsonschema import validate
from baseclasses.response import Response
from enums.global_enums import GlobalErrorMessages
from pydantic_schemas.post import Post
from tests.users.conftest import calculate

resp = requests.get('https://jsonplaceholder.typicode.com/posts')


def testing_getting_list():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    test_object = Response(response)
    test_object.assert_status_code(200)
# def test_getting_posts():
#     response = requests.get('https://jsonplaceholder.typicode.com/posts')
#     assert response.status_code == 200, GlobalErrorMessages
#     received_posts = response.json()
#     assert len(received_posts) == 100
#     print(response.json()[0])
#     response.assert_status_code(200).validate(Post)


@pytest.mark.production
@pytest.mark.skip('[ISSUE-23424] Issue with network connection')
def test_another():
    assert 1 == 1


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
])
def test_calculator(first_value, second_value, result):
    assert calculate(first_value, second_value) == result
