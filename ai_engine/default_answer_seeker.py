import requests


def mk_request_in_yandex(q):
    address = "https://yandex.ru/search/?"
    region = "lr=2&"
    query_start = "text="
    query = address + region + query_start + "%20".join(q.split())

    return mk_request(query)


def mk_request(query):
    response = requests.get(query)
    return response.text
