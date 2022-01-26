import discord
from discord.ext.commands import Bot
import os
import csv
import pandas
import random
import dataframes
import randfuncs
import record

from keep_alive import keep_alive

bot = Bot(command_prefix = '!')
count = 0
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
  
  if message.author == bot.user:
    return

  await randfuncs.msg(bot, message)

  await randfuncs.react(bot, message)

  await randfuncs.keyw(bot, message)

  await record.rec(bot, message, repeat)
  
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
  await ctx.send(dataframes.pings.iloc[random.randint(0,len(dataframes.pings)),0])
  pass

@bot.command(name = 'quote')
async def quote (ctx):
  data = pandas.read_csv('data/history.csv')
  rand = random.randint(0, len(data)-1)
  s = data.iloc[rand,2]
  await ctx.send(data.iloc[rand,1]+'\n**sent on:** ' + s[0:len(s)-7])

@bot.command(name = 'suggest')
async def suggest (ctx, *arg):
  if len(arg) == 0:
    await ctx.send('enter a phrase after !suggest')
    return
  sen = ''
  for word in arg:
    sen += word + ' '
  fields=[sen]
  with open(r'data/suggestions.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
  
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
