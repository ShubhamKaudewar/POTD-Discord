from requests import request
from resources.variables import ENDPOINT
from wikimedia.title import fetch_motd_title


def fetch_video():
    fetch_title_data = fetch_motd_title()
    page_id = str(fetch_title_data["pageid"])
    print(page_id)
    title = fetch_title_data["title"]
    print(title)

    title = title.replace("&", "%26").replace(" ", "%20")
    url = ENDPOINT + ("?action=query&format=json&prop=videoinfo"
                      "&viprop=derivatives&formatversion=2&titles=File:") + title
    response = request("GET", url, headers={}, data={})
    response = response.json()
    print(response["query"]["pages"])
    video_page = response["query"]["pages"][0]
    video_url = video_page["videoinfo"][0]["derivatives"][0]["src"]
    video_page_id = video_page["pageid"]
    return_data = {
        "video_page_id": video_page_id,
        "video_url": video_url
    }
    return return_data


if __name__ == "__main__":
    # from datetime import date
    # cur_date = date.today()
    # date_iso = cur_date.isoformat()
    x = fetch_image()
    print(x)