from requests import request
from resources.variables import ENDPOINT


def fetch_caption(pageid):
    ids = f'M{pageid}'
    url = ENDPOINT + f'?action=wbgetentities&format=json&ids={ids}&formatversion=2'

    response = request("GET", url, headers={}, data={})
    data = response.json()
    entity_id = data["entities"][ids]
    if "labels" in entity_id and entity_id["labels"] != {}:
        caption = data["entities"][ids]["labels"]["en"]["value"]
    else:
        return "None"
    return caption
