import discord
import csv
from discord.ext.commands import Bot
import os
import pandas
import random
import dataframes

async def msg (Bot, message):
  m = 2
  if (random.randint(0,100) > 100-m):
    await message.channel.send(dataframes.phrases.iloc[random.randint(0,len(dataframes.phrases)-1),0])
    print('random message')

async def react (Bot, message):
  r = 2
  if (random.randint(0,100) > 100-r):
    await message.add_reaction(dataframes.emotes.iloc[random.randint(0,len(dataframes.emotes)-1),0])
    print('reacted')

async def keyw (Bot, message):
  k = 20
  for n in range (len(dataframes.triggers)):
    if dataframes.triggers.iloc[n,0] in message.content.upper():
      if (random.randint(0,100) > 100-k):
        await message.channel.send(dataframes.triggers.iloc[n,1])
        print('sent keyword')

