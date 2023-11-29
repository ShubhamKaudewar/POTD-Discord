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
    url = ENDPOINT + ("?action=query&format=json&prop=imageinfo&iiprop=url"
                      "&iiurlwidth=1600&iiurlheight=600&titles=") + title
    response = request("GET", url, headers={}, data={})
    response = response.json()
    print(response["query"]["pages"])
    image_page = list(response["query"]["pages"].values())[0]
    image_url = image_page["imageinfo"][0]["responsiveUrls"]["1.5"]
    image_page_id = image_page["pageid"]
    return_data = {
        "image_page_id": image_page_id,
        "image_url": image_url
    }
    return return_data


if __name__ == "__main__":
    # from datetime import date
    # cur_date = date.today()
    # date_iso = cur_date.isoformat()
    x = fetch_image()
    print(x)