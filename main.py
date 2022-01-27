import discord
from discord.ext.commands import Bot
import os
import csv
import pandas
import random
import dataframes
import randfuncs
import record
import commands

from keep_alive import keep_alive

bot = Bot(command_prefix = '!')
count = 0
repeat = False
josh_id = 518974960912564225
josh_ping = '<@!518974960912564225>'

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  activity = discord.Activity(name="YOU.", type=3)
  await bot.change_presence(status=discord.Status.idle, activity=activity)

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  await randfuncs.msg(bot, message)
  await randfuncs.react(bot, message)
  await randfuncs.keyw(bot, message)
  await record.rec(bot, message, repeat) 
  await bot.process_commands(message)

@bot.command(name = 'h')
async def h (ctx):
  await commands.h(bot, ctx)

@bot.command(name = 'troll')
async def troll (ctx):
  await commands.troll(bot, ctx)
  
@bot.command(name = 'ping')
async def ping (ctx):
  await commands.ping(bot, ctx)

@bot.command(name = 'quote')
async def quote (ctx):
  await commands.suggest(bot, ctx)

@bot.command(name = 'suggest')
async def suggest (ctx, *arg):
  await commands.suggest(bot, ctx, *arg)
  
# SCAN FUNCTION
@bot.command(name = 'scan')
async def scan (ctx):
  await commands.scan(bot, ctx)
    
keep_alive() 
bot.run(os.environ['token'])