import requests

address = "https://yandex.ru/search/xml?"
user = "user=miles-tyoma&"
key = "key=03.334692089:b5b41d08ab68a718fadcdc649de6a553&"
query_start = "query="
query_fin = "&"
language = "l10n=ru&"
sort = "sortby=rlv&"
filtration = "filter=none&"
groups = "groupby=attr%3D%22%22.mode%3Dflat.groups-on-page%3D10.docs-in-group%3D1"


def mk_request(query):
    q = address + user + key + query_start + "+".join(query.split()) + query_fin + language + sort + filtration + groups
    response = requests.get(q)
    return response.json()
