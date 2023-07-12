import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
def run_commands():
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    discord.Intents.all()
    client = discord.Client(intents=intents)
    bot = commands.Bot(command_prefix='$', intents=intents)
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
    
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said: '{user_message}' {{channel}}")
        
        if user_message[0] == '?':
            user_message = user_message[1:]
            await channel.send(message, user_message, is_private=True)
        else: 
            await channel.send(message, user_message, is_private=False)
    
    @client.event
    async def on_message(message):
        if message.content.startswith('$greet'):
            channel = message.channel
            username = str(message.author)
            await channel.send(f"Hello {username}!")

            def check(m):
                return m.content == 'hello' and m.channel == channel

            msg = await client.wait_for('message', check=check)
            await channel.send(f'Hello {msg.author}!')

        if message.content.startswith('$hug'):
            channel = message.channel
            username = str(message.author)
            await channel.send(f"luv u {username}!")
            
            def check(m):
                return m.content == 'hello' and m.channel == channel
            
            msg = await client.wait_for('message', check=check)
            await channel.send(f'luv u {msg.author}!')
            
        if message.content.startswith('$esex'):
            channel = message.channel
            username = str(message.author)
            await channel.send(f"{username} loves esex!")
            
            def check(m):
                return m.content == 'hello' and m.channel == channel
            
            msg = await client.wait_for('message', check=check)
            await channel.send(f'hello{msg.author}!')
    
    client.run(TOKEN, root_logger=True)
