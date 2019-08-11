import requests

address = "https://yandex.ru/search/?"
region = "lr=2&"
query_start = "text="


def mk_request(query):
    q = address + region + query_start + "%20".join(query.split())
    response = requests.get(q)
    return response.text
