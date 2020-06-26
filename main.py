#Зона import
import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
import config
import time
#Конец зоны import
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
                        description='Голосуем за: ' + str(arg),
                        colour=discord.Color.purple())

    message = await ctx.send(embed=emb) # Возвращаем сообщение после отправки
    await message.add_reaction('✅')
    await message.add_reaction('❌')
    print('>>Sent message about voting. Voting for: ' + str(arg))


#Конец startvote

#Начало endvote
@Bot.command  # № 4
@commands.has_permissions(administrator=True)

@Bot.event
async def on_raw_reaction_add(payload):  # №2
    channel = Bot.get_channel(payload.channel_id) # получаем объект канала
    message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
    for emoji in message:
        emoji = payload.emoji
        if emoji == "\N{WHITE HEAVY CHECK MARK}":
            y += 1
        elif emoji == "\N{CROSS MARK}":
            n += 1
    return()

@Bot.event  # № 1
async def on_raw_reaction_remove(payload):  # №2
    channel = Bot.get_channel(payload.channel_id) # получаем объект канала
    message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
    for emoji in message:
        emoji = payload.emoji # реакция пользователя
        if emoji == "\N{WHITE HEAVY CHECK MARK}":
            y -= 1
        elif emoji == "\N{CROSS MARK}":
            n -= 1
    return()

@Bot.command
async def endvote(ctx):
    y = y
    n = n
    if y > n:
        result = 'Принято'  # Voting_ACCEPTED
    elif y == n:
        result = 'Отказано (Да = Нет)'  # Voting_REFUSED (y=n)
    else:
        result = 'Отказано'  # Voting_REFUSED
    emb = discord.Embed(title=f'Окончено голосование.', description = 'Результат: ' + result, colour=discord.Color.purple())
    return await ctx.send(embed=emb) # **Возвращаем** сообщение после отправки.
    y = 0
    n = 0
#Конец endvote

#Команда debug
@Bot.command
async def debug(ctx):
    emb = discord.Embed(title=f'Окно debug.', description='Список переменных дебага:', Y = y)
    return await ctx.send(embed=emb) # **Возвращаем** сообщение после отправки.
Bot.run(config.TOKEN)