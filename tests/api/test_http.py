import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Response is {r.text}")

#@pytest.mark.http
#def test_second_request():
#    r = requests.get('https://api.github.com/users/defunkt')
#    print(f"Response Body is {r.json()}")
#    assert r.status_code == 200
#    print(f"Response Status code is {r.status_code}")
#    print(f"Response Headers are {r.headers}")

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
#   assert headers['Server'] == 'GitHub.com'
    assert headers['Server'].lower() == 'github.com'
    print(headers['Server'])


@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')

    assert r.status_code == 404