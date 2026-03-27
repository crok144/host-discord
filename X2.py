import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("А вот и я!")

@bot.event
async def on_member_remove(member):
    channel_id = 1486995771365523568
    channel = bot.get_channel(channel_id)

    if channel:
        await channel.send(f"{member.name}, ты меня УТОМЛЯЕШЬ!")
        print(f"Пользователь {member.name} вышел с сервера.")

@bot.event
async def on_member_join(member):
    channel_id = 1486288743454474280
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(f"Добро пожаловать в мой мир, {member.mention}! Рады тебя видеть!")

    role_id = 1486283396685762673
    role = member.guild.get_role(role_id)
    if role:
        await member.add_roles(role)
        print(f"Роль выдана пользователю {member.name}")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Я сигма"))
    print(f"Запущен как {bot.user}")

bot.run(os.getenv('BOT_TOKEN'))
