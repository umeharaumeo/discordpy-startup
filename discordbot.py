from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

    
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視
    if message.author.bot:
        return

    if message.content == 'こい':
           await message.channel.send('ボイスチャンネルに参加しろ')
            

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
    
@bot.command()
async def こんにちわ(ctx):
    await ctx.send('にっこにっこに～！')

    
    
bot.run(token)
