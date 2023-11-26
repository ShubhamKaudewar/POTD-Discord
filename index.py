import requests
from Resources import variables

header = {"authorization": variables.TOKEN}
from wikimedia.image import fetch_image
image_url = fetch_image()
# TODO: Need to send above image to the discord channel

# The picture that we want to send in binary
files = {"file": ("./picture.jpg", open("./picture.jpg", 'rb'))}

# Optional message to send with the picture
payload = {"content": "message"}

channel_id = "channel_id" # Channel where we send the picture

r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=header, files=files)