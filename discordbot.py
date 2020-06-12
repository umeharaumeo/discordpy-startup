import discord
import os

token = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if message.content == 'ID':
        embed = discord.Embed(title='おのすにゃん', description='', color=0xff0000)
        embed.add_field(name="Switch", value="0884-9004-7707", inline=True)
        embed.add_field(name="Origin", value="mgmgOI4i", inline=True)
        embed.add_field(name="VALORANT", value="もぐもぐおいしい #JP1", inline=True)
        await message.channel.send(embed=embed)
        
    if message.content == 'ふれんど':
        embed = discord.Embed(title='はづぴす', description='', color=0xff0000)
        embed.add_field(name="VALORANT", value="hazupisu#JP1", inline=True)
        embed.add_field(name="Origin", value="hazupisu", inline=True)
        embed.add_field(name="Steam", value="Hazuki.JP", inline=True)
        await message.channel.send(embed=embed)

    if message.content == 'クラウド':
        await message.channel.send('時代はクラウド')

    if message.content == 'にこちゃん':
        await message.channel.send('にっこにっこに～！')
        
    if message.content == 'ねえ':
        await message.channel.send('はい！！')
        
    if message.content == 'クリエイトアドバイザー':
        await message.channel.send('おのすにゃん')
        
    if message.content == '制作者':
        await message.channel.send('はづぴす')

    if message.content == '制作':
        await message.channel.send('協力 おのすにゃん\n\n©︎ 2020 はづぴす')
        
    if message.content == 'MJ':
        await message.channel.send('PW 1234\n部屋名 はづぴす')

    if message.content == 'すき':
        await message.channel.send('らぶにこっ(⋈◍＞◡＜◍)。✧♡')
        
    if message.content == 'おかえり':
        await message.channel.send('ただいまママ♡')
        
    if message.content == 'はづぴす':
        await message.channel.send('ママ大好き♡')
        
    if message.content == 'ただいま':
        await message.channel.send('おかえりママ♡')
        
　　if message.content == 'すき':
        await message.channel.send('だまれ')
        print(message.author.345226218309681173)
        


# Botの起動とDiscordサーバーへの接続
client.run(token)
