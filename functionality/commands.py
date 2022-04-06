import discord
from discord.ext.commands import Bot

import os, csv, pandas, random

from functionality import randfuncs

from access import settings, dataframes

# displays commands formatted nicely
async def h(Bot, ctx):
    s = settings.command_header
    for n in range(len(dataframes.commands)):
        s += (dataframes.commands.iloc[n, 0] + ': ' +
              dataframes.commands.iloc[n, 1] + '\n')
    s += settings.format_footer
    await ctx.send(s)

# ping()
async def ping(Bot, ctx):
    await ctx.send(
        dataframes.ids.iloc[random.randint(0, len(dataframes.ids)), 0])

# quote()
async def quote(Bot, ctx):
    data = pandas.read_csv('data/history.csv')
    rand = random.randint(0, len(data) - 1)
    s = data.iloc[rand, 2]
    await ctx.send(data.iloc[rand, 1] + '\n**sent on:** ' + s[0:len(s) - 7])

# suggest()
async def suggest(Bot, ctx, *arg):
    if len(arg) == 0:
        await ctx.send(settings.suggest_message)
        return
    sen = ''
    for word in arg:
        sen += word + ' '
    fields = [sen]
    with open(r'data/suggestions.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

# reply()
async def reply(ctx):
    count = 0
    num = random.randint(0, 1000)
    async for msg in ctx.channel.history(limit=5000):
        if count > num:
            if (len(msg.content.split(' ')) > 10):
                list = msg.content.split(' ')
                s = ''
                for x in range (len(list)):
                    last = len(list)-x-1
                    ind = random.randint(0, last)
                    s += list[ind] + ' '
                    list[ind] = list[last]
                await msg.reply(s, mention_author = False)
                return
        count += 1

# scores()
async def scores(ctx):
    points = dataframes.points.sort_values(by='Score',
                                           ascending=False,
                                           inplace=True,
                                           kind='quicksort',
                                           na_position='last')
    s = settings.format_header
    for n in range(5):
        s += (str(dataframes.points.iloc[n, 0]) + ': ' +
              str(dataframes.points.iloc[n, 2]) + '\n')
    s += settings.format_footer
    await ctx.send(s)

# dist()
async def dist (ctx):
    s = settings.format_header
    for x in range (10):
        s += (str(dataframes.distr.iloc[x, 0]) + ': ' +
              str(dataframes.distr.iloc[x, 1]) + ' occurrences\n')
    s += settings.format_footer
    await ctx.send(s)

# freq()
async def freq (ctx, word):
  dist = dataframes.distr
  sent = False
  for x in range (len(dist)):
    if str(dist.iloc[x,0]) == word.lower():
      await ctx.send('Josh has said \"' + word + '\" ' + str(dist.iloc[x,1]) + ' times')
      sent = True
  if not sent:
    await ctx.send('Josh has said \"' + word + '\" ' +' 0 times')

# not needed anymore? don't delete tho
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
