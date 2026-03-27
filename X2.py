import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

processed_members = set()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Sigma"))
    print(f"Бот запущен как {bot.user}")

@bot.event
async def on_member_join(member):
    if member.id in processed_members:
        print(f"Повторный вход {member.name} проигнорирован.")
        return

    processed_members.add(member.id)

    channel_id = 1486288743454474280
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(f"Добро пожаловать в мой мир, {member.mention}! Рады тебя видеть!")
    
    try:
        role_id = 1486283396857626731
        role = member.guild.get_role(role_id)
        if role:
            await member.add_roles(role)
            print(f"Роль выдана пользователю {member.name}")
        else:
            print(f"Роль с ID {role_id} не найдена.")
    except Exception as e:
        print(f"Ошибка при выдаче роли: {e}")

bot.run('ВАШ_ТОКЕН_ЗДЕСЬ') 
