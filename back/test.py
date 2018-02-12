import requests

import pytest


@pytest.fixture
def exemple_html():
    r = requests.get('https://www.google.fr/')
    return r.status_code


def test_status_code(exemple_html):
    assert exemple_html == 200
