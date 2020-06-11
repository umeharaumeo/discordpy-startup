from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視
    if message.author.bot:
        return

    if message.content == 'にこちゃん':
        await message.channel.send('にっこにっこに～！')
        
    if message.content == 'ねえ':
        await message.channel.send('はい！！')
        
    if message.content == 'ばろ':
        await message.channel.send('hazupisu#JP1')
        
　　if message.content == '制作者':
        await message.channel.send('はづぴす')
        
    if message.content == 'クリエイトアドバイザー':
        await message.channel.send('おのすにゃん')

bot.run(token)
