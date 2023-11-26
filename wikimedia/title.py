from requests import request
from Resources.variables import ENDPOINT


def fetch_title(cur_date):
    if cur_date == "":
        from datetime import date
        cur_date = date.today()
        date_iso = cur_date.isoformat()
    else:
        date_iso = cur_date
    title = "Template:POTD protected/" + date_iso
    url = ENDPOINT + "?action=query&format=json&formatversion=2&prop=images&titles=" + title

    response = request("GET", url, headers={}, data={})
    data = response.json()
    pageid = data["query"]["pages"][0]["pageid"]
    title = data["query"]["pages"][0]["images"][0]["title"]
    response = {
        "pageid": pageid,
        "title": title
    }
    return response


# if __name__ == "__main__":
#     from datetime import date
#     cur_date = date.today()
#     date_iso = cur_date.isoformat()
#     x = fetch_title(date_iso)
#     print(x)