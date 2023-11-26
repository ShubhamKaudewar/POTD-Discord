import requests
from .Resources import Vari
# User's Token
header = {
    'authorization': "MTE3ODE5NTM1NDg1Njk4NDYzNg.GF9mhF.rNUEb7kngwEcPQdzDBUXS4_JvHdWdb8ImpGWA0",
}

# File
files = {
    "file" : ("./picture.jpg", open("./picture.jpg", 'rb')) # The picture that we want to send in binary
}

# Optional message to send with the picture
payload = {
    "content":"message"
}

channel_id = "channel_id" # Channel where we send the picture

r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=header, files=files)