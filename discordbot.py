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

    if message.content == 'こい':
        await message.channel.send('ボイスチャンネルに参加しろ')
        
    if message.content == 'ねえ':
        await message.channel.send('はい！！')

bot.run(token)
