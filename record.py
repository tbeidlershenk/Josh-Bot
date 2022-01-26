import discord
import csv
from discord.ext.commands import Bot
import os
import pandas
import random
import dataframes

josh_id = 518974960912564225

async def rec (Bot, message, repeat):
  if message.author.id == josh_id:
    fields=[len(pandas.read_csv('data/history.csv')), message.content, message.created_at, message.author]
    with open(r'data/history.csv', 'a') as f:
      writer = csv.writer(f)
      writer.writerow(fields)
    if repeat:
      await message.channel.send(message.content)