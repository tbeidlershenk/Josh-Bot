import discord
import csv
from discord.ext.commands import Bot
import os
import pandas
import random

import phrases
import dataframes

from keep_alive import keep_alive

bot = Bot(command_prefix = '!')
count = 0
mchance = 2
rchance = 2
kchance = 20
repeat = False
josh_id = 518974960912564225
josh_ping = '<@!518974960912564225>'
# READY FUNCTION

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  activity = discord.Activity(name="YOU.", type=3)
  await bot.change_presence(status=discord.Status.idle, activity=activity)


# ON MESSAGE FUNCTION

@bot.event
async def on_message(message):
  
  global count, mchance, rchance, repeat

  if message.author == bot.user:
    return
  elif (count > 10):
    mchance+=1
    rchance+=1
    count = 0

  if (random.randint(0,100) > 100-mchance):
    await message.channel.send(phrases.phrases[random.randint(0,len(phrases.phrases)-1)])
    mchance = 2

  for n in range (len(dataframes.triggers)):
    if dataframes.triggers.iloc[n,0] in message.content.upper():
      if (random.randint(0,100) > 100-kchance):
        await message.channel.send(dataframes.triggers.iloc[n,1])
  
  if (random.randint(0,100) > 100-rchance):
    await message.add_reaction('<:acme:925591518419484702>')
    rchance = 2

  if message.author.id == josh_id:
    fields=[len(pandas.read_csv('data/history.csv')), message.content, message.created_at, message.author]
    with open(r'data/history.csv', 'a') as f:
      writer = csv.writer(f)
      writer.writerow(fields)
    if repeat:
      await message.channel.send(message.content)
  
  count+=1
  await bot.process_commands(message)

# BOT COMMANDS

@bot.command(name = 'h')
async def h (ctx):
  s = '```Commands\n'
  for n in range (len(dataframes.commands)):
    s += (dataframes.commands.iloc[n,0] + ': ' + dataframes.commands.iloc[n,1] + '\n')
  s += '```'
  await ctx.send(s)

@bot.command(name = 'troll')
async def troll (ctx):
  global repeat
  if ctx.author.id != josh_id and not repeat:
    repeat = True
  elif ctx.author.id != josh_id and repeat:
    repeat = False
  
@bot.command(name = 'ping')
async def ping (ctx):
  await ctx.send(josh_id)

@bot.command(name = 'quote')
async def quote (ctx):
  data = pandas.read_csv('data/history.csv')
  rand = random.randint(0, len(data)-1)
  s = data.iloc[rand,2]
  await ctx.send(data.iloc[rand,1]+'\n**sent on:** ' + s[0:len(s)-7])

# SCAN FUNCTION
@bot.command(name = 'scan')
async def scan (ctx):
  print(ctx.author.id)
  if (ctx.author.id == 572796216589418528 and False): #cant run
    print(2)
    data = pandas.DataFrame(columns=['content', 'time', 'author'])
    count = 0
    async for msg in ctx.channel.history(limit=200000): 
      print(count)
      if msg.author.id == 518974960912564225:  
        if not msg.content.startswith('https'):                        
          data = data.append({'content': msg.content,
                                'time': msg.created_at,
                                'author': msg.author.name}, ignore_index=True)
          count+=1
        if len(data) == 30000:
          break
    print('done')
    data.to_csv('history.csv')
    
keep_alive() 
bot.run(os.environ['token'])
