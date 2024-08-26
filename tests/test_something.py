import requests
from jsonschema import validate
from enums.global_enums import GlobalErrorMessages
from pydantic_schemas.post import Post


def test_getting_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200, GlobalErrorMessages
    received_posts = response.json()
    assert len(received_posts) == 100
    print(response.json()[0])
    response.assert_status_code(200).validate(Post)
