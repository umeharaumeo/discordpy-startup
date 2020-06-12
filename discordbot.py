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
        
    if message.content == 'クリエイトアドバイザー':
        await message.channel.send('おのすにゃん')
        
    if message.content == '制作者':
        await message.channel.send('はづぴす')

    if message.content == '制作':
        await message.channel.send('協力 おのすにゃん\n\n©︎ 2020 はづぴす')
        
    if message.content == 'MJ':
        await message.channel.send('PW 1234\n部屋名 はづぴす')
        
    if message.content == 'すちーむ':
        await message.channel.send('Hazuki.JP')

    if message.content == 'すき':
        await message.channel.send('らぶにこっ(⋈◍＞◡＜◍)。✧♡')
        
    if message.content == 'はづぴす':
        embed = discord.Embed(title='Twitter', description='https://twitter.com/hazupisu', color=0x000200)
        embed.set_thumbnail(url='https://d.kuku.lu/df502ef3d5')
        embed.add_field(name='名前的な', value='内容', inline=True)#
        embed.set_image(url='画像のURL')
        await message.content.send(embed=embed)
        
          
       
        
bot.run(token)
