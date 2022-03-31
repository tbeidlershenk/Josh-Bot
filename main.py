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
from datetime import datetime
import threading
import asyncio

from keep_alive import keep_alive

bot = Bot(command_prefix='!')
count = 0
repeat = False
josh_id = 518974960912564225
josh_ping = '<@!518974960912564225>'


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    activity = discord.Activity(name="YOU.", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    bot.loop.create_task(background())

async def background():
    await bot.wait_until_ready()
    channel = bot.get_channel(935366855827271693)
    while not bot.is_closed():
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print("Current Time =", time)
        if (time == '04:00:00'):
            await channel.send('https://tenor.com/view/sweet-dreams-good-night-flowers-neon-gif-22768044')
            await channel.send('Goodnight ' + '<@518974960912564225>')
        await asyncio.sleep(1) # task runs every 60 seconds
      
def send(channel):
    channel.send('https://tenor.com/view/sweet-dreams-good-night-flowers-neon-gif-22768044'+'\nGoodnight ' + '<@518974960912564225>')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await randfuncs.msg(bot, message)
    await randfuncs.react(bot, message)
    await randfuncs.keyw(bot, message)
    await record.rec(bot, message, repeat)
    await record.gojopoints(message)
    await bot.process_commands(message)


@bot.command(name='h')
async def h(ctx):
    await commands.h(bot, ctx)


@bot.command(name='troll')
async def troll(ctx):
    await commands.troll(bot, ctx)


@bot.command(name='ping')
async def ping(ctx):
    await commands.ping(bot, ctx)


@bot.command(name='quote')
async def quote(ctx):
    await commands.quote(bot, ctx)

@bot.command(name='reply')
async def reply(ctx):
    await commands.reply(ctx)

@bot.command(name='suggest')
async def suggest(ctx, *arg):
    await commands.suggest(bot, ctx, *arg)


# SCAN FUNCTION
@bot.command(name='scan')
async def scan(ctx):
    await commands.scan(bot, ctx)


@bot.command(name='test')
async def test(ctx):
    for member in ctx.guild:
        print(member.id)

    pass


@bot.command(name='scores')
async def scores(ctx):
    await commands.scores(ctx)


keep_alive()
bot.run(os.environ['token'])
