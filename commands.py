import discord
import csv
from discord.ext.commands import Bot
import os
import pandas
import random
import dataframes
import randfuncs

count = 0
repeat = False
josh_id = 518974960912564225
josh_ping = '<@!518974960912564225>'


async def h(Bot, ctx):
    s = '```Commands\n'
    for n in range(len(dataframes.commands)):
        s += (dataframes.commands.iloc[n, 0] + ': ' +
              dataframes.commands.iloc[n, 1] + '\n')
    s += '```'
    await ctx.send(s)


async def troll(Bot, ctx):
    global repeat
    if ctx.author.id != josh_id and not repeat:
        repeat = True
    elif ctx.author.id != josh_id and repeat:
        repeat = False


async def ping(Bot, ctx):
    await ctx.send(
        dataframes.pings.iloc[random.randint(0, len(dataframes.pings)), 0])


async def quote(Bot, ctx):
    data = pandas.read_csv('data/history.csv')
    rand = random.randint(0, len(data) - 1)
    s = data.iloc[rand, 2]
    await ctx.send(data.iloc[rand, 1] + '\n**sent on:** ' + s[0:len(s) - 7])


async def suggest(Bot, ctx, *arg):
    if len(arg) == 0:
        await ctx.send('enter a phrase after !suggest')
        return
    sen = ''
    for word in arg:
        sen += word + ' '
    fields = [sen]
    with open(r'data/suggestions.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

async def reply(ctx):
    count = 0
    num = random.randint(0,500)
    async for msg in ctx.channel.history(limit=5000):
        print(count)
        if count == num:
            id = str(msg.author.id)
            await msg.reply('<@'+id+'>')
            return
        count+=1

async def scores(ctx):
    print(dataframes.points)
    points = dataframes.points.sort_values(by='Score',
                                           ascending=False,
                                           inplace=True,
                                           kind='quicksort',
                                           na_position='last')
    print(dataframes.points)

    s = '```Scores\n'
    for n in range(5):
        s += (str(dataframes.points.iloc[n, 0]) + ': ' +
              str(dataframes.points.iloc[n, 2]) + '\n')

    s += '```'
    await ctx.send(s)


async def scan(Bot, ctx):
    print(ctx.author.id)
    if (ctx.author.id == 572796216589418528 and False):  #cant run
        print(2)
        data = pandas.DataFrame(columns=['content', 'time', 'author'])
        count = 0
        async for msg in ctx.channel.history(limit=200000):
            print(count)
            if msg.author.id == 518974960912564225:
                if not msg.content.startswith('https'):
                    data = data.append(
                        {
                            'content': msg.content,
                            'time': msg.created_at,
                            'author': msg.author.name
                        },
                        ignore_index=True)
                    count += 1
                if len(data) == 30000:
                    break
        print('done')
        data.to_csv('history.csv')
