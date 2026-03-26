import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event 
async def on_ready():
    print("А вот и я!")

@bot.event
async def on_member_join(member):
    channel_id = 1486288743454474280 
    channel = bot.get_channel(channel_id)

    if channel:
        await channel.send(f"Добро пожаловать в мой мир, {member.mention}! Рады тебя видеть <:Xhi:1486275957370261645>")
@bot.event
async def on_member_join(member):
    role = member.guild.get_role(1486283396685762673)
    if role:
        await member.add_roles(role)
        print(f"Роль выдана пользователю {member.name}")
import os
bot.run(os.getenv('BOT_TOKEN'))

