

from os import getenv
from dotenv import load_dotenv
load_dotenv()

from discord import Client, Intents
client = Client(intents=Intents.default())

# setting trigger time
from datetime import time, timezone
utc = timezone.utc
trigger_time = time(hour=5, minute=30, tzinfo=utc)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    trigger_wotd.start()
    trigger_potd.start()


from discord.ext import tasks
@tasks.loop(time=trigger_time)
async def trigger_potd():
    from wikimedia.image import fetch_image
    image_data = fetch_image()
    image_url = image_data.get("image_url")
    image_page_id = image_data.get("image_page_id")
    from wikimedia.caption import fetch_caption
    caption = fetch_caption(image_page_id)
    description = "**Wikimedia Commons: Picture of the day** \n\n## _*" + caption + "*_"

    channel = client.get_channel(int(getenv("POTD_CHANNEL")))
    from aiohttp import ClientSession
    async with ClientSession() as session:  # creates session
        async with session.get(image_url) as resp:  # gets image from url
            img = await resp.read()  # reads image from response
            from io import BytesIO
            with BytesIO(img) as file:  # converts to file-like object
                print(file.__sizeof__())
                from discord import File
                await channel.send(description, file=File(file, "t.png"))


@tasks.loop(time=trigger_time)
async def trigger_wotd():
    from wordnik.word import WordNik
    channel = client.get_channel((int(getenv("WOTD_CHANNEL"))))
    from datetime import date, datetime
    cur_date = date.today()
    date_iso = cur_date.isoformat()
    word_text = WordNik().get_WOTD(date_iso)

    x_date = datetime.now()
    today = x_date.strftime("%A,%d %B, %Y")
    caption = f'WordNik API Present: Word of the day [{today}]\n{word_text}'
    await channel.send(caption)

client.run(getenv("BOT_TOKEN"))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     if message.content == '$potd':
#         channel_id = message.channel.id
#         await trigger(channel_id)
#     elif message.content == '$wotd':
#         channel_id = message.channel.id
#         await trigger_wotd(channel_id)
#     elif message.content == 'raise-exception':
#         raise discord.DiscordException


