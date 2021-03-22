import discord
from discord.ext import commands
import asyncio

token = "ODIzMjcwMTc5NjkyNzQwNjE4.YFeYGg.mu_r3F8ICdDOpHV4N3HEuymWcPE"

client = commands.Bot(command_prefix = '/' )

bot = commands.Bot(command_prefix = '/')

@client.command(pass_context =True)
async def clear( ctx, amount : int ):
    await ctx.channel.purge( limit = int(amount) )
    await ctx.send('Работаю я тут за тебя, а ты...', delete_after= 4.0)

client.run(token)