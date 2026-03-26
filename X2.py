import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_member_join(member):
    channel_id = 1271431183691022398 
    channel = bot.get_channel(channel_id)
    
    if channel:
        try:
            await channel.send(f"Добро пожаловать в мой мир, {member.mention}! Рады тебя видеть!")
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")

    role_id = 148283396685762673 
    role = member.guild.get_role(role_id)
    
    if role:
        try:
            await member.add_roles(role)
            print(f"Роль успешно выдана: {member.name}")
        except Exception as e:
            print(f"Не удалось выдать роль: {e}")
    else:
        print(f"Роль с ID {role_id} не найдена на сервере!")
bot.run(os.getenv('BOT_TOKEN'))
