import discord
import csv
from discord.ext.commands import Bot
import os
import pandas
import random
import dataframes
from datetime import datetime

josh_id = 518974960912564225
lastpfp = datetime.now()
#time = dataframes.times.iloc[len-1,1]
#lastpfp = datetime.strptime(time, 'YYYY-MM-DDTHH:MM:SS.mmmmmm')
#lastpfp = datetime.strptime(dataframes.times.iloc[0,0], '%d-%m-%Y %H:%M:%S')

async def rec (Bot, message, repeat):
  if message.author.id == josh_id:
    fields=[len(pandas.read_csv('data/history.csv')), message.content, message.created_at, message.author]
    with open(r'data/history.csv', 'a') as f:
      writer = csv.writer(f)
      writer.writerow(fields)
    if repeat:
      await message.channel.send(message.content)

async def gojopoints (message):
  print(dataframes.times.iloc[len(dataframes.times)-1,1])
  now = datetime.now();
  diff = now -datetime.strptime(dataframes.times.iloc[len(dataframes.times)-1,1],'%Y-%m-%d %H:%M:%S.%f')
  slice = int(str(diff)[0:1])
  if (len(str(diff)) == 15):
    slice = int(str(diff)[0:2])

  b = 'new pfp' in message.content
  print(b)
  if b and slice > 4:
    print(True)
    fields=[len(dataframes.times)-1,now]
    with open(r'data/time.csv', 'a') as f:
      writer = csv.writer(f)
      writer.writerow(fields)
      dataframes.times = pandas.read_csv('data/time.csv')
    for n in range(len(dataframes.points)-1):
      if dataframes.points.iloc[n,1] == str(message.author):
        dataframes.points.iloc[n,2] = int(dataframes.points.iloc[n,2])+1
        dataframes.points.to_csv('data/gojoscores.csv')
        print('here')



  else: 
    print(diff)
    print(slice)
    print(False)
  
async def update (Bot, message):
  scores = pandas.read_csv('data/scores.csv')
  scores.iloc[scores.loc(str(message.author))[0],2] = int(scores.iloc[scores.loc(str(message.author))[0],2])+1
  scores.to_csv('data/scores.csv')
  

    
    

