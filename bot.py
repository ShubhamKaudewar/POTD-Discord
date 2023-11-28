
from resources.variables import TOKEN
from discord.ext import commands
import discord
import bot
from datetime import datetime, time, timedelta
import asyncio

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def trigger(channel_id):
    from wikimedia.image import fetch_image
    image_data = fetch_image()
    image_url = image_data.get("image_url")
    caption = image_data.get("caption")
    description = "## Today's Picture of The Day from Wikipedia \n\n" + caption

    channel = client.get_channel(channel_id)  # replace id
    from aiohttp import ClientSession
    async with ClientSession() as session:  # creates session
        async with session.get(image_url) as resp:  # gets image from url
            img = await resp.read()  # reads image from response
            from io import BytesIO
            with BytesIO(img) as file:  # converts to file-like object
                from discord import File
                await channel.send(description, file=File(file, "t.png"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$potd':
        channel_id = message.channel.id
        await trigger(channel_id)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

client.run(TOKEN)


# FIXME: Below function for schedular
# bot = commands.Bot(command_prefix="$")
# WHEN = time(18, 0, 0)
#
# async def called_once_a_day():  # Fired every day
#     await bot.wait_until_ready()  # Make sure your guild cache is ready so the channel can be found via get_channel
#     await trigger()
#
#
# async def background_task():
#     now = datetime.utcnow()
#     if now.time() > WHEN:  # Make sure loop doesn't start after {WHEN} as then it will send immediately the first time as negative seconds will make the sleep yield instantly
#         tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
#         seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
#         await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start
#     while True:
#         now = datetime.utcnow() # You can do now() or a specific timezone if that matters, but I'll leave it with utcnow
#         target_time = datetime.combine(now.date(), WHEN)  # 6:00 PM today (In UTC)
#         seconds_until_target = (target_time - now).total_seconds()
#         await asyncio.sleep(seconds_until_target)  # Sleep until we hit the target time
#         await called_once_a_day()  # Call the helper function that sends the message
#         tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
#         seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
#         await asyncio.sleep(seconds)
#
# if __name__ == "__main__":
#     bot.loop.create_task(background_task())
#     bot.run(TOKEN)

