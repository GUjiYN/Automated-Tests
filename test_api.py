# test_api.py
import requests


# 使用免费的测试API（JSONPlaceholder）
def test_get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_post():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )
    assert response.status_code == 201
    assert response.json()["id"] == 101  # 该测试API会返回固定ID
