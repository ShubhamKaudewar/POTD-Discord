from requests import request
from resources.variables import ENDPOINT
from wikimedia.title import fetch_title


def fetch_image():
    fetch_title_data = fetch_title()
    page_id = str(fetch_title_data["pageid"])
    print(page_id)
    title = fetch_title_data["title"]
    print(title)

    title = title.replace("&", "%26")
    url = ENDPOINT + "?action=query&format=json&prop=imageinfo&iiprop=url&titles=" + title
    response = request("GET", url, headers={}, data={})
    response = response.json()
    print(response["query"]["pages"])
    image_url = response["query"]["pages"]["74081238"]["imageinfo"][0]["url"]
    print(image_url)
    return image_url


if __name__ == "__main__":
    # from datetime import date
    # cur_date = date.today()
    # date_iso = cur_date.isoformat()
    x = fetch_image()
    print(x)