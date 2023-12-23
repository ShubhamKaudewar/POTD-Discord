from requests import request
from resources.variables import ENDPOINT


def fetch_caption(pageid):
    ids = f'M{pageid}'
    url = ENDPOINT + f'?action=wbgetentities&format=json&ids={ids}&formatversion=2'

    response = request("GET", url, headers={}, data={})
    data = response.json()
    labels = data["entities"][ids]["labels"]
    default = data["entities"][ids]["title"]
    if labels == {} or "en" not in labels:
        return default
    return labels["en"]["value"]
