import discord
import random 

# This has to be put with quotation marks around it "" so that python knows it's a string.
TOKEN = "OTI0MDg3ODI3NjI3NjU1MjM5.YcZd2g.R2L74f8i6EoM78V-ekCBzEYBQT0" 

client = discord.Client()

@client.event 
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event 
async def on_message(message):
   username = str(message.author).split('#')[0]
   user_message = str(message.content)
   channel = str(message.channel.name)
   print(f'{username}:{user_message}({channel})')
  # where did the guy tell you to write the code that did the random numbers?
  # what does it say? A bunch of random words? can come in to my room and show me 
   if message.author == client.user:
      return

   if message.channel.name == 'mfh':
      if user_message.lower() == 'hello':
         await message.channel.send(f'Hello {username}!')
         return
      elif user_message.lower() == 'bye':
         await message.channel.send(f'See you later {username}!')
         return
      elif user_message.lower() == '!random':
         response = f'This your random number {random.randrange(10000000)}'
         await message.channel.send(response)
    


client.run(TOKEN)