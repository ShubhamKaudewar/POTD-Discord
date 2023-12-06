from requests import request
from resources.variables import ENDPOINT


def fetch_potd_title():
    from datetime import date
    cur_date = date.today()
    date_iso = cur_date.isoformat()
    title = "Template:Potd/" + date_iso
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

def fetch_motd_title():
    from datetime import date
    cur_date = date.today()
    date_iso = cur_date.isoformat()
    title = "Template:Motd/" + date_iso
    url = ENDPOINT + ("?action=query&format=json&prop=revisions&formatversion=2"
                      "&rvprop=content&rvslots=main&titles=") + title

    response = request("GET", url, headers={}, data={})
    data = response.json()
    pages = data["query"]["pages"][0]
    pageid = pages["pageid"]
    wiki_title = pages["revisions"][0]["slots"]["main"]["content"]
    import wikitextparser as wtp
    title = wtp.parse(wiki_title).templates[0].arguments[0].value
    response = {
        "pageid": pageid,
        "title": title
    }
    return response

# def test():
#     import wikitextparser as wtp
#     title = "{{Motd filename|1=2023-05-08 commemo-Meroux.webm|2=2023|3=11|4=30}}"
#     parsed = wtp.parse(title)
#     x = parsed.templates[0].arguments[0].value
#     return x

# if __name__ == "__main__":
    # from datetime import date
    # cur_date = date.today()
    # date_iso = cur_date.isoformat()
    # x = test()
    # print(x)