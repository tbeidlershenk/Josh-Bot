# main.py written by Tobias Beidler-Shenk
# on_ready()
    # sets bot activity
    # starts background task
# on_message()
    # runs functions from randfuncs.py
    # records messages josh's message to update files
    # processes commands (if necessary)
# commands specified here
# pings repl with keep_alive()

import discord
from discord.ext.commands import Bot
from datetime import datetime
from keep_alive import keep_alive

import os, csv, pandas, random, asyncio

from access import settings, dataframes
from functionality import background, commands, record, randfuncs

bot = Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    activity = discord.Activity(name="YOU.", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    bot.loop.create_task(background.background(bot))
      
@bot.event
async def on_message(message):

    # if msg from josh bot
    if message.author == bot.user:
        return

    # otherwise run the functions
    else:    
    
        # run random functions
        await randfuncs.msg(message)
        await randfuncs.react(message)
        await randfuncs.keyw(message)
        await randfuncs.typing(message)

        # run recording functions
        await record.rec(message)
        await record.gojopoints(message)
        await bot.process_commands(message)

# commands
@bot.command(name='h')
async def h(ctx):
    await commands.h(bot, ctx)

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

@bot.command(name='dist')
async def distribution(ctx):
    await commands.dist(ctx)

@bot.command(name='freq')
async def freq(ctx, arg):
    await commands.freq(ctx, arg)
    
@bot.command(name='scores')
async def scores(ctx):
    await commands.scores(ctx)

# scan function not used
@bot.command(name='scan')
async def scan(ctx):
    await commands.scan(bot, ctx)


# ping the repl
keep_alive()
bot.run(os.environ['TOKEN'])

