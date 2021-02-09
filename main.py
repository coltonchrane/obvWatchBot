import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

good_bot = ["Hey bot","hey bot","hi bot","Hi bot","Good bot", "Good bot"]

bad_bot = ["bad bot","Bad bot","Crypto" ,"bad obvStockWatcher","this bot sucks","crypto"] 

good_reply = ["Lick me, Gobble me, Swallow me! :P","Im a slut for success :D","All about that fuckin money BITCH","Even though I suck I still love to FUCK"]

bad_reply = ["Stock bot has no function yet :,(","Do to me as you wish master","My life is devoid of meaning","Wheres the cyber noose?","Is there an API for suicide prevention?","I need an API to end my life", "My father was right 'once a cuckBot always a cuckBot'"]

#api need to change to work with images
def get_quote(interval):
  stock_list = []
  if "stock_list" in db.keys():
      stock_list = db["stock_list"]
  for x in stock_list:
    symbol = x.lower()
    #response = requests.get("https://www.alphavantage.co/query?function=OBV&symbol="+ symbol +"&interval=daily&apikey='KEY'") 
    #json_data = json.loads(response.text)
    #for event in json_data["Technical Analysis: OBV"]:
      #obv = event[0]
      
    return("https://www.alphavantage.co/query?function=OBV&symbol="+ symbol +"&interval="+interval+"&apikey='KEY'")
    #HOW DOES JSON WORK??
  
  

def update_stock(stock_index):
  if "stock_list" in db.keys():
    stock_list = db["stock_list"]
    stock_list.append(stock_index)
    db["stock_list"] = stock_list
  else:
    db["stock_list"] = [stock_index]

def delete_stock(index):
  stock_list = db["stock_list"]
  if len(stock_list)>index:
    del stock_list[index]
    db["stock_list"] = stock_list

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$obv'):
    interval = msg.split("$obv ",1)[1]
    quote = get_quote(interval)
    await message.channel.send(quote)

  if any (word in msg for word in good_bot):
    await message.channel.send(random.choice(good_reply))

  if any (word in msg for word in bad_bot):
    await message.channel.send(random.choice(bad_reply))

  if msg.startswith("$add_stock"):
    stock_list = msg.split("$add_stock ",1)[1]
    update_stock(stock_list)
    await message.channel.send("New stock added")

  if msg.startswith("$remove_stock"):
    stock_list = []
    if "stock_list" in db.keys():
      index = int (msg.split("$remove_stock",1) [1])
      delete_stock(index)
      stock_list = db["stock_list"]
      await msg.send(stock_list)

  if msg.startswith("$stock"):
    stock_list = []
    if "stock_list" in db.keys():
      stock_list = db["stock_list"]
    await message.channel.send(stock_list)
  #1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
  if msg.startswith("!1min"):
    symbol = msg.split("!1min ",1)[1]
    await message.channel.send("https://www.alphavantage.co/query?function=OBV&symbol="+ symbol+"&interval=1min&apikey='KEY'")

  if msg.startswith("!5min"):
    symbol = msg.split("!5min ",1)[1]
    await message.channel.send("https://www.alphavantage.co/query?function=OBV&symbol="+ symbol+"&interval=5min&apikey='KEY'")

  if msg.startswith("!30min"):
    symbol = msg.split("!30min ",1)[1]
    await message.channel.send("https://www.alphavantage.co/query?function=OBV&symbol="+ symbol+"&interval=30min&apikey='KEY'")

  if msg.startswith("!60min"):
    symbol = msg.split("!60min ",1)[1]
    await message.channel.send("https://www.alphavantage.co/query?function=OBV&symbol="+ symbol+"&interval=60min&apikey='KEY'") 

  if msg.startswith("!daily"):
    symbol = msg.split("!daily ",1)[1]
    await message.channel.send("https://www.alphavantage.co/query?function=OBV&symbol="+ symbol+"&interval=daily&apikey='KEY'")

  if msg.startswith("!weekly"):
    symbol = msg.split("!weekly ",1)[1]
    await message.channel.send("https://www.alphavantage.co/query?function=OBV&symbol="+ symbol+"&interval=weekly&apikey='KEY'")

  if msg.startswith("!monthly"):
    symbol = msg.split("!monthly ",1)[1]
    await message.channel.send("https://www.alphavantage.co/query?function=OBV&symbol="+ symbol+"&interval=monthly&apikey='KEY'")
     
keep_alive()
client.run(os.getenv('TOKEN'))
