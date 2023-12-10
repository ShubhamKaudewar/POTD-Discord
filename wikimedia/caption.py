from requests import request
from resources.variables import ENDPOINT


def fetch_caption(pageid):
    ids = f'M{pageid}'
    url = ENDPOINT + f'?action=wbgetentities&format=json&ids={ids}&formatversion=2'

    response = request("GET", url, headers={}, data={})
    data = response.json()
    labels = data["entities"][ids]["labels"]
    if labels == {}:
        caption = data["entities"][ids]["title"]
    else:
        caption = data["entities"][ids]["labels"]["en"]["value"]
    return caption
