from requests import request
from Resources.variables import ENDPOINT

url = ENDPOINT + "?action=query&format=json&prop=imageinfo&iiprop=url&titles=File:Long-crested eagle (Lophaetus occipitalis) 3.jpg"

payload = {}
headers = {
  'Cookie': 'WMF-Last-Access-Global=25-Nov-2023; WMF-Last-Access=25-Nov-2023; enwikiBlockID=14675105%21c32a1f79e2c70302b86474755e78359e47dec74eee8732be91eac3225a047ac43e4369487c6c8b10d8bdda45c8aaeb72bb61b8617327897e5d3af54b54c8e37f'
}

response = request("GET", url, headers=headers, data=payload)

print(response.text)
