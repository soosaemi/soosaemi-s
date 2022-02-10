import discord
import os
import openpyxl
import requests
import asyncio
from json import loads
import random
import datetime

client = discord.Client()



@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("명령어 뭐야 해봐~")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("니애미"):
        await message.channel.send("패드립 하지 마 싹바가지 없는년아")

    if message.content.startswith("느금마"):
        await message.channel.send("패드립 하지 마 싹바가지 없는년아")

    if message.content.startswith("ㄴㅇㅁ"):
        await message.channel.send("패드립 하지 마 싹바가지 없는년아")

    if message.content.startswith("ㄴㄱㅁ"):
        await message.channel.send("패드립 하지 마 싹바가지 없는년아")

    if message.content.startswith("응니"):
        await message.channel.send("그건 너 시발럼아")

    if message.content.startswith("ㄹㅇㅋㅋ"):
        await message.channel.send("한국어 써 씨발롬아")

    if message.content.startswith("?"):
        await message.channel.send("뭐 씨발럼아")

    if message.content.startswith("ㅎㅇ"):
        await message.channel.send("어 그래그래 어서와라 새끼야")

    if message.content.startswith("명령어 뭐야"):
        await message.channel.send("알아서 뭐하게 새끼야!")

    if message.content.startswith("반갑다"):
        await message.channel.send("어 그래그래 반갑다 새끼야~")

    if message.content.startswith("씹새끼야"):
        await message.channel.send("왜 씹새끼야")

    if message.content.startswith("뭐먹을까"):
        await message.channel.send("쳐 굶으세요^^7")

    if message.content.startswith("게임할사람"):
        await message.channel.send("혼자해 응.니")

    if message.content.startswith("겜할사람"):
        await message.channel.send("혼자해 응.니")

    if message.content.startswith("카트"):
        await message.channel.send("그걸 왜해")

    if message.content.startswith("ㅋ"):
        await message.channel.send("웃지마 개새끼야 내가 만만해?")

    if message.content.startswith("ㄴ"):
        await message.channel.send("ㄱ")
        await message.channel.send("ㅁ 시발럼아")

    if message.content.startswith('야 핑'):
        await message.channel.send(f'지금 핑은 {round(client.latency * 1000)}ms 인데 뭐 어쩌라고')

    if message.content.startswith("!정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000 )
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름",value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("골라봐"):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await message.channel.send(choiceresult)


access_token = os.environ[BOT_TOKEN]
client.run("access_token")




