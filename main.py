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

#Команда startvote (outdated)
#@Bot.command()
#@commands.has_permissions(administrator=True)
#async def startvote(ctx, arg):
#    emb = discord.Embed(title=f'Начато голосование',
#                        description='Голосуем за: ' + str(arg) + '\n' + 'Голосование кончается через 30 секунд',
#                        colour=discord.Color.purple())
#
#    message = await ctx.send(embed=emb) # Возвращаем сообщение после отправки
#    await message.add_reaction('✅')
#    await message.add_reaction('❌')
#    print('>>Sent message about voting. Voting for: ' + str(arg))
#Конец startvote


#Начало группы vote_commands
message_id = 0 # Переменная для сообщения голосования

@Bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def startvote(ctx, content):
    #channel = ctx.channel
    emb = discord.Embed(title=f'Голосование начато.', description='Голосуем за: ' + str(content).lower,
                                  colour=discord.Color.purple())
    message = await ctx.send(embed=emb)
    author = message.get_author()
    print('>>Started voting. Voting about: ' + str(content))
    await message.add_reaction('✅')
    await message.add_reaction('❌')
    global message_id # Если используется класс, то необходимо создать в классе переменную
    message_id = message.id # Сохраняем id сообщения для голосования

@Bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def endvote(ctx):
    channel = ctx.channel
    message = await channel.fetch_message(message_id) # Ищем сообщение
    # Фильтруем реакции, чтобы остались только нужные
    resactions = [reaction for reaction in message.reactions if reaction.emoji in ['✅', '❌']]
    # Превращаем результат голосования в строку (вычитаем 1 из количества, значение по умолчанию)
    result = ''
    for reaction in resactions:
        result += reaction.emoji + ": " + str(reaction.count - 1)
    emb = discord.Embed(title=f'Результат.', description='Итог голосования: ' + str(result),
                                  colour=discord.Color.purple())
    print('>>Voting finished. Result: ' + str(result))
    await ctx.send(embed=emb)
#Конец группы vote_commands

#Начало группы vote_event_commands
message_id = 0 # Переменная для сообщения голосования

@Bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def starteventvote(ctx, content):
    #channel = ctx.channel
    emb = discord.Embed(title=f'Голосование за ивент.', description='Ивент: ' + str(content).lower,
                                  colour=discord.Color.purple())
    message = await ctx.send(embed=emb)
    print('>>Voting for event started. Voting for: ' + str(content))
    await message.add_reaction('✅')
    await message.add_reaction('❌')
    global message_id # Если используется класс, то необходимо создать в классе переменную
    message_id = message.id # Сохраняем id сообщения для голосования

@Bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def endeventvote(ctx):
    channel = ctx.channel
    message = await channel.fetch_message(message_id) # Ищем сообщение
    # Фильтруем реакции, чтобы остались только нужные
    resactions = [reaction for reaction in message.reactions if reaction.emoji in ['✅', '❌']]
    # Превращаем результат голосования в строку (вычитаем 1 из количества, значение по умолчанию)
    result = ''
    for reaction in resactions:
        result += reaction.emoji + ": " + str(reaction.count - 1)
    emb = discord.Embed(title=f'Результат.', description='Итог голосования: ' + str(result),
                                  colour=discord.Color.purple())
    print('>>Voting for event finished. Result: ' + str(result))
    await ctx.send(embed=emb)
#Конец группы vote_event_commands
Bot.run(config.TOKEN)