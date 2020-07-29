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
        await message.channel.send('ただいま♡')
        
    if message.content == 'はづぴす':
        await message.channel.send('ママ大好き♡')
        
    if message.content == 'ただいま':
        await message.channel.send('おかえり♡')
        
    # Get Weather Infomation
def getWeatherInformation(text):
    weather_api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    response_string = ''
    city_id = ''
    if text.find('長野') > -1:
        city_id = '200010'
    elif text.find('大阪') > -1:
        city_id = '270000'
    elif text.find('東京') > -1:
        city_id = '130010'
    elif text.find('北海道') > -1 or text.find('札幌') > -1:
        city_id = '016010'
    elif text.find('愛知') > -1 or text.find('名古屋') > -1:
        city_id = '230010'
    elif text.find('佐賀') > -1:
        city_id = '410010'
    else:
        city_id = '130010'
        response_string += '場所が聞き取れなかったので取り敢えず'

    try:
        params = {'city':city_id}
        response = requests.get(weather_api_url,params=params)
        response_dict = json.loads(response.text)
        title = response_dict["title"]
        description = response_dict["description"]["text"]
        response_string += title + "です！\n\n"
        forecasts_array = response_dict["forecasts"]
        forcast_array = []
        for forcast in forecasts_array:
            telop = forcast["telop"]
            telop_icon = ''
            if telop.find('雪') > -1:
                telop_icon = ':showman:'
            elif telop.find('雷') > -1:
                telop_icon = ':thunder_cloud_and_rain:'
            elif telop.find('晴') > -1:
                if telop.find('曇') > -1:
                    telop_icon = ':partly_sunny:'
                elif telop.find('雨') > -1:
                    telop_icon = ':partly_sunny_rain:'
                else:
                    telop_icon = ':sunny:'
            elif telop.find('雨') > -1:
                telop_icon = ':umbrella:'
            elif telop.find('曇') > -1:
                telop_icon = ':cloud:'
            else:
                telop_icon = ':fire:'

            temperature = forcast["temperature"]
            min_temp = temperature["min"]
            max_temp = temperature["max"]
            temp_text = ''
            if min_temp is not None:
                if len(min_temp) > 0:
                    temp_text += '\n最低気温は' + min_temp["celsius"] + "℃"
            if max_temp is not None:
                if len(max_temp) > 0:
                    temp_text += '\n最高気温は' + max_temp["celsius"] + "℃"

            forcast_array.append(forcast["dateLabel"] + ' ' + telop + telop_icon + temp_text)
        if len(forcast_array) > 0:
            response_string += '\n\n'.join(forcast_array)
        response_string += '\n\n' + description
    except Exception as e:
        response_string = '天気検索でエラーです＞＜ :cold_sweat:\n' + e.message + '\n' + str(e)
    return response_string

        


# Botの起動とDiscordサーバーへの接続
client.run(token)
