import os
import discord
import asyncio
import random
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands, tasks


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')
chat_id = 224809806299529217

hr = random.randint(6, 7)
mnt = random.randint(10, 59)
msg_time = '0' + str(hr) + ':' + str(mnt)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{bot.user} has connected to Discord!\n Guild: '
        f'{guild.name}(id: {guild.id})'
    )
    print(msg_time)

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send("дратути")

async def morning():
    await bot.wait_until_ready()
    message_channel = bot.get_channel(chat_id)

    while not bot.is_closed:
        time_now = datetime.strftime(datetime.utcnow(),'%H:%M')
        if time_now == msg_time:
            await message_channel.send("Доброе утро!")
            skip = 72000

            hr = random.randint(6, 7)
            mnt = random.randint(10, 59)
            msg_time = '0' + str(hr) + ':' + str(mnt)
            print(msg_time)
        else:
            skip = 1
        await asyncio.sleep(skip)


bot.run(TOKEN)