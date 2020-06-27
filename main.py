#Зона import
import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
import config
import time
#Конец зоны import
I_WAS_TESTING = 0
global n
global y
n = 0
y = 0
result = "?"
msgsent = ''
#Объявления префикса
Bot = commands.Bot(command_prefix= '!')
#Префикс объявлен

#Вывод объявления об активности
@Bot.event
async def on_ready():
    print('>>Bot started. Обычно, ты на этом радуешься)')
#Сепаратор------------------------------------------

#Команда startvote
@Bot.command()
@commands.has_permissions(administrator=True)
async def startvote(ctx, arg):
    emb = discord.Embed(title=f'Начато голосование',
                        description='Голосуем за: ' + str(arg) + '\n' + 'Голосование кончается через 30 секунд',
                        colour=discord.Color.purple())

    message = await ctx.send(embed=emb) # Возвращаем сообщение после отправки
    await message.add_reaction('✅')
    await message.add_reaction('❌')
    print('>>Sent message about voting. Voting for: ' + str(arg))
    @Bot.event()
    @Bot.on_reaction_add()
    emojis = message.get_all_emojis()
    for i in emojis:
        if i == '✅':
            y += 1
        elif i == '❌'
            n += 1
    @Bot.event()
    @Bot.on_reaction_remove()
    emojis = message.get_all_emojis()
    for i in emojis:
        if i == '✅':
            y += 1
        elif i == '❌'
            n += 1
#Конец startvote


#Начало endvote

#Конец endvote

#Команда debug
@Bot.command
async def debug(ctx):
    emb = discord.Embed(title=f'Окно debug.', description='Список переменных дебага:', Y = y)
    return await ctx.send(embed=emb) # **Возвращаем** сообщение после отправки.
Bot.run(config.TOKEN)