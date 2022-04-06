# randfuncs.py written by Tobias Beidler-Shenk
# This file specifies functions run on every message. These functions
# will output randomly.
# Current Functionality:
    # msg() sends random messages
    # react() reacts with random emote
    # keyw() sends a keyword based on message
    # typing() displays typing flair for a length of time
  
import discord
from discord.ext.commands import Bot

import csv, os, pandas, random, asyncio

from access import dataframes, settings

# send a random message from 'data/phrases.csv' 
async def msg (message):
  if (random.randint(0,100) > 100 - settings.msg_chance):
    await message.channel.send(dataframes.phrases.iloc[random.randint(0,len(dataframes.phrases)-1),0])
    print('random message')

# react with a random emote from 'data/emotes.csv' 
async def react (message):
  if (random.randint(0,100) > 100 - settings.react_chance):
    rand = random.randint(0,len(dataframes.emotes)-1)
    emote = dataframes.emotes.iloc[rand,0]
    await message.add_reaction(emote)
    print('reacted')

# send a keyword triggered by message.content from 'data/keywords.csv'
async def keyw (message):
  if (random.randint(0,100) > 100 - settings.keyw_chance):
    for n in range (len(dataframes.triggers)):
      if dataframes.triggers.iloc[n,0] in message.content.upper():
        await message.channel.send(dataframes.triggers.iloc[n,1])
        print('sent keyword')

# show typing flair in message.channel context
async def typing (message):
  if (random.randint(0, 100) > 100 - settings.typing_chance):
    async with channel.typing():
      await asyncio.sleep(settings.typing_time)

