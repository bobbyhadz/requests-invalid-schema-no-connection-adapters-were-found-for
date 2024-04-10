# Python Requests: No connection adapters were found for

import requests


def make_request():
    # ✅ the URL is now a string
    url = 'https://jsonplaceholder.typicode.com/posts'

    res = requests.get(url, timeout=10)

    parsed = res.json()
    print(parsed)


# ✅ Works
make_request()
