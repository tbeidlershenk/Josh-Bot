# background.py written by Tobias Beidler-Shenk
# This file specifies a background function that begins running on bot login.
# The function runs at time intervals specified in settings.py.
# Current functionality: 
    # goodnight message (thats it right now)
    
import discord
from discord.ext.commands import Bot
from datetime import datetime

import asyncio

from access import settings

async def background(bot):
    
    await bot.wait_until_ready()
    channel = bot.get_channel(settings.general)
    
    while not bot.is_closed():
        
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        
        # send gn message
        if (time == settings.say_gn):
            await channel.send(settings.gn_gif)
            await channel.send(settings.gn_msg)
        await asyncio.sleep(settings.frequency)

        # add more tasks...