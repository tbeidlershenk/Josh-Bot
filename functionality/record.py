import discord
from discord.ext.commands import Bot
from datetime import datetime

import csv, os, pandas, random

from access import dataframes, settings

# record josh's messages
async def rec (message):
  if message.author.id == settings.josh_id:
    
    # update 'data/history.csv'
    fields=[len(pandas.read_csv('data/history.csv')), message.content, message.created_at, message.author]
    with open(r'data/history.csv', 'a') as f:
      writer = csv.writer(f)
      writer.writerow(fields)

    # update 'data/distribution.csv'
    list = message.content.split(' ')    
    for word in list:
        new = True
        for y in range (len(dataframes.distr)):
            if (str(dataframes.distr.iloc[y,0]) == word.lower()):
                dataframes.distr.iloc[y,1] = int(dataframes.distr.iloc[y,1])+1
                new = False
                break
        if new:
            df = pandas.DataFrame({'word' : [word.lower()],'frequency' : ['1']})
            dataframes.distr =   pandas.concat([dataframes.distr, df], ignore_index = True, axis = 0)
    
    # return distr dataframe to 'data/distribution.csv'
    dataframes.distr.to_csv('data/distribution.csv', index = False)

# records gojopoints
async def gojopoints (message):
  
  # check if message has 'new pfp'
  b = 'NEW PFP' in message.content.upper()
  if not b:
    return

  now = datetime.now();
  c = False
  diff = now -datetime.strptime(dataframes.times.iloc[len(dataframes.times)-1,1],'%Y-%m-%d %H:%M:%S.%f')
  leng = len(str(diff))

  # slice the datetime object
  if (leng == 14):
    slice = int(str(diff)[0:1])
  if (leng == 15):
    slice = int(str(diff)[0:2])
  elif ('day' in str(diff)):
    stri = str(diff).split(',')[1][1:leng]
    print(stri)
    if (len(stri) == 14):
      slice = int(stri[0:1])
    else:
      slice = int(stri[0:2])
    c = True

  # add a point to the correct person 
  if (b and slice > 4) or (b and c):
    fields=[len(dataframes.times)-1,now]
    with open(r'data/time.csv', 'a') as f:
      writer = csv.writer(f)
      writer.writerow(fields)
      dataframes.times = pandas.read_csv('data/time.csv')
    length = len(dataframes.points.columns)-1
    for n in range(len(dataframes.points)-1):
      if dataframes.points.iloc[n,length-1] == str(message.author):
        dataframes.points.iloc[n,length] = int(dataframes.points.iloc[n,length])+1
        dataframes.points.to_csv('data/gojoscores.csv', index = False)
  
# update scores
async def update (message):
  scores = pandas.read_csv('data/scores.csv')
  scores.iloc[scores.loc(str(message.author))[0],2] = int(scores.iloc[scores.loc(str(message.author))[0],2])+1
  scores.to_csv('data/scores.csv')
  
  
    
    

