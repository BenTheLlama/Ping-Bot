import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Ready To Ping')

@client.command()
async def ping1531684364(ctx,*,question):
    count = 0
    while (count < 1):
        await ctx.send(f'{question}')



client.run('Imput Bot Token')
