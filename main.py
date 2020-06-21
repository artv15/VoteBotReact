#Зона import
import discord
from discord import utils
import discord.ext
from discord.ext import commands
import config
#Конец зоны import

#Объявления префикса
Bot = commands.Bot(command_prefix= '!')
#Префикс объявлен

#Вывод объявления об активности
@Bot.event
async def on_ready():
    print('>>Bot started.')
#Конец вывода об активности

#Комманда ping
@Bot.command(pass_context= True)
async def ping(ctx):
    await Bot.say('Pong!')
#Конец ping

#Команда startvote
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def startvote(ctx, arg):
    emb = discord.Embed(title=f + str(arg),
                        description='Госование начато',
                        colour=discord.Color.purple())

    message = await ctx.send(embed=emb) # Возвращаем сообщение после отправки
    await message.add_reaction('✅')
    await message.add_reaction('❌')
#Конец startvote
Bot.run(config.TOKEN)