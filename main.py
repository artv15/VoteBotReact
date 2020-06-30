#Зона import
import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
import config
import random
import string
#Конец зоны import
#Объявление глобальных переменных
pass_key = buildblock(8)
print('>>Password for debug created. Password: ' + pass_key)
#Переменные объявлены
result = "?"
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
    emb = discord.Embed(title=f'Голосование начато.', description='Голосуем за: ' + str(content),
                                  colour=discord.Color.purple())
    message = await ctx.send(embed=emb)
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
    FinalResultY = result[3]
    FinalResultN = result[7]
    if FinalResultY > FinalResultN:
        Final = 'Принято'
    elif FinalResultY == FinalResultN:
        Final = 'Голоса равны. Решение за организатором голосования.'
    elif FinalResultY < FinalResultN:
        Final = 'Отказано.'
    emb = discord.Embed(title=f'Результат.', description='Голоса: ' + str(result),
                                  colour=discord.Color.purple())
    emb.add_field(name="Итог: ", value=Final, inline=True)
    print('>>Voting finished. Result: ' + str(result) + ' Final result: ' + Final)
    await ctx.send(embed=emb)
#Конец группы vote_commands

#Начало группы vote_event_commands
message_id = 0 # Переменная для сообщения голосования

@Bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def starteventvote(ctx, content):
    #channel = ctx.channel
    emb = discord.Embed(title=f'Голосование за ивент.', description='Ивент: ' + str(content),
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
    #Посчёт результата(Принято/Отказано)
    FinalResultY = result[3]
    FinalResultN = result[7]
    if FinalResultY > FinalResultN:
        Final = 'Принято'
    elif FinalResultY == FinalResultN:
        Final = 'Голоса равны. Решение за организатором голосования.'
    elif FinalResultY < FinalResultN:
        Final = 'Отказано.'
    emb = discord.Embed(title=f'Результат.', description='Итог голосования: ' + str(result),
                                  colour=discord.Color.purple())
    emb.add_field(name="Итог: ", value=Final, inline=True)
    print('>>Voting for event finished. Result: ' + str(result) + ' Final result: ' + Final)
    await ctx.send(embed=emb)
#Конец группы vote_event_commands



#Начало группы Debug
@Bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def debug(ctx, passwd):
    if passwd == pass_key:
        emb = discord.Embed(title=f'Debug menu opened.', description='Here shown all vars, which are required in DeBug.', colour=0x00ff08)
        emb.add_field(name='Information', value='There are 0 vars to debug!')
        emb.add_field(name='var', value='null')
        emb.add_field(name='Attention!', value='If you can see debug menu, without running !debug with using valid passwd, then do not save any of this data. Thank you for attention(now get out)')
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(title=f'Incorrect password received.', description='Access denied.', colour=0xff0000)
        await ctx.send(embed=emb)

    def buildblock(size):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))
    pass_key = buildblock(8)
    print('Password for debug regenerated. Please, use this password: ' + pass_key)
#Конец группы Debug
Bot.run(config.TOKEN)