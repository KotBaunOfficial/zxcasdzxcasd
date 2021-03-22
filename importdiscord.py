import discord
from discord.ext import commands
import asyncio
import os

client = commands.Bot(command_prefix = '/' )

bot = commands.Bot(command_prefix = '/')

@client.command(pass_context =True)
async def clear( ctx, amount : int ):
    await ctx.channel.purge( limit = int(amount) )
    await ctx.send('Работаю я тут за тебя, а ты...', delete_after= 4.0)

token = os.envrion.get('BOT_TOKEN')

client.run(str(token))
