import requests


def mk_request(query):
    response = requests.get(query)
    return response.text
