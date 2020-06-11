from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
    
@bot.command()
async def hey(ctx):
    await ctx.send('にっこにっこに～！')
    
    
@bot.command()
async def valo(ctx):
    await ctx.send('hazupisu#JP1')
    
    
bot.run(token)
